from typing import _ProtocolMeta
import requests
from requests.models import to_native_string
import config
import json
import re

my_headers = {'Authorization' : 'Bearer ' + config.twitterBearerToken}
trend_world = requests.get('https://api.twitter.com/1.1/trends/available.json', headers=my_headers)
trending_now = trend_world.json()

#Does not return a list YET
def country_list():
    for trend in trending_now:
        print(trend['name'], trend['country'])


def getPlace(name):
    if(name == 'USA'):
        name = 'United States'
    if(name == 'South Korea' or name == 'North Korea'):
        name = 'Korea'
    if(name == 'Riyadh Province Saudi Arabia'):
        name = 'Saudi Arabia'
    for trend in trending_now:
        
        if(trend['name'] == name): # we switch this to a paramiter från the user input
            woeid = trend['woeid']
            trend_place = requests.get('https://api.twitter.com/1.1/trends/place.json?id='+ str(woeid) , headers=my_headers)
            trend_place = trend_place.json()
        #print(trend['name'], trend['country'], trend['woeid'])

    trend_place = requests.get('https://api.twitter.com/1.1/trends/place.json?id='+ str(woeid) , headers=my_headers)
    return trend_place.json()

   # trend_place = requests.get('https://api.twitter.com/1.1/trends/place.json?id='+ str(woeid) , headers=my_headers)

    #return getTheTrendingTweets(trend_place)


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
        #text = res['text']
        #fav_point = res['favorite_count']
        res['truncated'] = 'False'
        for r in res['entities']['urls']:
            #url = r['url']
            if(res['favorite_count'] > likes):
            
                list2.clear()
                text = re.sub(r'http\S+', '', res['text'])
                likes = res['favorite_count']
                url = r['url']
                                
                x2 = {
                    "text": text,
                    "url": url,
                    "likes": likes
                }

                list2.append(x2)

    return list2


'''test = getCountry('Turkey')
print(test)

text = getTheTrendingTweets(test)
print(text[0]['name'])
print("getTheTrendingTweet: ", text)
trans = getTextToTranslate(text)
print("getTextToTranslate: ",trans)'''

country_list()
