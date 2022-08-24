class create_display():
    def __init__(self, i2c, *value):
        self.i2c = i2c
        self.display = None
        self.__register = {}
    def function(self, func_name, *array_value):
        if func_name in self.__register:
            return self.__register[func_name](*array_value)
        else:
            raise KeyError('Function name for the display don\'t exist.')

info = {
    'name' : ['ht16k33', 'diymall_96'], 
    'info' : {}, 
    'channels' : {}, 
    'functions' : {
        'create' : create_display,
    }, 
}