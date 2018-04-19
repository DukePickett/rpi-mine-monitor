#!/usr/bin/env python

import sys
import time
import datetime
import json
import requests

from envirophat import light, weather, motion, analog, leds


API_ENDPOINT = 'http://192.168.0.71:8080/api/sensors/store-reading'
API_TOKEN = '30d6a4a0-41ed-11e8-bce4-f81a67180469'
unit = 'hPa' # Pressure unit, can be either hPa (hectopascals) or Pa (pascals)
sleep_time = 60*2; # 2 minutes

data = {}
data['api_token'] = API_TOKEN

def write(data):
    url     = API_ENDPOINT
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    res = requests.post(url, json=data, headers=headers)
    sys.stdout.write('.')
    sys.stdout.flush()

print('\nStarting EnviroPhat monitoring with BitPartner.io\n================================================\n')

try:
    while True:
	leds.on()
        rgb = light.rgb()
        analog_values = analog.read_all()
        mag_values = motion.magnetometer()
        acc_values = [round(x,2) for x in motion.accelerometer()]
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

        data['altitude'] = weather.altitude()
        data['temperature']  = weather.temperature()
        data['pressure']  = weather.pressure(unit=unit)
        data['lux']  = light.light()
        data['red']  = rgb[0]
        data['green']  = rgb[1]
        data['blue']  = rgb[2]
        data['heading']  = motion.heading()
        data['timestamp'] = timestamp

        write(data);
	leds.off()
	time.sleep(0.1);
	leds.on()
	time.sleep(0.1);
	leds.off()
        time.sleep(sleep_time)

except KeyboardInterrupt:
    pass

