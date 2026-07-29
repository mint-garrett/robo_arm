##servo data
period = 20000  # 50 Hz
POS_0   = 1000
POS_90  = 1500
POS_180 = 2000
##motor dictionary

MOTORS = {
    "servo1": {
        "location":"base",
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
        "pin":13,
        "wf_pos":POS_0,
        "old_wf_pos":0,
        "coord_pos":0,
        "key_bindings":{"to_0":"a","to_90":"s", "to_180":"d"},
        "last_key":None,
        "last_key_time":0.0,
    },
    "servo3": {
        "location":"wrist",
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