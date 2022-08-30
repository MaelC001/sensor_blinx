import ssd1306

class create_display():
    def __init__(self, i2c, *value):
        self.i2c = i2c
        x = 128
        y = 64
        if len(value) == 2:
            x = value[0]
            y = value[1]
        self.display = ssd1306.SSD1306_I2C(x, y, i2c)
        self.__register = {
            'power_off': {'func':self.display.poweroff, 'type': [[]]},
            'power_on': {'func':self.display.poweron, 'type': [[]]},
            'contrast': {'func':self.display.contrast, 'type': [[int]]},
            'invert': {'func':self.display.invert, 'type': [[int]]},
            'rotate': {'func':self.display.rotate, 'type': [[bool]]},
            'show': {'func':self.display.show, 'type': [[]]},
            'fill': {'func':self.display.fill, 'type': [[int]]},
            'pixel': {'func':self.display.pixel, 'type': [[int, int], [int, int, int]]},
            'line': {'func':self.display.line, 'type': [[int, int, int, int, int]]},
            'vline': {'func':self.display.vline, 'type': [[int, int, int, int, int]]},
            'hline': {'func':self.display.hline, 'type': [[int, int, int, int, int]]},
            'rect': {'func':self.display.rect, 'type': [[int, int, int, int, int]]},
            'fill_rect': {'func':self.display.fill_rect, 'type': [[int, int, int, int, int]]},
            'text': {'func':self.display.text, 'type': [[str, int, int, int]]},
            'scroll': {'func':self.display.scroll, 'type': [[int, int]]},
            #'blit': {'func':self.display.blit, 'type': [..., int, int, int]},
        }
    def function(self, func_name, *array_value):
        if func_name in self.__register:
            temp = self.__register[func_name]
            s = []
            for i in range(len(temp['type'])):
                if len(array_value) in len(temp['type'][i]):
                    array_value_format = []
                    for y in range(len(array_value)):
                        array_value_format.append(temp['type'][y](array_value[i][y]))
                    return temp['func'](*array_value_format)
            raise KeyError('Not the good amount of arguments.')
        else:
            raise KeyError('Function name for the display don\'t exist.')


info = {
    'name' : ['ssd1306_oled', 'ssd13006', 'screen'], 
    'info' : {}, 
    'channels' : {}, 
    'functions' : {
        'create' : create_display,
    }, 
}
