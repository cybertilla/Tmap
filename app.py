# -*- coding: utf-8 -*-

import requests
from flask import Flask, jsonify, request, url_for, render_template
import storage as storage
import json
import config


my_headers = {'Authorization' : 'Bearer ' + config.twitterBearerToken}
trend_world = requests.get('https://api.twitter.com/1.1/trends/available.json', headers=my_headers)
trending_now = trend_world.json()

app = Flask(__name__)
storage.setup()

@app.route('/', methods=['GET'])
def homepage():
    '''
    Homepage
    '''
    return render_template("index.html")



@app.route('/places', methods=['GET'])
def display_map():
    '''
    At this endpoint we show the full world map via Google maps
    '''
    key = config.MapsAPIKey
    return render_template("maps.html", key=key)


@app.route('/places/<name>', methods=['GET'])
def display_location(name):
    #print("from display_country: " + name)
    print(name)
    for trend in trending_now:
        
        if(trend['name'] == name): # we switch this to a parameter from the user input
            print(name)
            woeid = trend['woeid']
            trend_place = requests.get('https://api.twitter.com/1.1/trends/place.json?id='+ str(woeid) , headers=my_headers)
            trend_place = trend_place.json()
        
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

    likes = 0
    list2 = []
    list3 = []
    key = list1[0]['name'].replace('#', " ")
    resource_url = requests.get('https://api.twitter.com/1.1/search/tweets.json?q=' + key + '&result_type=popular', headers =my_headers)
    resource_url = resource_url.json()

    print(key)
    for res in resource_url['statuses']:
        
        for r in res['text']:

            if(res['favorite_count'] > likes):
            
                list2.clear()
                text = res['text']
                likes = res['favorite_count']
                url = res['urls']
                                
                x2 = {
                    "text": text,
                    "url": url,
                    "likes": likes
                }

                print("text: ",text)
                print("url: ",url)
                list2.append(x2)
                    #print("innan: ", likes)
                    #print(re.search("(?P<url>https?://[^\s]+)", text).group("url"))
                    #list2.append(res['text'])
                    #list2.append(re.search("(?P<url>https?://[^\s]+)", text).group("url"))
                    #list2.append(res['favorite_count'])
                    #print(list2)
    

    y = json.dumps(list2, indent=4, sort_keys=True, default=str)
    print(y)


    return y
            

    #print(trend['name'], trend['country'], trend['woeid'])
    #text = storage.display_country(name)
    #y = json.dumps(json.loads(text), indent=4, sort_keys=True, default=str)
           
    
    

@app.route("/apidocs", methods=['GET'])
def swagger():
    '''
    shows documentation for the apidocs
    '''
    pass
