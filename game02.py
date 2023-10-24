import json
import random
import time as t

import RPi.GPIO as g
import thingspeak as ts

channel_id = 268361
write_key = "..."
read_key = "..."
channel = ts.Channel(id=channel_id, write_key=write_key, api_key=read_key)

g.setmode(g.BCM)
g.setwarnings(False)


g.setup(17, g.OUT)
g.setup(27, g.OUT)
g.setup(10, g.IN)
g.setup(22, g.OUT)

g.output(17, g.LOW)
g.output(22, g.LOW)
g.output(27, g.LOW)


def send_data(v, anzahl):
    print("Sending data...")
    read = channel.get({})
    ch = json.loads(read)
    last_entry_id = ch["channel"]["last_entry_id"]

    v2 = 0
    try:
        feeds = ch["feeds"]
        feed = feeds[last_entry_id - 1]
        v2 = int(feed["field3"])
    except:
        print("no score")

    if int(v) == 2:
        v2 = v2 + 1
    else:
        v2 = v2 - 1

    channel.update({"field1": v, "field2": anzahl, "field3": v2})
    print("Sending is done.")


def play(gx):
    print("Game started.")
    game = []
    x = random.randint(2, 10)

    while len(game) < x:
        game.append(random.randint(0, 1))

    play_lights(game)
    print(game)
    userInput = []
    d = 0
    while d < len(game):
        userInput.append(test())
        d = d + 1

    if game == userInput:
        print("won")
        audio_won()
        # x = x + 1

        print(x)
        try:
            send_data(2, len(game))
        except:
            print("no internet")

        print("Sending done")
    else:
        print("lost")
        audio_lost()
        # x = x -1

        print(x)
        try:
            send_data(1, len(game))
        except:
            print("no internet")

        print("Sending done")

    gx = gx - 1

    if gx > 0:
        t.sleep(1.5)
        play(gx)


def play_lights(g2):
    c = 0
    light_off()
    while c < len(g2):
        if g2[c] == 1:
            light_red_on()
            t.sleep(0.5)
        else:
            light_blue_on()
            t.sleep(0.5)
        c = c + 1

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


def audio(f1):
    g.output(22, g.HIGH)
    t.sleep(f1)
    g.output(22, g.LOW)


def audio_won():
    for i in range(1, 6):
        audio(i * 0.1)
        t.sleep(i * 0.1)


def audio_lost():
    audio(2)


# Funktion play wird gestartet


play(10)


g.cleanup()
