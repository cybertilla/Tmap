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

# Instructions

## Windows
1. Make sure that ​​python --version returns version 3.8.0 or higher
2. Activate the virtual env with . myenv/Scripts/activate 
If you get an error type: python -m venv myenv and start over with instruction no 2. 
3. Make sure that you are in the right folder(the one closest to the code) and install the right version of Flask and requests with pip install -r requirements.txt
4. Start Flask with set FLASK_APP=src/app.py , if you use PowerShell run $env:FLASK_APP = "src/app.py"

## Mac/Linux
1. Make sure that ​​python --version returns version 3.8.0 or higher
2. Create an virtual enviroment with python3 -m venv myenv
3. Activate the virtual env with . myenv/bin/activate 
4. Make sure that you are in the right folder(the one closest to the code) and install the right version of Flask and requests with pip install -r requirements.txt
5. Start Flask with export FLASK_APP=app.py , if you get an error you may have to add Tmap-main folder to you path. If so do this command export PATH=”$(pwd):$PATH”

## All OS
Start Flask with flask run

Open the address from the console output and explore T-map!
