import datetime
import glob
import time

import max7219.led as led
import requests
import thingspeak as ts

matrix = led.matrix(cascaded=2)

channel = ts.Channel(id=268361, write_key="...", api_key="...")

pfad = "/sys/bus/w1/devices/"
sensor_ordner = glob.glob(pfad + "28*")[0]
sensor_daten_pfad = sensor_ordner + "/w1_slave"


def send_papa(v):
    try:
        print("Temperatur " + "{0:g}".format(v * 1000) + " wird an Papa geschickt...")
        now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        print(now)
        r = requests.post(
            ".../....aspx",
            "DeviceID=3&Temperatur=" + "{0:g}".format(v * 1000) + "&MeasureDate=" + now,
        )
        if r.status_code == 200:
            print("Done, ok")
        else:
            print("Done, but failed")
    except:
        print("Fehler bei Papa")


def send_thingspeak(v):
    try:
        print("Sending data to thingspeak...")
        r = channel.update({"field4": v})
        print("Done")
    except:
        print("Fehler bei thingspeak")


def temperatur_lesen():
    datei = open(sensor_daten_pfad, "r")
    zeilen = datei.readlines()
    datei.close()
    return zeilen


def grad_lesen():
    zeilen = temperatur_lesen()
    while zeilen[0].strip()[-3:] != "YES":
        time.sleep(0.2)
        zeilen = temperatur_lesen()
    equal_pos = zeilen[1].find("t=")
    if equal_pos != -1:
        temp_string = zeilen[1][equal_pos + 2 :]
        temp_c = float(temp_string) / 1000.0
        return temp_c


while True:
    fin = grad_lesen()
    file = open("testfile.txt", "w")
    file.truncate()
    file.write(str(fin))
    file.close()
    time.sleep(1)
    print(fin)

    # send_papa(t)
    # send_thingspeak(t)
    # time.sleep(60 - datetime.datetime.now().second)
