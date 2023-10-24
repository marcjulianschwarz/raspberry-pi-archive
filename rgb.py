import RPi.GPIO as g
import time as t

g.setmode(g.BCM)
g.setwarnings(False)
g.setup(18, g.OUT)
g.setup(23, g.OUT)
g.setup(24, g.OUT)



def reset():
	g.output(23, g.LOW)
	g.output(24, g.LOW)
	g.output(18, g.LOW)

def blau():
	print "blau"
	g.output(24, g.HIGH)
def gruen():
	print "gruen"
	g.output(23, g.HIGH)
def rot():
	print "rot"
	g.output(18, g.HIGH)


reset()


for i in range(0,8):

	print str(i) + "\t" + str(i & 4 == 4) + "\t" + str(i & 2 == 2) + "\t" + str(i & 1 == 1)

	reset()

	if(i & 4 == 4):
		rot()
	if(i & 2 == 2):
		gruen()
	if(i & 1 == 1):
		blau()

	t.sleep(2)

g.cleanup()
