import requests
import json
from flask import Flask, request

app = Flask(__name__)
app.config.from_object("config.Config")

@app.route("/<string:id>")
def get_document(id:str):
    """
    Get a Panviva document id from the Http request and construct a compact Json payload by
    calling multiple API calls to Panviva.
    """

    # start and set headers for requests.
    req_session = requests.Session()
    req_session.headers.update({"Ocp-Apim-Subscription-Key":app.config['API_KEY'],"Accept":"application/json"})

    # Call API Endpoints and return error if unsuccessfull
    document_result = req_session.get(f"{app.config['BASE_URL']}/v3/{app.config['INSTANCE']}/resources/document/{id}")

    if(document_result.status_code != 200):
        return document_result.content, document_result.status_code
    
    containers_result = req_session.get(f"{app.config['BASE_URL']}/v3/{app.config['INSTANCE']}/resources/document/{id}/containers")

    if(containers_result.status_code != 200):
        return containers_result.content, containers_result.status_code

    translations_result = req_session.get(f"{app.config['BASE_URL']}/v3/{app.config['INSTANCE']}/resources/document/{id}/translations")

    if(translations_result.status_code != 200):
        return translations_result.content, translations_result.status_code

    # Load responces to JSON objects.
    document_json_obj = json.loads(document_result.content)
    containers_json_obj = json.loads(containers_result.content)
    translations_json_obj = json.loads(translations_result.content)

    #Construct the final payload.
    keyword_for_containers = 'containers'
    keyword_for_translations = 'translations'
    keyword_for_relations = 'links'

    del document_json_obj[keyword_for_relations]
    document_json_obj[keyword_for_translations] = translations_json_obj[keyword_for_translations]
    document_json_obj[keyword_for_containers] = containers_json_obj[keyword_for_containers]

    # Send the modified document JSON payload.
    return json.dumps(document_json_obj), 200

if __name__ == "__main__":
    app.run()