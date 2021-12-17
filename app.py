# -*- coding: utf-8 -*-

import re
from flask import Flask, jsonify, request, url_for, render_template
import storage as storage
import json
#import relevant objects

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

@app.route("/places", methods=['GET'])
def display_map():
    '''
    At this endpoint we show the full world map via Google maps
    '''
    return render_template("index.tpl")


@app.route("/places/<name>", methods=['GET'])
def display_map1(name):
    print("från route: " + name)
    text = storage.display_country(name)
    y = json.dumps(json.loads(text), indent=4, sort_keys=True, default=str)
    return y
    '''
    At this endpoint we show the full world map via Google maps
    '''
    

@app.route("/apidocs/", methods=['GET'])
def swagger():
    '''
    shows documentation for the apidocs
    '''
    pass
