import requests
import xmltodict, json

from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {
        'user': 'Victor',
        'lat': 41.980262,
        'lon': -87.668452,
    }
    response = requests.get('http://127.0.0.1:8000/northbuses')
    north_buses = response.json()

    return render_template('index.html', user=user, north_buses=north_buses['northbuses'])