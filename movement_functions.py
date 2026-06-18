import pigpio
import time
from pynput import keyboard

pin12 = 12
period = 20000  # 50 Hz

POS_0   = 1000
POS_90  = 1500
POS_180 = 2000

def move_to(pi, pulse_width):
    pulses = [
        pigpio.pulse(1 << pin12, 0, pulse_width),
        pigpio.pulse(0, 1 << pin12, period - pulse_width),
    ]

    pi.wave_clear()
    pi.wave_add_generic(pulses)
    waveform = pi.wave_create()

    if waveform >= 0:
        pi.wave_send_repeat(waveform)
    else:
        print(f"Wave creation failed: {waveform}")

def move(pi):
    move_to(pi, POS_0)
    time.sleep(2)
	'''TODO: add evdev support for ssh key recognition'''
    current_keys = set()

    def on_press(key):
        try:
            current_keys.add(key.char)
            print(f"got: {key.char}")
        except AttributeError:
            pass

    def on_release(key):
        try:
            current_keys.discard(key.char)
        except AttributeError:
            pass

        if key == keyboard.Key.esc:
            return False

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        while listener.running:

            if 'a' in current_keys:
                move_to(pi, POS_0)
            elif 'd' in current_keys:
                move_to(pi, POS_180)
            elif 'm' in current_keys:
                move_to(pi, POS_90)
            elif 'b' in current_keys:
                break
