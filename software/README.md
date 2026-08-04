Software README.md:

config.py - contains all data (MOTORS dict and important variables) needed for the coords.py and movment_functions.py. 

coords.py - defines all functions related to the arm's position in space (degree_vector_init(), update_degree_vector())

movement_functions.py - contains the move() function, which basically serves as the project's main function.

working_main.py - starts the pigpiod daemon and the move() function
