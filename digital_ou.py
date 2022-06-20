from machine import Pin

def write(pin, value):
    # pin = Pin(pin, mode=Pin.OUT)
    return pin.value(value)