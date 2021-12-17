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
    print("från display_country: " + name)
    
    twitterApi.getCountry(name)
    '''
    Centers map on specifi town, calls Twitter API for hashtag data
    Returns JSON object??
    '''
    pass

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
