import requests
import config
import json

def translate(text):

    #text = 'Hej, jag heter Linn'
    #OBS gör inte mer sökning än vad som behövs då vi inte vet hur många request man ska göra. Fråga eric!!
    translateRequests = requests.get("https://translation.googleapis.com/language/translate/v2?key=" + config.googleKeyTranslate + "&q=" + text + "&target=es")
    test = translateRequests.json()

    y = json.dumps(test, indent=4, sort_keys=True, default=str)
    return y
    #text = twitterApi.getTextToTranslate()
#OBS gör inte mer sökning än vad som behövs då vi inte vet hur många request man ska göra. Fråga eric!!
    #translateRequests = requests.get("https://translation.googleapis.com/language/translate/v2?key=" + config.googleKeyTranslate + "&q=" + text + "&target=es")
    #return translateRequests.json()

#test = translateRequests.json()
#print(translate())