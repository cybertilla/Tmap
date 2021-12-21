# -*- coding: utf-8 -*-

import re
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
 # Det här nollställer databasen inför varje körning

# Jag har låtit varje enskild metod- och URL-kombination få en egen funktion.
# Det går lika bra att köra två funktioner (en för / och en för /id) och bara
# titta efter vilket verb som användes vid anropet. Hur dessa definieras finns
# dokumenterat på
# https://flask.palletsprojects.com/en/2.0.x/api/url-route-registrations

# Den alternativa lösningen som beskrivs ovan
#@app.route("/<int: id>", methods=['GET', 'POST'])
#def handle_unicorn(id: int):
#    if request.method == 'GET':
#        pass
#    elif request.method == 'POST':
#        pass

@app.route('/places', methods=['GET'])
def display_map():
    '''
    At this endpoint we show the full world map via Google maps
    '''
    return render_template("index.tpl")


@app.route("/translated/<text>", methods=['POST'])
def translate(text):
    #translatedText = translateAPI.translate(text)
    
    translateRequests = requests.get("https://translation.googleapis.com/language/translate/v2?key=" + config.googleKeyTranslate + "&q=" + text + "&target=en")
    test = translateRequests.json()
    print(translateRequests.json)
    y = json.dumps(test, indent=4, sort_keys=True, default=str, ensure_ascii=False).encode('UTF-8')
    print(y)
    return ""
    #return translatedText




@app.route('/tweets/<name>', methods=['GET'])
def display_map1(name):

    country = twitterApi.getCountry(name)
    list = twitterApi.getTheTrendingTweets(country)
    list1 = twitterApi.getTextToTranslate(list)
    y = json.dumps(list1, indent=4, sort_keys=True, default=str, ensure_ascii=False).encode('UTF-8')
    return y.decode()
           
    
    

@app.route("/apidocs/", methods=['GET'])
def swagger():
    '''
    shows documentation for the apidocs
    '''
    pass
