
def function(value, oldData, error):
    alpha = 0.75
    return alpha * oldData + (1 - alpha) * value
