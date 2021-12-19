# -*- coding: utf-8 -*-

import re
from flask import Flask, jsonify, request, url_for, render_template
import storage as storage
import json
import config


app = Flask(__name__)
storage.setup()

@app.route("/places", methods=['GET'])
def display_map():
    '''
    At this endpoint we show the full world map via Google maps
    '''
    key=config.MapsAPIKey
    return render_template("maps.html", key=key)


@app.route("/places/<name>", methods=['GET'])
def display_map1(name):
    '''
    At this endpoint we show the specific location map
    '''
    print("från route: " + name)
    text = storage.display_country(name)
    y = json.dumps(json.loads(text), indent=4, sort_keys=True, default=str)
    return y

    

@app.route("/apidocs/", methods=['GET'])
def swagger():
    '''
    shows documentation for the apidocs
    '''
    pass
