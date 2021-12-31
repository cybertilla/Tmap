import requests
import config
import json

def translate(text):
    translateRequests = requests.get("https://translation.googleapis.com/language/translate/v2?key=" + config.googleKeyTranslate + "&q=" + text + "&target=en")
    test = translateRequests.json()    
    y = json.dumps(test['data' ]['translations'][0]['translatedText'], indent=4, sort_keys=True, default=str, ensure_ascii=False).encode('UTF-8')
    return y
