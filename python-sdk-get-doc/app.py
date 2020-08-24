from __future__ import print_function
import time
import panviva
from panviva.rest import ApiException
from pprint import pprint
import html2text

h = html2text.HTML2Text()
h.ESCAPE_SNOB = True

# Configure API key authorization: apiKeyHeader
configuration = panviva.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'

api_instance = panviva.ResourcesApi(panviva.ApiClient(configuration))
instance = 'instancename' # str | The instance name as shown on the Panviva Developer Portal.
id = '100' # str | A document unique identifier, Document ID. If a document is a translated document, this value represents Internal ID or IID in Panviva API v1.

try:
    # Document
    document_metadata = api_instance.resources_document_by_id(instance, id)
    document_containers = api_instance.resources_document_by_id_containers(instance, id)
    document = document_metadata.__dict__
    document["containers"] = []
    
    for container in document_containers.containers:
        container_raw_text = h.handle(container.body)
        document["containers"].append(container_raw_text)
    
    pprint(document)
except ApiException as e:
    print("Exception when calling ResourcesApi->resources_document_by_id: %s\n" % e)
