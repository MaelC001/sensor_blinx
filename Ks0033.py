import math

def function(value, oldData, error):
    tempo=(value/1023)*5
    r=(5-tempo)/tempo*4700
    return  1/(math.log(r/10000) /3950 + 1/(25+273.15))-273.15
