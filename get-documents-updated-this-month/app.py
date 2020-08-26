from __future__ import print_function
from datetime import datetime
import panviva
from panviva.rest import ApiException
from pprint import pprint
import html2text
from config import Config

h = html2text.HTML2Text()
h.ESCAPE_SNOB = True

config = Config()
panviva_configuration = panviva.Configuration()
panviva_configuration.api_key['Ocp-Apim-Subscription-Key'] = config.panviva['api_key']

resources_api_instance = panviva.ResourcesApi(panviva.ApiClient(panviva_configuration))
operations_api_instance = panviva.OperationsApi(panviva.ApiClient(panviva_configuration))
instance = config.panviva['instance']

def monthdelta(date, delta):
    m, y = (date.month+delta) % 12, date.year + ((date.month)+delta-1) // 12
    if not m: m = 12
    d = min(date.day, [31,
        29 if y%4==0 and not y%400==0 else 28,31,30,31,30,31,31,30,31,30,31][m-1])
    return date.replace(day=d,month=m, year=y)

def search_documents_generator(instance, term):
    has_more_docs = True
    page_limit = 20
    page_offset = 0
    
    while has_more_docs:
        search_response = operations_api_instance.operations_search(instance, term, page_offset=page_offset, page_limit=page_limit)
        if not search_response.results:
            return
        yield search_response
        
        has_more_docs = (page_offset + 1) * page_limit < search_response.total
        page_offset += 1

try:
    documents = []
    datetime_lastmonth = monthdelta(datetime.now(), -1)
    term = 'data.attributes.updatedDate:{' + datetime_lastmonth.strftime("%Y-%m-%d") + ' TO *}' # str | all documents with updated date since 2020-08-01 to now

    for search_response in search_documents_generator(instance, term):
        for document_result in search_response.results:
            document = vars(document_result)
            document["containers"] = []
            document_containers = resources_api_instance.resources_document_by_id_containers(instance, document["_id"])

            for container in document_containers.containers:
                if not container.body:
                    continue
                container_raw_text = h.handle(container.body)
                document["containers"].append(container_raw_text)
            documents.append(document)
    pprint(documents)
except ApiException as e:
    print("Exception when calling creating Panviva document: %s\n" % e)
