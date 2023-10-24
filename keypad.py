import RPi.GPIO as g
import time as t
import math as m

g.setmode(g.BCM)
g.setwarnings(False)
spalte = [12, 16, 20, 21]
zeile = [18, 23, 24, 25]


pad = [[1.0, 2.0, 3.0, "+"],[4.0, 5.0, 6.0, "-"],[7.0, 8.0, 9.0, "*"],["*", 0.0, "=", "/",]]


def ad(zahl1, zahl2):
	return zahl1 + zahl2
def sub(zahl1, zahl2):
	return zahl1 - zahl2
def mult(zahl1, zahl2):
	return zahl1 * zahl2
def div(zahl1, zahl2):
	return zahl1 / zahl2



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

t = 1
y = 1
x = 1

n = 0
r = 0
while y == 1:
	while x == 1:
		n = keypad()
		if n == "-" or n == "+" or n == "*" or n == "/":
			r = n
			print(r)
			x = x+1
		else:	 
			a = a*10+n
			print(a)
	while t == 1:
		n = keypad()
		if n == "=":
                        t = t+1
                else:
                        b = b*10+n
                        print(b)
	
	if r == "-":
		print(a-b)
		y = y+1
	elif r == "+":
		print(a+b)
		y = y+1
		elif r == "*":
				print(a*b)
				y = y+1
		elif r == "/":
				print(a/b)
				y = y+1
	else:
		print("Diesen Rechenoperator gibt es nicht.")

		
