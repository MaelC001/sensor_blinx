from machine import Pin, ADC

def immediate(i2c, info):
    result = []
    for pin_info in info:
        Pin(0, mode=Pin.OUT).value(pin_info['p1'])
        Pin(2, mode=Pin.OUT).value(pin_info['p2'])
        Pin(15, mode=Pin.OUT).value(pin_info['p3'])
        result.append(data_translate(ADC(0).read()))
    return ';'.join(result)

last_value = 0
def data_translate(value):
    global last
    alpha = 0.75
    new_value = alpha * last_value + (1 - alpha) * value;
    last_value = new_value
    return new_value

info = {
    'name' : ['pulse_rate'], 
    'info' : {
        'freq' : 1000,
    }, 
    'channels' : {
        '0' : {
            'waiting' : 0, 
            'functionsId' : {
                'byte' : lambda x, y, z : x,
                'data' : data_translate,
            }, 
        }, 
    }, 
    'functions' : {
        'immediate' : immediate,
    }, 
}