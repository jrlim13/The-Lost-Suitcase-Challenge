import requests
import xmltodict, json

from math import pi, cos, asin, sqrt

"""Get values from API and Convert to JSON"""
def parse():
    north_buses = []

    response = requests.get('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
    buses = json.loads(json.dumps(xmltodict.parse(response.content)))

    # Get all going North Bound
    for bus in buses['buses']['bus']:
        if bus['d'] == 'North Bound' and distance(float(bus['lat']), float(bus['lon'])) < 1:
            north_buses.append({
                'id': bus['id'],
                'lat': bus['lat'],
                'lon': bus['lon']
            })
        print('distance: ', distance(float(bus['lat']), float(bus['lon'])), ' ', bus['id'])

    # # Display if no buses going North Bound
    # if len(north_buses) < 1:
    #     print("No Buses going Northbound")

    return north_buses

"""Computes distance between latitude and longitude points"""
def distance(lat1, lon1, lat2=41.980262, lon2=-87.668452):
    p = pi / 180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))