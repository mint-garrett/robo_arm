##servo data
period = 20000  # 50 Hz
POS_0   = 1000
POS_90  = 1500
POS_180 = 2000
deg_per_us = .18 #180/(2000-1000)
##motor dictionary

MOTORS = {
    "servo1": {
        "location":"base",
        "idx":0,
        "pin": 12,
        "wf_pos": POS_90,
        "old_wf_pos":0,
        "coord_pos":0,
        "key_bindings": {"to_0":"z", "to_90":"x", "to_180":"c"},
        "last_key":None,
        "last_key_time": 0.0,
    },
    "servo2": {
        "location":"shoulder",
        "idx":1,
        "pin":13,
        "wf_pos":POS_90,
        "old_wf_pos":0,
        "coord_pos":0,
        "key_bindings":{"to_0":"a","to_90":"s", "to_180":"d"},
        "last_key":None,
        "last_key_time":0.0,
    },
    "servo3": {
        "location":"wrist",
        "idx":2,
        "pin":3,
        "wf_pos":POS_90,
        "old_wf_pos":0,
        "coord_pos":0,
        "key_bindings":{"to_0":"q", "to_90":"w","to_180":"e"},
        "last_key":None,
        "last_key_time": 0.0
    },
    "servo4": {
        "location":"finger",
        "idx":3,
        "pin":22,
        "wf_pos":POS_90,
        "old_wf_pos":0,
        "coord_pos":0,
        "key_bindings":{"to_0":"o", "to_90":"l", "to_180":"p"},
        "last_key":None,
        "last_key_time": 0.0
    }
}
#timing variables for move function
step = 20
repeat_key_buffer = .2
delay = .01