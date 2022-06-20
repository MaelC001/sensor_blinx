from machine import Pin

def write(pin, value):
    return Pin(pin, mode=Pin.OUT).value(value)