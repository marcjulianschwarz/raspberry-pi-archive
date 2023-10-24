import RPi.GPIO as g
import time as t
import math as m

g.setmode(g.BCM)
g.setwarnings(False)
spalte = [12, 16, 20, 21]
zeile = [18, 23, 24, 25]


pad = [[1.0, 2.0, 3.0, "+"],[4.0, 5.0, 6.0, "-"],[7.0, 8.0, 9.0, "*"],["*", 0.0, "=", "/",]]

for x in range (4):
	g.setup(spalte[x], g.OUT)
	g.output(spalte[x], 1)
	g.setup(zeile[x], g.IN, pull_up_down = g.PUD_UP)

def keypad():
	while True:
		for x in range(4):
			g.output(spalte[x], 0)
			for i in range(4):
				if g.input(zeile[i]) == 0:
					#print(str(x) + " " + str(i))
					eingabe = pad[i][x]
					#print(eingabe)
					while g.input(zeile[i])==0:
						pass
					return eingabe
			g.output(spalte[x], 1)
	return False

a = 0
b = 0
n = 0
r = "0"


while True:

	n = keypad()

	if n == "-" or n == "+" or n == "*" or n == "/":

		if r == "+":
			b = b + a
			print("Ergebnis=" + str(b))
		elif r == "-":
			b = b - a
			print("Ergebnis=" + str(b))
		elif r == "*":
			b = b * a
			print("Ergebnis=" + str(b))
		elif r == "/":
			b = b / a
			print("Ergebnis=" + str(b))
		else:
			b = a
		r = n
		a = 0
	else:
		a = a*10 + n


        print("b=" + str(b) + "\t" + r + "\ta=" + str(a))












		
