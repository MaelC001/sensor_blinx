from machine import Pin, ADC

def immediate(i2c, info):
    result = []

    # analog
    pin_info = info[0]
    Pin(0, mode=Pin.OUT).value(pin_info['p1'])
    Pin(2, mode=Pin.OUT).value(pin_info['p2'])
    Pin(15, mode=Pin.OUT).value(pin_info['p3'])
    result.append(ADC(0).read())

    # digital
    pin_info = info[0]
    pin = pin_info['pin']
    t = Pin(pin, Pin.OUT)
    result.append(b'\x01' if t() else b'\x00')

    return ';'.join(result)

info = {
    'name' : ['ms1100'], 
    'info' : {
        'freq' : 1000,
    }, 
    'channels' : {
        '0' : {
            'waiting' : 0, 
            'functionsId' : {
                'byte' : lambda x, y, z : x,
                'data' : lambda x:int.from_bytes(x, 'big'),
            }, 
        }
    }, 
    'functions' : {
        'immediate' : immediate,
    }, 
}