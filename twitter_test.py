import requests
import config
import json

my_headers = {'Authorization' : 'Bearer ' + config.twitterBearerToken}
trend_world = requests.get('https://api.twitter.com/1.1/trends/available.json', headers=my_headers)
trending_now = trend_world.json()

for trend in trending_now:
    
    if(trend['name'] == 'United States'):
        woeid = trend['woeid']

    #print(trend['name'], trend['country'], trend['woeid'])

trend_place = requests.get('https://api.twitter.com/1.1/trends/place.json?id='+ str(woeid) , headers=my_headers)


#list1 = []
#theTweet = []
for trends in trend_place.json():
    
    for t in trends['trends']:
        print(max(t['tweet_volume']))
        '''if(t['tweet_volume'] == 'None' or t['tweet_volume'] is None):
            pass
        else:
            list1.append(t['tweet_volume'])
            theTweet.append(t['name'])
            theTweet.append(t['url'])
            tweetVolume = max(list1)
            if(max(list1) == t):
                print(theTweet)'''


#print("Largest element is:", t[max(list1)])       

#print(list1)
#plocka ut name, url, välja ut det som har mest tweet volume.

trend_swe = trend_place.json()



'''for trend in trend_swe:
    print(trend['trends'][0]['name'], trend['trends'][0]['url'], trend['trends'][0]['tweet_volume'])'''






