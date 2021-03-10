from flask import Flask,jsonify,send_from_directory
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from Api.BeerApi import beer_api
from Api.SearchApi import search_api
from Api.PanierApi import panier_api


app=Flask(__name__)
CORS(app)

app.register_blueprint(beer_api)
app.register_blueprint(search_api)
app.register_blueprint(panier_api)

@app.route('/Api/<path:path>')
def send_api(path) :
    return send_from_directory('Api',path)


SWAGGER_URL = '/spec'
API_URL = '/Api/swagger.json'
swaggerui_api = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name' : "BeersApi"
    }
)
app.register_blueprint(swaggerui_api,url_prefix=SWAGGER_URL)


if __name__ =='__main__' :
    app.run()

