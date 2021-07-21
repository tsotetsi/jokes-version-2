from flask import Flask
from flask import jsonify

import requests



app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_chuck_norris_jokes():

    api_url = "https://api.chucknorris.io/jokes/random"

    response = requests.get(api_url).json()

    return response


@app.route("/categories", methods=["GET"])
def get_jokes_categories():

    api_url = "https://api.chucknorris.io/jokes/categories"
    response = requests.get(api_url).json()

    return jsonify(response)