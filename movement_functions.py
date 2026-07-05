import pigpio
import select
import sys
import termios
import time
import tty

pin12 = 12
period = 20000  # 50 Hz

POS_0   = 1000
POS_90  = 1500
POS_180 = 2000
#timing variables for move function
step = 20
repeat_key_buffer = .2
delay = .01

#returns key input as a string for move fn
def get_key():
    if select.select([sys.stdin], [], [], 0)[0]:
        return sys.stdin.read(1)
    return None

##early move function, used to initialize move function
def move_to(pi, pulse_width):
    pulse_width = max(POS_0, min(POS_180, pulse_width))
    pi.set_servo_pulsewidth(pin12, pulse_width)
    return pulse_width

def move(pi):
    desired_direction = POS_90
    last_key = None
    last_key_time = 0.0
    key_accept = False
    
    move_to(pi, desired_direction)
    time.sleep(.5)

    ##gets current terminal attributes and switces to cbreak for character-by character interpretation
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    tty.setcbreak(fd)
    
    try:
        while True:
            print("servo 1 listening!")
            key = get_key()
            if key is None:
                time.sleep(delay)
                continue
                
            current_time= time.time()
            
            if key == '\x1b':
                break
            if key in ('a','d','m'):
                key_accept = False
                
                if key == 'm': ##accept variable is the "gateway" to movement
                    key_accept = True
                elif key != last_key:
                    key_accept = True
                elif (current_time - last_key_time) >= repeat_key_buffer:
                    key_accept = True
                    
                if key_accept: #allows movement incrementally, or to the middle position
                    if key == 'd':
                        desired_direction -= step
                    elif key == 'a':
                        desired_direction += step
                    elif key == 'm':
                        desired_direction = POS_90
                        
                    desired_direction = move_to(pi, desired_direction)
                    print(f"rpos: {desired_direction} us   ", end='', flush = True)
                    last_key = key
                    last_key_time = current_time
                
            elif key is not None:
                last_key = None
                
                time.sleep(delay)

    finally:
        #resets terminal to normal
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        print("exiting!")
