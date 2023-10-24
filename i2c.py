import time

import smbus

bus = smbus.SMBus(1)
address = 0x4F

data = bus.read_i2c_block_data(address, 0xAA)

# Daten kommen binaer - [Lowbyte, Highbyte]
MSB = data[0]
LSB = data[1]

print(MSB)
print(LSB)

temp_c = MSB * 10

if MSB & 0x80:
    temp_c = (128 - (MSB & 0x7F)) * (-10)

if LSB == 0x80:
    temp_c = temp_c + 5

print(temp_c)

frac = 100 * (LSB & 0xF0) / 256


print("Temp=" + str(MSB) + "." + str(frac))
