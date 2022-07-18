from machine import Pin

def immediate(i2c, info):
    result = []
    for pin_info in info:
        pin = pin_info['pin']
        t = Pin(pin, Pin.OUT)
        result.append(b'\x01' if t() else b'\x00')
    return ';'.join(result)

info = {
    'name' : [''],
    'info' : {
        #'freq' : '', # analog
        #'addr' : '', # I2C
        #'byteReceive' : '', # I2C
        #'codeSend' : '', # I2C
    },
    'channels' : {
        '0' : {
            'waiting' : 0,
            'functionsId' : {
                #'byte' : '', # analog + I2C : lambda x,y,z : x
                #'data' : '', # analog + I2C : lambda x:x
            },
        },
    },
    'functions' : {
        'immediate' : immediate,
        #'create' : '', # display
    },
}