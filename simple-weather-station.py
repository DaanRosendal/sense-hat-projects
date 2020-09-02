#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
from sense_hat import SenseHat
import time
import sys

sense = SenseHat()
sense.clear()
sense.set_rotation(90)

try:
      while True:
           temp = sense.get_temperature()
           cpu_temp = 16
           temp = int(temp) - cpu_temp
           print("Temperature:", str(temp) + "°C")

           humidity = sense.get_humidity()
           humidity = int(humidity)
           print("Humidity:", str(humidity) + "%")

           pressure = sense.get_pressure()
           pressure = int(pressure)
           print("Atmospheric pressure:", pressure, "millibar (hPa)")

           sense.show_message(str(temp))
except KeyboardInterrupt:
      pass 
