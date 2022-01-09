# Tmap
## Trend map or Twitter map or TwitterTrends map
an api that shows the most trending word int a country from twitter on a world map
and translates relative tweets into English

University project for Malmö University HT2021

In this project you'll need an file called "config.py" that contain all the API keys that you'll need. If you don't have those the application will not work!
The keys that you will need are:
* Twitter API key(Bearer Token),
* Google Maps API key(containg access to Geocoding API, Maps JavaScript)
* Google Cloud Translation key. 

**Instructions**

Make sure that ​​python --version returns version 3.8.0 or higher
Activate the virtual env with . myenv/bin/activate
Install the right version of Flask with pip install -r requirements.txt

# Windows
Start Flask with FLASK_APP=src/app.py , if you use PowerShell run $env:FLASK_APP = "src/app.py"

# Mac/Linux
Activate the virtual env with . myenv/bin/activate

Start Flask with FLASK_APP=app.py

# All OS
Start Flask with flask run

Open the address from the console outsput and explore T-map!
