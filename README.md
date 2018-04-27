# RPI Mine Monitor

This is a script works in conjunction with the Pimoroni "Enviro pHAT" for the Raspberry Pi zero to read and post enviromental data. The sensors detect temperature, air pressure, movement, luminance, and a general color reading (sort of like a 1 pixel camera).

https://shop.pimoroni.com/products/enviro-phat

In a nutshell, this script will:
    - read the sensors on the Eniro pHAT board
    - write the readings (as json) as file to be read by a local web server
    - post the readings to a URL for remote aggregation, processing, and reporting
    - echo the readings (as json) to the terminal

In order to automate a sensor, this script should be scheduled to run regularly using cron.

Instructions on building a sensor and using this script can be found here:

http://bitpartner.io/rpi-mine-monitor-how-to




