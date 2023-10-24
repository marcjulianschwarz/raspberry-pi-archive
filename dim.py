import time as t

import RPi.GPIO as g

g.setmode(g.BCM)
g.setwarnings(False)
g.setup(17, g.OUT)

led = g.PWM(17, 100)

led.start(0)

pause_time = 0.02

while True:
    for i in range(0, 101):
        led.ChangeDutyCycle(i)
        t.sleep(pause_time)
    for i in range(100, -1, -1):
        led.ChangeDutyCycle(i)
        t.sleep(pause_time)


g.cleanup()
