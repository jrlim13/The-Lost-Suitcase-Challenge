import requests
import webbrowser
import subprocess
import time

from xml.etree import ElementTree
from math import cos, asin, sqrt, pi
from selenium import webdriver

buses = []

"""Get values from API"""
def parse():
    response = requests.get("http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22")

    root = ElementTree.fromstring(response.content)

    return root

"""Get all buses and their location that are headed North Bound"""
def getAllNorthBound(root):
    print("All Buses Going Northbound: ")

    for bus in root.findall("./bus/[d='North Bound']"):
        bus_id = bus.find('id').text
        bus_lat = bus.find('lat').text
        bus_lon = bus.find('lon').text
        buses.append({
            "id": bus_id,
            "lat": bus_lat,
            "lon": bus_lon
        })
        print(bus_id)
        # print(bus_id, bus_lat, bus_lon)

"""Computes distance between latitude and longitude points"""
def distance(lat1, lon1, lat2, lon2):
    p = pi / 180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))

"""Displays map of near buses"""
def displayMap(bus_id, vic_lat, vic_lon, bus_lat, bus_lon):
    ACCESS_TOKEN="pk.eyJ1Ijoicm9zZWJpdGVzMTMiLCJhIjoiY2s1ejFraDRsMHEwbDNvcjd4Y2x1Z2dvbyJ9.MCAH4_8ZqYM8KEWrRJ1wcA"

    # url = "https://api.mapbox.com/styles/v1/mapbox/streets-v11/static/{},{},14.25,0,0/1280x1280?access_token={}".format(lon, lat, ACCESS_TOKEN)
    url = "https://api.mapbox.com/styles/v1/mapbox/streets-v11/static/pin-l-v+0000cc({},{}),pin-l-b+ff0000({},{})/{},{},14.25,0,0/900x900?access_token={}".format(vic_lon, vic_lat, bus_lon, bus_lat, bus_lon, bus_lat, ACCESS_TOKEN)

    # webbrowser.open(url)

    # p = subprocess.Popen(["firefox", url])
    # return p

    driver = webdriver.Firefox()
    # if driver.service.process != None:
    driver.get(url)
    return driver

if __name__ == "__main__":
    vic_lat = 41.980262
    vic_lon = -87.668452

    # start_time = time.time()

    while True:
        are_buses_near = False
        driver = None

        print(time.asctime(time.localtime(time.time())))

        # All buses going northbound
        getAllNorthBound(parse())

        print("\nDistance of the buses from Victor's Place in KM:")
        for i in range(len(buses)):
            dis_bus = distance(vic_lat, vic_lon, float(buses[i]['lat']), float(buses[i]['lon']))

            if dis_bus < 1:
                are_buses_near = True
                print(str(buses[i]['id']), str(dis_bus), "NEAR")
                driver = displayMap(buses[i]['id'], vic_lat, vic_lon, float(buses[i]['lat']), float(buses[i]['lon']))
            else:
                print(str(buses[i]['id']), str(dis_bus))

        if are_buses_near == False:
            print("\nNo buses near Victor's Place")\

        print("\nWaiting for next update...")

        time.sleep(60.0 - (time.time() % 60.0))

        if driver is not None:
            driver.close()

        buses.clear()
        print("\n" * 100)