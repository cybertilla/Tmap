# -*- coding: utf-8 -*-
import requests
import sqlite3
import config
import twitterApi
#import relevant stuff

my_headers = {'Authorization' : 'Bearer ' + config.twitterBearerToken}
trend_world = requests.get('https://api.twitter.com/1.1/trends/available.json', headers=my_headers)
trending_now = trend_world.json()

def setup():
    '''
    The database is used only for authentication
    '''
    pass
    '''
    conn = sqlite3.connect('tmap.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS user")
    c.execute("CREATE TABLE user (id VARCHAR PRIMARY KEY, password TEXT)")
    conn.commit()
    conn.close()
    '''

def display_map():
    '''
    Shows the world map from GoogleMapAPI
    '''
    #Get request to Google Map API
    return map

def display_country(name):
    woeid = " "
    #print("från display_country: " + name)
    

    for trend in trending_now:
        
        if(trend['name'] == name): # we switch this to a paramiter från the user input
            woeid = trend['woeid']
            trend_place = requests.get('https://api.twitter.com/1.1/trends/place.json?id='+ str(woeid) , headers=my_headers)

    #print(trend['name'], trend['country'], trend['woeid'])




#plocka ut name, url, välja ut det som har mest tweet volume.


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
                #print(x)
                list1.append(x)
            




    likes = 0
    list2 = []
    resource_url = requests.get('https://api.twitter.com/1.1/search/tweets.json?q=' + list1[0]['name'] + '&result_type=popular', headers =my_headers)
    resource_url = resource_url.json()


    for res in resource_url['statuses']:
        
        for r in res['text']:

            if(res['favorite_count'] > likes):

                list2.clear()
                likes = res['favorite_count']
                #print("innan: ", likes)
                text = res['text']
                #print(re.search("(?P<url>https?://[^\s]+)", text).group("url"))
                list2.append(res['text'])
                list2.append(re.search("(?P<url>https?://[^\s]+)", text).group("url"))
                list2.append(res['favorite_count'])
                #print(list2)


'''
Centers map on specifi town, calls Twitter API for hashtag data
Returns JSON object??
>>>>>>> 7cbbacd92f0e10c6b4d9d3e71207779b57a8b648
    '''

def add_town(coordinates):
    '''
    Requests a new town and its trending hashtag.
    '''
    pass

def update_hashtag(coordinates):
    '''
    Updates the map to see if hashtag has changed
    '''
    pass

def remove_town(coordinates):
    '''
    Remove a town from the map, resets to world map
    '''
    pass
