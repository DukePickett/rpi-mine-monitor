#!/usr/bin/env python

import sys
import time
import datetime
import json
import requests

from envirophat import light, weather, motion, analog, leds

#this is where we'll post some json data
API_ENDPOINT = 'http://bitpartner.io/api/sensors/store-reading'
API_TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
FILE = '/var/www/html/index.lighttpd.html'
unit = 'hPa' # Pressure unit, can be either hPa (hectopascals) or Pa (pascals)

def post(data):
    data['api_token'] = API_TOKEN
    url     = API_ENDPOINT
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    res = requests.post(url, json=data, headers=headers)

def save(data):
    f = open(FILE,"w") 
    f.write(json.dumps(data))
    f.close()

def display(data):
    print(json.dumps(data))

def readdata():
    leds.on()

    rgb = light.rgb()
    analog_values = analog.read_all()
    mag_values = motion.magnetometer()
    acc_values = [round(x,2) for x in motion.accelerometer()]
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    data = {}
    data['altitude'] = weather.altitude()
    data['temperature']  = weather.temperature()
    data['pressure']  = weather.pressure(unit=unit)
    data['lux']  = light.light()
    data['red']  = rgb[0]
    data['green']  = rgb[1]
    data['blue']  = rgb[2]
    data['heading']  = motion.heading()
    data['timestamp'] = timestamp

    leds.off()
    return data

def strobe():
    time.sleep(0.1)
    leds.on()
    time.sleep(0.1)
    leds.off()

#read the data from the sensors
data = readdata()

#show the data at the terminal
display(data)

#save the data to the webserver
save(data)

#post the data to the api endpoint
post(data)

#strobe the led lights on the sensor
strobe()
