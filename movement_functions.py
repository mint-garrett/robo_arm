import pigpio
import select
import sys
import termios
import time
import tty
##servo data
period = 20000  # 50 Hz
POS_0   = 1000
POS_90  = 1500
POS_180 = 2000
##motor dictionary
MOTORS = {
    "servo1": {
        "pin": 12,
        "position": POS_90,
        "key_bindings": {"to_0":"z", "to_90":"x", "to_180":"c"},
        "last_key":None,
        "last_key_time": 0.0,
    },
    "servo2": {
        "pin":13,
        "position":POS_0,
        "key_bindings":{"to_0":"a","to_90":"s", "to_180":"d"},
        "last_key":None,
        "last_key_time":0.0,
    },
    "servo3": {
        "pin":3,
        "position":POS_90,
        "key_bindings":{"to_0":"q", "to_90":"w","to_180":"e"},
        "last_key":None,
        "last_key_time": 0.0
    },
    "servo4": {
        "pin":22,
        "position":POS_90,
        "key_bindings":{"to_0":"o", "to_90":"l", "to_180":"p"},
        "last_key":None,
        "last_key_time": 0.0
    }
}
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
def move_to(pi, pin, pulse_width):
    pulse_width = max(POS_0, min(POS_180, pulse_width))
    pi.set_servo_pulsewidth(pin, pulse_width)
    return pulse_width

def move(pi):
    #all motors to starting positions
    for m in MOTORS.values():
        move_to(pi,m["pin"], m["position"])
    time.sleep(.5)

    ##gets current terminal attributes and switces to cbreak for character-by character interpretation
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    tty.setcbreak(fd)
    
    try:
        while True:
            print("starting!")
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
                  ####TODO: fix indentation errors
                key_accept = False
                if key == k["to_90"]:
                    key_accept = True
                    print("hi 90")
                elif key != m["last_key"]:
                    key_accept = True
                    print("hilast key")
                elif (current_time - m["last_key_time"]) >= repeat_key_buffer:
                    key_accept = True
                
                if key_accept: #allows movement incrementally, or to the middle position
                    if key == k['to_0']:
                        m["position"] -= step
                        print("hi - step")
                    elif key == k['to_180']:
                        m["position"] += step
                        print("hi + step")
                    elif key == k['to_90']:
                        m["position"] = POS_90
                        print("hi middle")
                        
                    m["position"] = move_to(pi, m["pin"],m["position"])                 
                    m["last_key"] = key 
                    m["last_key_time"] = current_time
                break      
            time.sleep(delay)

    finally:
        #resets terminal to normal
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        print("exiting!")
