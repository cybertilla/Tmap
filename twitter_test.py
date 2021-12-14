import requests
import config
import json

my_headers = {'Authorization' : 'Bearer ' + config.twitterBearerToken}
trend_world = requests.get('https://api.twitter.com/1.1/trends/available.json', headers=my_headers)
trending_now = trend_world.json()

for trend in trending_now:
    
    if(trend['name'] == 'United States'): # we switch this to a paramiter från the user input
        woeid = trend['woeid']

    #print(trend['name'], trend['country'], trend['woeid'])

trend_place = requests.get('https://api.twitter.com/1.1/trends/place.json?id='+ str(woeid) , headers=my_headers)


list1 = []
maxNum = 0
for trends in trend_place.json():
    #print(trends)
    for t in trends['trends']:
       
        if(t['tweet_volume'] == 'None' or t['tweet_volume'] is None):
                pass
            
        elif(t['tweet_volume'] > maxNum):
                list1.clear()
                maxNum = t['tweet_volume']
                #print("max num: ", maxNum)
                
                list1.append(t['tweet_volume'])
                list1.append(t['name'])
                list1.append(t['url'])
                #print(t['tweet_volume'])
                #print("in if: ", t['tweet_volume'])
      
#plocka ut name, url, välja ut det som har mest tweet volume.

trend_swe = trend_place.json()
#print(list1)


'''for trend in trend_swe:
    print(trend['trends'][0]['name'], trend['trends'][0]['url'], trend['trends'][0]['tweet_volume'])'''

resource_url = requests.get('https://api.twitter.com/1.1/search/tweets.json?q=' + list1[1] + '&result_type=popular', headers =my_headers)
resource_url = resource_url.json()

#print(resource_url)



def getTextToTranslate():

    likes = 0
    list2 = []
    text = " "
    for res in resource_url['statuses']:
        
        for r in res['text']:

            if(res['favorite_count'] > likes):

                list2.clear()
                likes = res['favorite_count']
                #print("innan: ", likes)
                text = res['text']
                list2.append(res['text'])
                list2.append(res['favorite_count'])
                
    return text            
                
    #print(list2)


