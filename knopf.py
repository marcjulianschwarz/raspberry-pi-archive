import time as t

import RPi.GPIO as G

G.setmode(G.BCM)

G.setwarnings(False)


G.setup(17, G.OUT)
G.setup(27, G.OUT)
G.setup(10, G.IN)
G.output(17, G.LOW)
G.output(27, G.LOW)


while True:
    if G.input(10) == 0:
        G.output(17, G.HIGH)
        G.output(27, G.LOW)

    else:
        G.output(27, G.HIGH)
        G.output(17, G.LOW)

G.cleanup()
