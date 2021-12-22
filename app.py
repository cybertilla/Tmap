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


@app.route('/translated/<text>', methods=['POST'])
def translate(text):

    y = translateAPI.translate(text)
    y = y.decode()
    
    return render_template("index.html", y=y)

@app.route('/tweets/<name>', methods=['GET'])
def display_map1(name):

    country = twitterApi.getCountry(name)
    list = twitterApi.getTheTrendingTweets(country)
    list1 = twitterApi.getTextToTranslate(list)
    list1=list1[0]['text']
    list1 = list1.replace('#', " ")
    return render_template("index.html", y=list1)

            

@app.route("/apidocs", methods=['GET'])
def swagger():
    '''
    shows documentation for the apidocs
    '''
    return render_template("docs.html")
