# Suitcase-Problem
Bootcamp (Novare) - Training 2
Jerry went to chicago then rode a bus at route 22 to see his long time friend Victor. At the stop over, he went off the bus to buy some ice cream without noticing that the bus has already left. After a while he realized that he’d left the suitcase on the bus! Jerry needs to get it back but he needs your support. Your task is to help Jerry get it back.

1.) Jerry has no idea what’s the number of the bus he was riding at that time. Find all possible candidates by parsing the data from this API:

http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route={route number}

We need all buses going northbound. Victor’s location is at 41.980262 latitude and -87.668452 longitude.


2.) Create a program/script which monitors the identified buses and reports their current distance from Victor’s office. When the bus gets closer than 1 kilometer, the program must issue an alert by popping up a web-page showing the bus location on a map so that Jerry could meet them and get the suitcase back.

## Script Version
1. Run the script normally

## Flask Verision
1. Run the web API first
2. Type `export FLASK_APP=training_suitcase_flask.py FLASK_ENV=development`
3. Type `flask run` in terminal
