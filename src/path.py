import numpy as np 
import time 
import uuid

""" Customer request. """

class Path():

    def __init__(self, requested_time, s_pos, e_pos):
        self.route = uuid.uuid4()
        self.requested_time = requested_time
        self.start_position = s_pos
        self.end_position = e_pos

    def __repr__(self):
        return repr(self.route)

    def delta_time(self):
        return self.requested_time -  time.time()
    

