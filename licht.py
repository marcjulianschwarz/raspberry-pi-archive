import time as t

import RPi.GPIO as g
import thingspeak as ts

g.setwarnings(False)

g.setmode(g.BOARD)
g.setup(13, g.OUT)


g.output(13, g.LOW)
pin_to_circuit = 12

channel = ts.Channel(id=268361, write_key="...", api_key="...")


def sending_data():
    try:
        print("Sending data...")
        r = channel.update({"field5": licht})
        print("Done")
    except:
        print("sending fail")


def rc_time(pin_to_circuit):
    count = 0

    g.setup(pin_to_circuit, g.OUT)
    g.output(pin_to_circuit, g.LOW)
    t.sleep(0.1)

    g.setup(pin_to_circuit, g.IN)

    while g.input(pin_to_circuit) == g.LOW:
        count += 1

    return count


try:
    while True:
        licht = rc_time(pin_to_circuit)
        # 		print("Sending...")
        # 		sending_data()
        # 		print("Done")

        if licht < 7000:
            g.output(13, g.LOW)
        else:
            g.output(13, g.HIGH)

        print(licht)

except KeyboardInterrupt:
    pass
finally:
    g.cleanup()
