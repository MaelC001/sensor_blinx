from machine import Pin, PWM

def write(pwm, value):
    # pin = Pin(pin, Pin.OUT)
    # pwm = PWM(pin)
    # pwm.freq(1000)
    pwm.duty(value)