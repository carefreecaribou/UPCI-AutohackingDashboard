import time

def accelerate(c, v=False):
	c.setCanBaud(CAN_125KBPS)
	for i in range(0, 90):
		str = "\xc9\x5f\x6b\x4d\x4a\x48" + chr(i) + "\xac"
		c.CANxmit(0x110, str)
		time.sleep(0.1)
		if v==True:
			print('110#', str)
	for i in range(90, -1, -1):
		str = "\xc9\x5f\x6b\x4d\x4a\x48" + chr(i) + "\xac"
		c.CANxmit(0x110, str)
		time.sleep(0.1)
		if v==True:
			print('110#', str)
