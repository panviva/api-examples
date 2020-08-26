from __future__ import print_function
import time
import panviva
from panviva.rest import ApiException
from pprint import pprint
from config import Config
import html2text

h = html2text.HTML2Text()
h.ESCAPE_SNOB = True

config = Config()
panviva_configuration = panviva.Configuration()
panviva_configuration.api_key['Ocp-Apim-Subscription-Key'] = config.panviva['api_key']

api_instance = panviva.ResourcesApi(panviva.ApiClient(panviva_configuration))
instance = config.panviva['instance']
id = '100' # str | A document unique identifier, Document ID. If a document is a translated document, this value represents Internal ID or IID in Panviva API v1.

try:
    document_metadata = api_instance.resources_document_by_id(instance, id)
    document_containers = api_instance.resources_document_by_id_containers(instance, id)
    document = vars(document_metadata)
    document["containers"] = []
    
    for container in document_containers.containers:
        if not container.body:
            continue
        container_raw_text = h.handle(container.body)
        document["containers"].append(container_raw_text)
    
    pprint(document)
except ApiException as e:
    print("Exception when calling creating Panviva document: %s\n" % e)
