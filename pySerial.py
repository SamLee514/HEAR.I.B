#!/usr/bin/env python3

import serial

arduino = serial.Serial('/dev/ttyACM0', 9600) #timeout parameter omitted

while True:
  data = arduino.readline()[:-2]
  if data:
    print (data)
