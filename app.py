# -*- coding: utf-8 -*-

import requests
from flask import Flask, jsonify, request, url_for, render_template
import storage as storage
import json
import config

import twitterApi
import translateAPI
#import relevant objects

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



@app.route("/translated/<text>", methods=['POST'])
def translate(text):
    #translatedText = translateAPI.translate(text)
    translateRequests = requests.get("https://translation.googleapis.com/language/translate/v2?key=" + config.googleKeyTranslate + "&q=" + text + "&target=en")
    test = translateRequests.json()
    print(translateRequests.json)
    y = json.dumps(test, indent=4, sort_keys=True, default=str, ensure_ascii=False).encode('UTF-8')
    print(y)
    return ""


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

    
    
    #return translatedText





@app.route('/tweets/<name>', methods=['GET'])
def display_map1(name):

    country = twitterApi.getCountry(name)
    list = twitterApi.getTheTrendingTweets(country)
    list1 = twitterApi.getTextToTranslate(list)
    y = json.dumps(list1, indent=4, sort_keys=True, default=str, ensure_ascii=False).encode('UTF-8')
    return y.decode()

            

    #print(trend['name'], trend['country'], trend['woeid'])
    #text = storage.display_country(name)
    #y = json.dumps(json.loads(text), indent=4, sort_keys=True, default=str)


           
    
    

@app.route("/apidocs", methods=['GET'])
def swagger():
    '''
    shows documentation for the apidocs
    '''
    return render_template("docs.html")
