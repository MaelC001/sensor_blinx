from machine import Pin, I2C
import time
import ustruct

DATA_FORMAT = 0x31
BW_RATE  = 0x2c
POWER_CTL = 0x2d
INT_ENABLE  = 0x2E
OFSX = 0x1e
OFSY = 0x1f
OFSZ = 0x20
addr = 0xe5

def read_xyz(self):
    fmt = ' < h' #little-endian
    buf1 = self.readByte(0x32)
    buf2 = self.readByte(0x33)
    buf = bytearray([buf1[0], buf2[0]])
    x, = ustruct.unpack(fmt, buf)
    x = x*3.9
    #print('x:', x)

    buf1 = self.readByte(0x34)
    buf2 = self.readByte(0x35)
    buf = bytearray([buf1[0], buf2[0]])
    y, = ustruct.unpack(fmt, buf)
    y = y*3.9
    #print('y:', y)

    buf1 = self.readByte(0x36)
    buf2 = self.readByte(0x37)
    buf = bytearray([buf1[0], buf2[0]])
    z, = ustruct.unpack(fmt, buf)
    z = z*3.9
    #print('z:', z)
    #print('************************')
    #time.sleep(0.5)
    return (x, y, z)

def write_byte(self, addr, data):
    d = bytearray([data])
    self.i2c.writeto_mem(self.slvAddr, addr, d)
def read_byte(self, addr):
    return self.i2c.readfrom_mem(self.slvAddr, addr, 1)



writeByte(DATA_FORMAT, 0x2B)
writeByte(BW_RATE, 0x0A)
writeByte(INT_ENABLE, 0x00)
writeByte(OFSX, 0x00)
writeByte(OFSY, 0x00)
writeByte(OFSZ, 0x00)
writeByte(POWER_CTL, 0x28)

