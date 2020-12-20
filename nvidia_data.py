import serial
import syslog
import time
from jtop import jtop
import json
import datetime
import os
import threading
import re

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

def openjtop():
    with jtop() as jetson:
      while jetson.ok():
         return jetson.stats

def closejtop():
   jetson = jtop()
   jetson.close()
   return 'ok'

def changedict(data):
    del data['uptime']
    data['Temp_GPU']=data.pop("Temp GPU")
    data['Temp_CPU']=data.pop("Temp CPU")
    data['power_avg']=data.pop("power avg")
    data['power_cur']=data.pop("power cur")
    data['nvp_model']=data.pop("nvp model")
    data['Temp_thermal']=data.pop("Temp thermal")
    data['Temp_PLL']=data.pop("Temp PLL")
    data['Temp_AO']=data.pop("Temp AO")
    return data

def send_json():
  while True:
   # if ard.isOpen():
      data=openjtop() #get jtop stats
      closejtop()
      data=changedict(data) #change dict
      d1 = dict(data.items()[len(data)/2:])
      d2 = dict(data.items()[:len(data)/2])
      d1 = json.dumps(d1,default=myconverter)
      d2 = json.dumps(d2,default=myconverter)
      d1="["+d1+"]"
      d2="["+d2+"]"

      print(d1,d2)

send_json()
"""
      ard.write(d1.encode('ascii'))
      ard.flush()
      time.sleep(2)
      ard.write(d2.encode('ascii'))
      ard.flush()
      time.sleep(5)
"""
