import datetime
import glob
import time as time

import requests
import RPi.GPIO as g
import thingspeak as ts

g.setwarnings(False)
g.setmode(g.BOARD)

channel = ts.Channel(id=268361, write_key="...", api_key="...")


def send_thingspeak(v):
    try:
        print("Sending data to thingspeak...")
        r = channel.update({"field4": v})
        # print(r)
        print("Done")
    except:
        print("Fehler bei thingspeak!")


def solar_lesen():
    print("Solar lesen")


while True:
    solar_lesen()
    time.sleep(60 - datetime.datetime.now().second)
