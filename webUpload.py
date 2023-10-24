import time as t

import max7219.led as led
import requests
from max7219.font import CP437_FONT, LCD_FONT, SINCLAIR_FONT, TINY_FONT

matrix = led.matrix(cascaded=2)

font = SINCLAIR_FONT

while True:
    try:
        r = requests.get("http://www.marc-julian.de/api/data.aspx")
        data = r.text
        # FONT
        if data[0] == "1":
            font = LCD_FONT
        elif data[0] == "2":
            font = TINY_FONT

        # SHOW
        matrix.show_message(data[1:], font)
        print(data[1:])
    except:
        print("No internet or other error")
        matrix.show_message("ERROR")

    t.sleep(1)
