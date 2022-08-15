import time

def immediate(i2c, info, addr = 0x70):
    i2c.writeto(addr,b'\x24\x00')
    bytes = i2c.readfrom(addr, 6)
    time.sleep_ms(15)
    data = test_byte(bytes, False, False)
    if data:
        return test_data(data)
    else:
        return 'error'

def test_byte(data, error, old_data):
    result = data[3:5]
    if crc8_sht3(result) != data[5]:
        return error
    return result

def test_data(bytes):
    return (100.0 * float(bytes[0] << 8 | bytes[1]) / 65535.0)

def crc8_sht3(buffer):
	""" Polynomial 0x31 (x8 + x5 +x4 +1) """
	polynomial = 0x31
	crc = 0xFF
	index = 0
	for index in range(0, len(buffer)):
		crc ^= buffer[index]
		for i in range(8, 0, -1):
			if crc & 0x80:
				crc = (crc << 1) ^ polynomial
			else:
				crc = (crc << 1)
	return crc & 0xFF

info = {
    'name' : ['sht3x_hum'],
    'channels' : {
        '0' : {
            'waiting' : 15, 
            'functionsId' : {
                'byte' : test_byte,
                'data' : test_data,
            }, 
        }, 
    }, 
    'functions' : {
        'immediate' : immediate,
    }, 
    'info' : {
    	'addr': 0x70,
    	'byteReceive': 6,
    	'codeSend':  b'\x24\x00',#0x7CA2,
    },
}
