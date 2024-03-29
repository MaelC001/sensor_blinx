from machine import Pin, ADC

def immediate(i2c, info):
    result = []
    for pin_info in info:
        Pin(0, mode=Pin.OUT).value(pin_info['p1'])
        Pin(2, mode=Pin.OUT).value(pin_info['p2'])
        Pin(15, mode=Pin.OUT).value(pin_info['p3'])
        result.append(ADC(0).read())
    return ';'.join(result)

info = {
    'name' : ['gp2y014au', 'electomagnet', '4550ntu', 'rotation_analog', 'sound_analog', 'moisture_sensor', 'ceramic_vibration', 'LM358', 'rotation_analog', 'mq_2', 'mq_3', 'mq_4', 'mq_5', 'mq_6', 'mq_7', 'mq_8', 'mq_9', 'mq_135', 'ad_key_button', 'knock_sensor', 'slide_potentiometre', 'lm35', 'photocell', 'analog_temperature', 'microphone', 'water_sensor', 'soil_humidity', 'temt6000', 'steam_sensor', 'guva_s12sd_3528', 'piezoelectric', 'thin_film_pressure', 'xd_58c', 'gy_ml8511'] + ['servo_9g', 'vibration_motor', 'l9110', 'sg90s'], 
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
        }, 
    }, 
    'functions' : {
        'immediate' : immediate,
    }, 
}