import ssd1306

class create_display():
    def __init__(self, i2c, *value):
        self.i2c = i2c
        self.display = ssd1306.SSD1306_I2C(128, 64, i2c)
        self.__register = {
            'power_off': self.display.poweroff,
            'power_on': self.display.poweron,
            'contrast': self.display.contrast,
            'invert': self.display.invert,
            'rotate': self.display.rotate,
            'show': self.display.show,
            'fill': self.display.fill,
            'pixel': self.display.pixel,
            'line': self.display.line,
            'vline': self.display.vline,
            'hline': self.display.hline,
            'rect': self.display.rect,
            'fill_rect': self.display.fill_rect,
            'text': self.display.text,
            'scroll': self.display.scroll,
            'blit': self.display.blit,
        }
    def function(self, func_name, *array_value):
        if func_name in self.__register:
            return self.__register[func_name](*array_value)
        else:
            raise KeyError('Function name for the display don\'t exist.')


info = {
    'name' : ['ssd1306_oled', 'ssd13006'], 
    'info' : {}, 
    'channels' : {}, 
    'functions' : {
        'create' : create_display,
    }, 
}