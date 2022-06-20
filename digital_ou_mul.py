from machine import Pin

def write(arrayPin, arrayValue):
    laP = len(arrayPin)
    if laP == len(arrayValue):
        for i in range(laP):
            # pin = Pin(pin, mode=Pin.OUT)
            arrayPin[i].value(arrayValue[i])
        return ''
    else:
        raise Exception('not the same length')