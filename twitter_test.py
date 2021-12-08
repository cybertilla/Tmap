import requests

my_headers = {'Authorization' : 'Bearer {INSERT HERE}'}
trend_place = requests.get('https://api.twitter.com/1.1/trends/place.json?id=23424954', headers=my_headers)
trend_swe = trend_place.json()

'''for trend in trend_swe:
    print(trend['trends'][0]['name'], trend['trends'][0]['url'], trend['trends'][0]['tweet_volume'])
'''

trend_world = requests.get('https://api.twitter.com/1.1/trends/available.json', headers=my_headers)
trending_now = trend_world.json()

for trend in trending_now:
    print(trend['name'], trend['country'], trend['woeid'])