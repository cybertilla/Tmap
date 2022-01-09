# Tmap
## Trend map or Twitter map or TwitterTrends map
an api that shows the most trending word int a country from twitter on a world map
and translates relative tweets into English

University project for Malmö University HT2021

In this project you'll need an file called "config.py" that contain all the API keys that you'll need. If you don't have those the application will not work!
The keys that you will need are a Twitter API key(Bearer Token), Google Maps API key(containg access to Geocoding API, Maps JavaScript) and Google Cloud Translation key. 

Instructioner
Windows
Säkerställa att ​​python --version returnerar en version över 3.8.0
Aktivera den virtuella utvecklingsmiljö med . myenv/bin/activate OBS: Skulle du få felmeddelande i detta steget gör python -m venv myenv och sedan börja om på steget.
Installera den rätta version av ramverket Flask med pip install -r requirements.txt
Sätt igång Flask med set FLASK_APP=src/app.py eller om det görs i PowerShell $env:FLASK_APP = "src/app.py"
Kör servern genom att skriva flask run
Öppna webbadressen som returneras i konsolen, nu kan du explorera T-map.
Mac/Linux
Säkerställa att ​​python --version returnerar en version över 3.8.0
Installera den rätta version av ramverket Flask med pip install -r requirements.txt
Aktivera den virtuella utvecklingsmiljö med . myenv/bin/activate
Sätt igång Flask med export FLASK_APP=app.py
Kör servern genom att skriva flask run
Öppna webbadressen som returneras i konsolen, nu kan du explorera T-map.
