from machine import Pin

def immediate(i2c, info):
    result = []
    for pin_info in info:
        pin = pin_info['pin']
        t = Pin(pin, Pin.OUT)
        result.append(b'\x01' if t() else b'\x00')
    return ';'.join(result)

info = {
    'name' : ['cs100a', 'relay2', 'a4988', 'led', 'buzzer_digi', 'buzzer_passive', 'relay_5v', '3w_led', 'white_led', 'red_led', 'green_led', 'yellow_led', 'blue_led', 'sfe_reed_switch', 'reed_switch', 'tilt', 'capacitive_touch', 'flame_sensor', '801s', 'infrared_obstacle', 'line_tracking', 'pir', 'xkc_y25_t12v', 'dht11', 'push_button', 'collision_sensor'], 
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
                #'byte' : '', # analog + I2C : lambda x, y, z : x
                #'data' : '', # analog + I2C : lambda x:x
            }, 
        }, 
    }, 
    'functions' : {
        'immediate' : immediate, 
        #'create' : '', # display
    }, 
}