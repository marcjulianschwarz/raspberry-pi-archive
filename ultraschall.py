import RPi.GPIO as g
import time as t
g.setmode(g.BCM)

trig = 3
echo = 4
rot = 26
green1 = 19 
green2 = 13
green3 = 6


print("Es wird gemessen....")

g.setup(trig, g.OUT)
g.setup(echo, g.IN)

g.setup(rot, g.OUT)
g.setup(green1, g.OUT)
g.setup(green2, g.OUT)
g.setup(green3, g.OUT)

g.output(rot,False)
g.output(green1, False)
g.output(green2, False)
g.output(green3, False)

g.setwarnings(False)


def messen():
	g.output(trig, False)
	t.sleep(0.1)
	
	g.output(trig, True)
	t.sleep(0.00001)
	g.output(trig, False)
	
	while g.input(echo) == 0:
		start = t.time()
	
	while g.input(echo) ==1:
		stop = t.time()
	
	try:
		deltaZeit = stop - start
	except:
		deltaZeit = 0.1
	entfernung = round(deltaZeit*34000/2, 2)
	
	if entfernung > 1:
		print(entfernung)
				
		if entfernung < 5:
			g.output(rot, False)
                        g.output(green1, False)
                        g.output(green2, False)
                        g.output(green3, False)		

		elif entfernung < 10 and entfernung > 5:
			g.output(rot, True)
			g.output(green1, False)
			g.output(green2, False)
			g.output(green3, False)
		elif entfernung > 10 and entfernung < 15:
			g.output(rot, True)
			g.output(green1, True)
			g.output(green2, False)
			g.output(green3, False)	
		elif entfernung > 15 and entfernung < 20:
			g.output(rot, True)
                        g.output(green1, True)
                        g.output(green2, True)
                        g.output(green3, False)
		elif entfernung > 20 and entfernung < 25:
			g.output(rot, True)
                        g.output(green1, True)
                        g.output(green2, True)
                        g.output(green3, True)

while True:
	messen()
