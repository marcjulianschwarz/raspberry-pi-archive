import random
import time as t

import RPi.GPIO as g

g.setmode(g.BCM)
g.setwarnings(False)


g.setup(17, g.OUT)
g.setup(27, g.OUT)
g.setup(10, g.IN)
g.setup(22, g.OUT)

g.output(17, g.LOW)
g.output(22, g.LOW)
g.output(27, g.LOW)


game = []
x = random.randint(2, 4)

while len(game) < x:
    game.append(random.randint(0, 1))


def play_lights(g2):
    c = 0
    light_off()
    while c < len(g2):
        if g2[c] == 1:
            light_red_on()
        else:
            light_blue_on()
        c = c + 1
        t.sleep(0.4)
        light_off()
        t.sleep(0.2)


def light_red_on():
    g.output(27, g.HIGH)
    g.output(17, g.LOW)


def light_blue_on():
    g.output(27, g.LOW)
    g.output(17, g.HIGH)


def light_off():
    g.output(27, g.LOW)
    g.output(17, g.LOW)


play_lights(game)


def test():
    y = 0
    z = 0
    user = -1
    while y < 1:
        while g.input(10) == 0:
            z = z + 0.1
            t.sleep(0.1)

            if z <= 0.5:
                user = 0
                # print(z)
                y = y + 1
            else:
                if z > 0.5:
                    user = 1
                    # print(z)
                    y = y + 1
    return user


userInput = []

d = 0

while d < len(game):
    userInput.append(test())
    d = d + 1


def play(f1):
    g.output(22, g.HIGH)
    t.sleep(f1)
    g.output(22, g.LOW)


if game == userInput:
    print("won")

    for i in range(1, 6):
        play(i * 0.1)
        t.sleep(i * 0.1)

else:
    print("loose")
    play(2)


g.cleanup()
