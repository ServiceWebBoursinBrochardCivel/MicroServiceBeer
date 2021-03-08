from flask import Flask
from flask_cors import CORS
from Api.BeerApi import beer_api
from Api.SearchApi import search_api
from Api.PanierApi import panier_api

app=Flask(__name__)
CORS(app)

app.register_blueprint(beer_api)
app.register_blueprint(search_api)
app.register_blueprint(panier_api)

if __name__ =='__main__' :
    app.run()