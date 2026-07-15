import pigpio
import subprocess
import time

from movement_functions import move, MOTORS

try:
    subprocess.run("sudo pigpiod", timeout = 5, shell = True)
    print("subprocess executed")
    time.sleep (2)
except subprocess.TimeoutExpired as f:
    print(f"pigpiod is started but timed out waiting: {f}")
except subprocess.CalledProcessError as e:
    print(f"sudo pigpiod failed to execute: {e}")


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
