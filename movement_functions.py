
import sys
import termios
import tty
import select
import pigpio
import time

pin12 = 12
period = 20000  # 50 Hz

POS_0   = 1000
POS_90  = 1500
POS_180 = 2000

def get_key():
    key = None
    if select.select([sys.stdin], [], [], 0)[0]:
        return sys.stdin.read(1)
    return None

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
    ####TODO: figure out step timing/ servo precision issue
    step = 50
    step_time = 0
    desired_direction = POS_0
    
    move_to(pi, desired_direction)
    time.sleep(2)
    
    delay = .15
    last_direction = desired_direction
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    tty.setcbreak(fd)
    
    try:
        while True:
            print("servo 1 listening!")
            key = get_key()
            current_time= time.time()
            
            if key == '\x1b':
                break
            if key and (current_time - step_time) >= step:
                if key == 'a':
                    desired_direction = min(POS_0, desired_direction + step)
                    print("a being pressed")
                elif key == 'd':
                    desired_direction = max(POS_180, desired_direction - step)
                    print("d being pressed")
                elif key == 'm':
                    desired_direction = POS_90
                    print("middle")
                step_time = current_time
                
            if desired_direction != last_direction:
                move_to(pi, desired_direction)
                last_direction = desired_direction
                
            time.sleep(.1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        print("exiting!")
