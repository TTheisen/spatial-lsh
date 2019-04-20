import numpy as np
from plane import Plane

class Partition():

    def __init__(self, grid_id, n_planes, time, xl, xu, yl, yu):
        self.grid_id = grid_id
        self.n_planes = n_planes
        self.time = time
        self.planes = self.add_planes(xl, xu, yl, yu)
    
    def __repr__(self):
        return repr([self.grid_id, self.n_planes, self.time])

    def add_planes(self, xl, xu, yl, yu): #x1, x2, y1, y2
        p = []
        for _ in range(self.n_planes):
            plane = Plane(xl, xu, yl, yu)
            p.append(plane)
        return p

    def get_planes(self):
        return self.planes