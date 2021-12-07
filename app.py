# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request, url_for, render_template
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
    map = storage.display_map()

    if request.headers.get("Accept") == "application/json":
        # Om JSON efterfrågas, skicka tillbaka det. jsonify() hanterar även vår
        # Content-Type-header. Se vidare dokumentation på
        # https://flask.palletsprojects.com/en/2.0.x/api/#module-flask.json
        return jsonify(map)
    else:
        # Annars får vi skicka tillbaka HTML. url_for() berättar var vår
        # style.css ligger någonstans. Se vidare dokumentation på
        # https://flask.palletsprojects.com/en/2.0.x/api/#flask.url_for
        url_for("static", filename="static/style.css")

        # Till render_template() skickar vi namnet på den mall vi vill använda
        # för att rendera en webbsida. Vi skickar också med våra enhörningar.
        # Dessa benämns "unicorns" även i mallen. Alla mallar ligger i
        # katalogen src/templates. Se vidare dokumentation på
        # https://flask.palletsprojects.com/en/2.0.x/api/#flask.render_template
        return render_template("index.tpl", map=map)
