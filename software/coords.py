import numpy
from movement_functions import MOTORS

def degree_vector_init(): 
    degree_vector = numpy.array([0],[0],[0],[0])
            return degree_vector

def update_degree_vector(degree_vector, servo_number, current_wf_pos, last_wf_pos):
    #magical code
    #TODO: get degree values from waveform timing, write them into the degree vector
    return updated_degree_vector

def triangulate(updated_degree_vector, servo_number):
    #TODO: take degree vector, and turn it into a system that can figure out where the finger is
    something = 0
    return something
