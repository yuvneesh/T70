import serial

ser=serial.Serial("/dev/ttyp1", baudrate=2400, 
timeout=5,
bytesize=serial.EIGHTBITS,
stopbits = serial.STOPBITS_ONE,
parity=serial.PARITY_NONE)

data = b''
	
print('Starting to Read...')

"""
	while True:
		readText = ser.read(10)
		print(readText)
	
	
"""
with open("virtual_data.txt", "w") as f:
	try:
		while True:
			readText = ser.read(10)
			data += readText
	except KeyboardInterrupt:
		f.write(data.decode())
		f.close()
		raise


	

ser.close
print('script ended')
