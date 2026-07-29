import pigpio
import select
import sys
import termios
import time
import tty

from config import period, POS_0, POS_180, POS_90, MOTORS, step, repeat_key_buffer, delay
from coords import degree_vector_init, update_degree_vector

degree_vector = degree_vector_init()

#returns key input as a string for move fn
def get_key():
    if select.select([sys.stdin], [], [], 0)[0]:
        return sys.stdin.read(1)
    return None

##early move function, used to initialize move function
def move_to(pi, pin, pulse_width):
    pulse_width = max(POS_0, min(POS_180, pulse_width))
    pi.set_servo_pulsewidth(pin, pulse_width)
    return pulse_width

def move(pi):
    #all motors to starting positions
    for m in MOTORS.values():
        move_to(pi,m["pin"], m["wf_pos"])
    time.sleep(.5)

    ##gets current terminal attributes and switces to cbreak for character-by character interpretation
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    tty.setcbreak(fd)
    
    try:
        print("starting!")
        while True:
            key = get_key()
            if key is None:
                time.sleep(delay)
                continue
            #master exit
            if key == '\x1b':
                break
                
            current_time= time.time()

            for name, m in MOTORS.items():
                k = m["key_bindings"]
                if key not in (k["to_0"],k["to_90"],k["to_180"]):
                    continue
                key_accept = False
                if key == k["to_90"]:
                    key_accept = True
                elif key != m["last_key"]:
                    key_accept = True
                elif (current_time - m["last_key_time"]) >= repeat_key_buffer:
                    key_accept = True

                from coords import degree_vector_init, update_degree_vector
                if key_accept: #allows movement incrementally, or to the middle position
                    if key == k['to_0']:
                        m["old_wf_pos"] = m["wf_pos"]
                        m["wf_pos"] -= step
                        print(f"{m["location"]}    key = {k["to_0"]}   wf len = {m["wf_pos"]}")
                        update_degree_vector(degree_vector, m["wf_pos"], m["old_wf_pos"])
                        
                    elif key == k['to_180']:
                        m["old_wf_pos"] = m["wf_pos"]
                        m["wf_pos"] += step
                        print(f"{m["location"]}    key = {k["to_180"]}   wf len = {m["wf_pos"]}")
                        update_degree_vector(degree_vector, m["wf_pos"], m["old_wf_pos"])

                    elif key == k['to_90']:
                        m["old_wf_pos"] = m["wf_pos"]
                        m["wf_pos"] = POS_90
                        print(f"{m["location"]}    key = {k["to_90"]}  center wf: {m["wf_pos"]}")
                        update_degree_vector(degree_vector, m["wf_pos"], m["old_wf_pos"])
                        
                    
                    m["wf_pos"] = move_to(pi, m["pin"],m["wf_pos"])                 
                    m["last_key"] = key 
                    m["last_key_time"] = current_time
                break      
            time.sleep(delay)

    finally:
        #resets terminal to normal
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        print("exiting!")
