import pigpio
import time

pi = pigpio.pi()
if not pi.connected:
    print("daemon not working")
    exit()

pin = 17
period = 20000  # 50Hz

pi.set_mode(pin, pigpio.OUTPUT)

def move_to(pulse_width):
    ## send waveform for a given pulse width in microsecond
    pulses = [
        pigpio.pulse(1 << pin, 0,         pulse_width),
        pigpio.pulse(0,         1 << pin, period - pulse_width),
        ]
    pi.wave_clear()
    pi.wave_add_generic(pulses)
    waveform = pi.wave_create()

    if waveform >= 0:
        pi.wave_send_repeat(waveform)
        print(pulse_width)
    else:
        print(f"Wave creation failed: {waveform}")
    return

POS_0   = 1000   # 0°
POS_90  = 1500   # 90° (center)
POS_180 = 2000   # 180°

try:
    while True:
        move_to(POS_0)
        time.sleep(2)
        move_to(POS_90)
        time.sleep(2)

        move_to(POS_180)
        time.sleep(2)

except KeyboardInterrupt:
    print("Stopping")

finally:
    pi.wave_tx_stop()
    pi.wave_clear()
    pi.stop()
