from machine import Pin, ADC

def immediate(i2c, info):
    result = []
    for pin_info in info:
        Pin(0, mode=Pin.OUT).value(pin_info['p1'])
        Pin(2, mode=Pin.OUT).value(pin_info['p2'])
        Pin(15, mode=Pin.OUT).value(pin_info['p3'])
        tempo = make_data_translate()
        result.append(tempo(ADC(0).read()))
    return ';'.join(result)

def make_data_translate():
    last_value = 0
    def data_translate(value):
        nonlocal last_value
        alpha = 0.75
        new_value = alpha * last_value + (1 - alpha) * value;
        last_value = new_value
        return new_value
    return data_translate

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
                'data' : make_data_translate(),
            }, 
        }, 
    }, 
    'functions' : {
        'immediate' : immediate,
    }, 
}