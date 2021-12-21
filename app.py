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

#Funkar typ
'''@app.route("/translated", methods=['POST'])
def translate():
    #translatedText = translateAPI.translate(text)
    text = request.form.get('translate')
    translateRequests = requests.get("https://translation.googleapis.com/language/translate/v2?key=" + config.googleKeyTranslate + "&q=" + text + "&target=en")
    test = translateRequests.json()
    print(translateRequests.json)
    y = json.dumps(test, indent=4, sort_keys=True, default=str, ensure_ascii=False).encode('UTF-8')
    return y'''

@app.route("/translated/<text>", methods=['POST'])
def translate(text):
    #translatedText = translateAPI.translate(text)
    text = request.form.get('submit_translate') == 'button'
    print(type(text))
    print(text)
    translateRequests = requests.get("https://translation.googleapis.com/language/translate/v2?key=" + config.googleKeyTranslate + "&q=" + text + "&target=en")
    test = translateRequests.json()
    print(test)
    y = json.dumps(test, indent=4, sort_keys=True, default=str, ensure_ascii=False).encode('UTF-8')
    return render_template("index.html", y=y)

@app.route('/tweets/<name>', methods=['GET'])
def display_map1(name):

    country = twitterApi.getCountry(name)
    list = twitterApi.getTheTrendingTweets(country)
    list1 = twitterApi.getTextToTranslate(list)
    #y = json.dumps(list1, indent=4, sort_keys=True, default=str, ensure_ascii=False).encode('UTF-8')
    #y = y.decode()
    print(list1)
    list1=list1[0]['text']
    return render_template("index.html", y=list1)

            

    #print(trend['name'], trend['country'], trend['woeid'])
    #text = storage.display_country(name)
    #y = json.dumps(json.loads(text), indent=4, sort_keys=True, default=str)

@app.route("/apidocs", methods=['GET'])
def swagger():
    '''
    shows documentation for the apidocs
    '''
    return render_template("docs.html")
