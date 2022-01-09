import requests
import config
import json
import urllib.parse

'''
Gets a text to translate to english
Makes a GET request to Cloud Translate API and returns the translated text
'''
def translate(text):
    text = urllib.parse.quote(text)
    query = "https://translation.googleapis.com/language/translate/v2?key=" + config.googleKeyTranslate + "&q=" + text + "&target=en"
    translateRequests = requests.get(query)
    test = translateRequests.json()
    y = json.dumps(test['data' ]['translations'][0]['translatedText'], indent=4, sort_keys=True, default=str, ensure_ascii=False).encode('UTF-8')
    return y
