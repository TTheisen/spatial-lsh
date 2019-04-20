import numpy as np 
import time 
import uuid
import operator
from point import Point

""" Customer request. """

class Path():

    def __init__(self, requested_time, s_pos, e_pos):
        self.route = uuid.uuid4()
        self.requested_time = requested_time
        self.start_position = s_pos
        self.end_position = e_pos

    def __repr__(self):
        return repr(self.route)

    def element_wise_addition(self, list1, list2):
        return list(map(operator.add, list1, list2))

    def generate(self):
        path = list([self.start_position])
        x_diff = self.end_position[0] - self.start_position[0]
        y_diff = self.end_position[1] - self.start_position[1]  
        for _ in range(abs(x_diff)):
            if x_diff < 0:
                pos = self.element_wise_addition(path[-1], [-1,0])
                path.append(pos)
            else:
                pos = self.element_wise_addition(path[-1], [1,0])
                path.append(pos)
        for _ in range(abs(y_diff)):
            if y_diff < 0:
                pos = self.element_wise_addition(path[-1], [0,-1])
                path.append(pos)
            else:
                pos = self.element_wise_addition(path[-1], [0,1])
                path.append(pos)
        return path