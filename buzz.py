import time as t

import RPi.GPIO as G

G.setmode(G.BCM)

G.setwarnings(False)

G.setup(17, G.OUT)
G.setup(27, G.OUT)
G.setup(10, G.IN)
G.setup(22, G.OUT)


G.output(17, G.LOW)
G.output(27, G.LOW)
x = 0

while True:
    if G.input(10) == 0:
        G.output(22, G.HIGH)
        t.sleep(0.2)
        G.output(22, G.LOW)
        t.sleep(0.2)
        G.output(22, G.HIGH)
        t.sleep(0.2)
        G.output(22, G.LOW)
        t.sleep(0.2)
        G.output(22, G.HIGH)
        t.sleep(0.2)
        G.output(22, G.LOW)


G.cleanup()
