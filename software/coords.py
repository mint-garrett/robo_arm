import numpy
from config import MOTORS

def degree_vector_init(): 
    degree_vector = numpy.matrix([[0],[0],[0],[0]])
    return degree_vector

def update_degree_vector(degree_vector, current_wf_pos, last_wf_pos):
    #magical code
    #TODO: get degree values from waveform timing, write them into the degree vector
     
    for name, m in MOTORS.items():
        if m["wf_pos"] != m["old_wf_pos"]:
            sum = m["wf_pos"] - m["old_wf_pos"]
            if sum == -20:
                print("-20")
            elif sum == 20:
                print("20")
            else:
                print(f"{sum}")
        else:
            print("no change")


    #return updated_degree_vector

def triangulate(updated_degree_vector, servo_number):
    #TODO: take degree vector, and turn it into a system that can figure out where the finger is
    something = 0
    return something
