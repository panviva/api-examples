import json
import sys

class Config(object):

    # try and load the file
    try:
        settings_file = open('settings.json')
    except:
        print("Error : could not load the 'settings.json' file")
        sys.exit()

    # read data from settings.json
    with settings_file:
        data = json.load(settings_file)

    BASE_URL = data['BaseUrl']
    INSTANCE = data['Instance']
    API_KEY = data['ApiKey']

    if BASE_URL == "" or INSTANCE == "" or API_KEY == "":
        print("Error : invalid data in 'settings.json' file")
        sys.exit()
