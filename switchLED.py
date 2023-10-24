import time as t

import RPi.GPIO as g

g.setwarnings(False)
g.setmode(g.BCM)
g.setup(18, g.OUT)
g.output(18, g.HIGH)


x = 0

while True:
    file = open("switch.txt", "r")
    x = file.read()
    file.close()
    if x == "true":
        g.output(18, g.HIGH)
    else:
        g.output(18, g.LOW)
