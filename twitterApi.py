import requests
from requests.models import to_native_string
import config
import json
import re

my_headers = {'Authorization' : 'Bearer ' + config.twitterBearerToken}
trend_world = requests.get('https://api.twitter.com/1.1/trends/available.json', headers=my_headers)
trending_now = trend_world.json()


def getCountry(name):
    for trend in trending_now:
        
        if(trend['name'] == name): # we switch this to a paramiter från the user input
            woeid = trend['woeid']

        #print(trend['name'], trend['country'], trend['woeid'])

    trend_place = requests.get('https://api.twitter.com/1.1/trends/place.json?id='+ str(woeid) , headers=my_headers)
    return trend_place.json()


#plocka ut name, url, välja ut det som har mest tweet volume.

def getTheTrendingTweets(trend_place):
    list1 = []
    maxNum = 0

    for trends in trend_place:

        for t in trends['trends']:

            if(t['tweet_volume'] == 'None' or t['tweet_volume'] is None):
                pass
                
            elif(t['tweet_volume'] > maxNum):
                list1.clear()
                maxNum = t['tweet_volume']
                x = {
                    "tweet_volume": t['tweet_volume'],
                    "name": t['name'],
                    "url": t['url']
                }
                list1.append(x)

    return list1


def getTextToTranslate(list1):

    likes = 0
    list2 = []
    key = list1[0]['name'].replace('#', " ")
    resource_url = requests.get('https://api.twitter.com/1.1/search/tweets.json?q=' + key + '&result_type=popular', headers =my_headers)
    resource_url = resource_url.json()


    for res in resource_url['statuses']:
        
        for r in res['text']:
            if(res['favorite_count'] > likes):
                    list2.clear()
                    likes = res['favorite_count']
                    text = res['text']
                    list2.append(re.search("(?P<url>https?://[^\s]+)", text).group("url"))
                    text = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', text)
                    list2.append(text)
                    
                    list2.append(res['favorite_count'])
                    #print(list2)
    return list2




test = getCountry('Turkey')
#print(test)

text = getTheTrendingTweets(test)
print("getTheTrendingTweet: ", text)
trans = getTextToTranslate(text)
print("getTextToTranslate: ",trans)


