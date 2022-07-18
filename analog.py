
def function(a, b, c):
    return a


info = {
    'name' : ['led', 'buzzer_digi', 'buzzer_passive', 'relay_5v', '3w_led', 'white_led', 'red_led', 'green_led', 'yellow_led', 'blue_led', 'SFE_Reed_Switch', 'Reed_Switch'],
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