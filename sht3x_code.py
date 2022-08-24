import time
from machine import I2C, Pin
i2c = I2C(sda = Pin(4), scl = Pin(5))
addr = 0x70
i2c.writeto(addr, b'\x7C\xA2')
time.sleep_ms(15)
sht = i2c.readfrom(addr, 6)
print(sht)
