from flask import Flask
from ApiFiles.BeerApi import beer_api
from ApiFiles.SearchApi import search_api
from ApiFiles.PanierApi import panier_api

app=Flask(__name__)

app.register_blueprint(beer_api)
app.register_blueprint(search_api)
app.register_blueprint(panier_api)

if __name__ =='__main__' :
    app.run()