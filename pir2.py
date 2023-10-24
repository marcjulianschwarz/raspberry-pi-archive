import time as t

import RPi.GPIO as g

g.setmode(g.BCM)
g.setwarnings(False)
GPIO_PIR = 7
print("Pir Test")
g.setup(GPIO_PIR, g.IN)
g.setup(17, g.OUT)
g.setup(22, g.OUT)

g.output(22, g.LOW)
g.output(17, g.LOW)
Current_State = 0
Previous_State = 0

try:
    # 	print("Waiting")
    # 	while g.input(GPIO_PIR) == 1:
    # 		Current_State = 0
    # 	print("Ready")

    while True:
        Current_State = g.input(GPIO_PIR)

        print(Current_State)

        if Current_State == 1 and Previous_State == 0:
            # g.output(17, g.HIGH)
            # t.sleep(1)
            # g.output(17, g.LOW)
            print("Motion")

            Previous_State = 1
        elif Current_State == 0 and Previous_State == 1:
            Previous_State = 0
            # t.sleep(4.5)
            # g.output(22, g.HIGH)
            # t.sleep(.1)
            # g.output(22, g.LOW)
            print("REady")
        t.sleep(0.01)

except KeyboardInterrupt:
    print("Quit")
    g.cleanup()
