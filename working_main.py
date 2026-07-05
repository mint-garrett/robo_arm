import pigpio
from movement_functions import move, pin12

pi = pigpio.pi()
if not pi.connected:
    print("daemon not working")
    raise SystemExit

pi.set_mode(pin12, pigpio.OUTPUT)

try:
    move(pi)
finally:
    pi.set_servo_pulsewidth(pin12,0)
    pi.stop()
