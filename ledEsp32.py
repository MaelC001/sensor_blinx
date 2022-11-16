from neopixel import NeoPixel
from machine import Pin

pin = Pin(0, Pin.OUT)   # set GPIO0 to output to drive NeoPixels
np = NeoPixel(pin, 8)   # create NeoPixel driver on GPIO0 for 8 pixels

def immediate(i2c, info):
    text = []
    for i in np[0]:
        text.append(str(i))
    return ';'.join(text)

def functionRead(id):
    return np[0][id].to_bytes(2, 'big')

def functionWrite(id, intColor):
    color = list(np[0])
    color[id] = intColor
    np[0] = color   # set the first pixel to white
    np.write()      # write data to all pixels

info = {
    'name' : ['led'], 
    'info' : {
        #'freq' : '', # analog
        #'addr' : '', # I2C
        #'byteReceive' : '', # I2C
        #'codeSend' : '', # I2C
    }, 
    'channels' : {},
    'functions' : {
        'immediate' : immediate, 
        'functionRead' : functionRead, 
        'functionWrite' : functionWrite, 
        #'create' : '', # display
    }, 
}