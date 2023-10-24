import time as t

import RPi.GPIO as g

g.setmode(g.BCM)
g.setwarnings(False)
g.setup(17, g.OUT)
g.setup(27, g.OUT)


g.output(17, g.LOW)


g.output(27, g.LOW)

g.output(17, g.HIGH)
g.output(27, g.HIGH)
t.sleep(20)


g.cleanup()
