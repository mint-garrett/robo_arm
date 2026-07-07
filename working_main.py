import pigpio
from movement_functions import move, MOTORS

pi = pigpio.pi()
if not pi.connected:
    print("daemon not working")
    raise SystemExit

for m in MOTORS.values():
    pi.set_mode(int(m["pin"]), pigpio.OUTPUT)

try:
    move(pi)
finally:
    for m in MOTORS.values():
        pi.set_servo_pulsewidth(m["pin"],0)
    pi.stop()
