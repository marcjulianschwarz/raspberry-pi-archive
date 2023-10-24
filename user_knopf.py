import time as t

import RPi.GPIO as G

G.setmode(G.BCM)

G.setwarnings(False)

G.setup(17, G.OUT)
G.setup(27, G.OUT)
G.setup(10, G.IN)


G.output(17, G.LOW)
G.output(27, G.LOW)
x = 0
y = 0


print("2s: 2")
print("30s: 30 ")
print("usw...  ")
user2 = input("Wie lange soll das LED an sein? ")
print(" ")
print(" ")

print("Rot: 1 ")
print("Blau: 2 ")
user = input("Welche Farbe soll das LED haben? ")

print(" ")
print(" ")

print("Zum Ausfuehren den Knopf druecken.")

while y < 1:
    if G.input(10) == 0:
        y = y + 1

        while x < 1:
            if user == 1:
                G.output(27, G.HIGH)
                x = x + 1
            else:
                if user == 2:
                    G.output(17, G.HIGH)
                    x = x + 1
                else:
                    print("Dieses LED gibt es nicht.")
                    G.output(27, G.LOW)
                    G.output(17, G.LOW)
                    x = x + 1


t.sleep(user2)
print(" ")
print(" ")
print(" ")
print("Das LED wurde nach deinem Wunsch eingeschaltet.")
G.cleanup()
