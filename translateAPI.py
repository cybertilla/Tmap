import requests
import config
import twitter_test



text = twitter_test.getTextToTranslate()
#OBS gör inte mer sökning än vad som behövs då vi inte vet hur många request man ska göra. Fråga eric!!
translateRequests = requests.get("https://translation.googleapis.com/language/translate/v2?key=" + config.googleKeyTranslate + "&q=" + text + "&target=es")


test = translateRequests.json()
print(test)