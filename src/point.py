import numpy as np 

""" Discrete object making up path. """

class Point():

    def __init__(self, x, y, time):
        self.x = x
        self.y = y
        self.point = np.array([self.x, self.y])
        self.time = time
    
    def __repr__(self):
        return repr(self.point)

    def __getitem__(self, index):
        return self.point[index]

    