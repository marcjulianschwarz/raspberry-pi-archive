import time as t

import RPi.GPIO as G

G.setmode(G.BCM)
G.setwarnings(False)
G.setup(10, G.IN, pull_up_down=G.PUD_DOWN)
G.setup(27, G.OUT)


def myFuncDown(channel):
    v = G.input(channel)

    if v == G.HIGH:
        return

    G.output(27, G.HIGH)
    t.sleep(5)
    G.output(27, G.LOW)


G.add_event_detect(10, G.BOTH, callback=myFuncDown)

while True:
    t.sleep(0.1)


G.cleanup()
