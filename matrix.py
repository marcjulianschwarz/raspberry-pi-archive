import time as t
from random import randint

import max7219.led as led

matrix = led.matrix(cascaded=2)
matrix.brightness(1)
