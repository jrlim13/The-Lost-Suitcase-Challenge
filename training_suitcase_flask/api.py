from flask import Flask, jsonify
from flask_restful import Resource, Api

from parse import parse

app = Flask(__name__)
api = Api(app)

class NorthBusList(Resource):
    def get(self):
        north_buses = parse()
        return jsonify({'northbuses': north_buses})

api.add_resource(NorthBusList, '/northbuses')

if __name__ == '__main__':
    app.run(debug=True, port=8000)