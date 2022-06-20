from machine import Pin, PWM

def write(arrayPwm, arrayValue):
    laP = len(arrayPwm)
    if laP == len(arrayValue):
        for i in range(laP):
            # pin = Pin(pin, Pin.OUT)
            # pwm = PWM(pin)
            # pwm.freq(1000)
            arrayPwm[i].duty(arrayValue[i])
        return ''
    else:
        raise Exception('not the same length')