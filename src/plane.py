import random
import numpy as np

""" Object used for spatial hashing. """

class Plane():

    def __init__(self, x_lower, x_upper, y_lower, y_upper):
        self.x_l = x_lower
        self.x_u = x_upper
        self.y_l = y_lower
        self.y_u = y_upper
        self.plane = self.generate()

    def __repr__(self):
        return repr(self.plane)

    def __getitem__(self, index):
        return self.plane[index]
    
    def generate(self): #coordinate order: x1, y1, x2, y2
        t = random.randint(1,6) 
        if t == 1:   #left vertical to upper horizontal
            return np.array([self.x_l, np.random.randint(self.y_u), np.random.randint(self.x_u), self.y_u])
        elif t == 2: #left vertical to right vertical
            return np.array([self.x_l, np.random.randint(self.y_u), self.x_u, np.random.randint(self.y_u)])
        elif t == 3: #left vertical to lower horizontal
            return np.array([self.x_l, np.random.randint(self.y_u), np.random.randint(self.x_u), self.y_l])
        elif t == 4: #lower horizontal to upper horizontal
            return np.array([np.random.randint(self.x_u), self.y_l, np.random.randint(self.x_u), self.y_u])
        elif t == 5: #lower horizontal to right vertical
            return np.array([np.random.randint(self.x_u), self.y_l, self.x_u, np.random.randint(self.y_u)])
        else:        #upper horizontal to right vertical
            return np.array([np.random.randint(self.x_u), self.y_u, self.x_u, np.random.randint(self.y_u)])