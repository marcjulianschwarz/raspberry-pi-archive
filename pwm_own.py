import time as t

import RPi.GPIO as g

g.setmode(g.BCM)
g.setwarnings(False)
g.cleanup()

g.setup(18, g.OUT)
g.setup(23, g.OUT)
g.setup(24, g.OUT)


def reset():
    g.output(18, g.LOW)
    g.output(23, g.LOW)
    g.output(24, g.LOW)


def rot():
    reset()
    g.output(18, g.HIGH)


def blau():
    reset()
    g.pwm(24, 100)


def gruen():
    reset()
    g.output(23, g.HIGH)


reset()


pwm = g.PWM(24, 100)
pwm2 = g.PWM(23, 100)
pwm3 = g.PWM(18, 100)

while True:
    reset()
    pwm.start(100)
    for i in range(1, 100):
        pwm.ChangeDutyCycle(i)
        t.sleep(0.02)
    for i in range(100, -1, -1):
        pwm.ChangeDutyCycle(i)
        t.sleep(0.02)

    reset()
    pwm2.start(100)
    for i in range(1, 100):
        pwm2.ChangeDutyCycle(i)
        t.sleep(0.02)
    for i in range(100, -1, -1):
        pwm2.ChangeDutyCycle(i)
        t.sleep(0.02)

    reset()
    pwm3.start(100)
    for i in range(1, 100):
        pwm3.ChangeDutyCycle(i)
        t.sleep(0.02)
    for i in range(100, -1, -1):
        pwm3.ChangeDutyCycle(i)
        t.sleep(0.02)
    reset()


reset()
g.cleanup()
