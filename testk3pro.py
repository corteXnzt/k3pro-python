import serial
from time import sleep

port = "/dev/ttyUSB0"
ser = serial.Serial(port, 115200, timeout=0)

add_preceeding_data = False
temperature = ''

while True:
	data = ser.read(9999)
	if len(data) > 1:
		# print(data)
		if(add_preceeding_data):
			add_preceeding_data = False
			temperature = temperature + data[0:4]
			print(temperature)
			
		position = data.decode('ISO-8859-1').rfind('T body =')		
		if position > 1:
			if(position == 21):
				add_preceeding_data = True
				temperature = data[position + 9 : position + 9 + 7]	
ser.close()
