import numpy
from config import MOTORS, deg_per_us, POS_0, POS_180, POS_90

def degree_vector_init(): 
    degree_vector = numpy.matrix([[0],[0],[0],[0]], dtype=float )
    return degree_vector

def update_degree_vector(degree_vector, motor_idx, current_wf_pos, last_wf_pos):
    if current_wf_pos == last_wf_pos:
        return degree_vector

    current_wf_pos = max(POS_0, min(POS_180, current_wf_pos))
    last_wf_pos = max(POS_0, min(POS_180, last_wf_pos))

    wf_difference = current_wf_pos - last_wf_pos
    deg_difference = wf_difference * deg_per_us
    degree_vector[motor_idx, 0] += deg_difference
    
    return degree_vector

def triangulate(degree_vector, servo_number):
    #TODO: take degree vector, and turn it into a system that can figure out where the finger is
    something = 0
    return something
