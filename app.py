# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request, url_for, render_template
import storage as storage
import config
#import relevant objects

app = Flask(__name__)
storage.setup()   # Det här nollställer databasen inför varje körning

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

@app.route("/", methods=['GET'])
def display_map():
    '''
    At this endpoint we show the full world map via Google maps
    '''
    key = config.MapsAPIKey
    lat = 51.508742
    long = -0.120850

    return render_template("index.tpl", key=key, lat=lat, long=long)


@app.route("/apidocs/", methods=['GET'])
def swagger():
    '''
    shows documentation for the apidocs
    '''
    pass
