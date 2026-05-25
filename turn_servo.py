from gpiozero import Servo
import time

servo = Servo(18)

while True:
	servo.min()
	print("0 deg")
	time.sleep(2)
	servo.mid()
	print("90 deg")
	time.sleep(2)
	servo.max()
	print("180 deg")
	time.sleep(2)
