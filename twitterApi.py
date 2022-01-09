from typing import _ProtocolMeta
import requests
from requests.models import to_native_string
import config
import json
import re

my_headers = {'Authorization' : 'Bearer ' + config.twitterBearerToken}
trend_world = requests.get('https://api.twitter.com/1.1/trends/available.json', headers=my_headers)
trending_now = trend_world.json()

'''Returns a list of countries'''
def country_list():
    for trend in trending_now:
        print(trend['name'], trend['country'])


'''Turns a name(String) of a country to an ID
    Makes a GET request from Twitter API of the trending topics from the chosen country
'''
def getPlace(name):
    if(name == 'USA'):
        name = 'United States'
    if(name == 'South Korea' or name == 'North Korea'):
        name = 'Korea'
    if(name == 'Riyadh Province Saudi Arabia'):
        name = 'Saudi Arabia'
    for trend in trending_now:
        
        if(trend['name'] == name): 
            woeid = trend['woeid']
            trend_place = requests.get('https://api.twitter.com/1.1/trends/place.json?id='+ str(woeid) , headers=my_headers)
            trend_place = trend_place.json()

    trend_place = requests.get('https://api.twitter.com/1.1/trends/place.json?id='+ str(woeid) , headers=my_headers)
    return trend_place.json()


'''Gets the list of the trends, takes the one that has the highest number of likes and returns a list of name, tweet_volume and the url'''

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


'''Gets a list, makes a GET request to Twitter API to search for tweets of the trending topic, takes the tweet with the highest likes and 
   return a list with topic, text,url and likes'''
def getTextFromTrending(list1):

    likes = 0
    list2 = []
    key = list1[0]['name'].replace('#', " ")
    resource_url = requests.get('https://api.twitter.com/1.1/search/tweets.json?q=' + key + '&result_type=popular', headers =my_headers)
    resource_url = resource_url.json()


    for res in resource_url['statuses']:
        
        res['truncated'] = 'False'
        for r in res['entities']['urls']:
            
            if(res['favorite_count'] > likes):
            
                list2.clear()
                text = re.sub(r'http\S+', '', res['text'])
                likes = res['favorite_count']
                url = r['url']
                             
                x2 = {
                    "topic": list1[0].get('name',' '),
                    "text": text,
                    "url": url,
                    "likes": likes
                }

                list2.append(x2)

    return list2


