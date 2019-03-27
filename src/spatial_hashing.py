'''

Author: Thomas Theisen

Objective: Hash Spatial 2D Features using Random Planes 

'''

import numpy as np
import math

class Grid():
    
    def __init__(self, row_cells, column_cells):
        self.rows = row_cells
        self.columns = column_cells
        self.grid = np.zeros((self.rows, self.columns))
        self.paths = []
        self.planes = []
        self.hashes = {}
        
    def __repr__(self):
        return repr(self.grid)
        
    def add_path(self, path):
        self.paths.append(path)
        
    def add_plane(self, plane):
        self.planes.append(plane)
        
    def gen_hash(self):
        for index_path, path in enumerate(self.paths):
            key = 'Path' + str(index_path)
            self.hashes[key] = []
            for index_plane, plane in enumerate(self.planes):
                hash_value = hashfunc(path[index_plane][0], path[index_plane][1], plane)    #applying one plane
                self.hashes[key].append(hash_value)
                
class Path():

    def __init__(self):
        self.path = list()
        
    def __repr__(self):
        return repr(self.path)
    
    def __getitem__(self, index):
        return self.path[index]
          
    def add_point(self, point):
        self.path.append(point)
        
class Point():
    
    def __init__(self, latitude, longitude, time):
        self.point = [latitude, longitude, time]
        
    def __repr__(self):
        return repr(self.point)
    
    def __getitem__(self, index):
        return self.point[index]
    
class Plane():
    
    def __init__(self, row_cells, column_cells, time):
        self.plane = [[0, np.random.randint(row_cells)], [column_cells, np.random.randint(row_cells)], time]

    def __repr__(self):
        return repr(self.plane)
    
    def __getitem__(self, index):
        return self.plane[index]
 
def hashfunc(x, y, plane):
   
    sign = distance(x, y, plane)
    if sign > 0:
        return 1
    else: 
        return 0
    
def distance(x, y, plane):
    pp1, pp2 = plane[0], plane[1]
    n = abs(pp2[0] - pp1[0]) * (pp1[1] - y) - (pp1[0] - x) * (pp2[1] - pp1[1])
    d = math.sqrt(math.pow((pp2[0] - pp1[0]), 2) + math.pow((pp2[1] - pp1[1]),2))
    return n/d

def invalid_position(new_coordinate, bounds):      
    
    new_latitude, new_longitude = new_coordinate[0], new_coordinate[1]
    if new_latitude < bounds[0] or new_latitude > bounds[1]:
        return True
    elif new_longitude < bounds[2] or new_longitude > bounds[3]:
        return True
    else:
        return False

def generate_random_paths(row_cells, column_cells, timesteps):
    
    bounds = [0, row_cells, 0, column_cells]
    
    path = Path()
    
    latitude, longitude, t = np.random.randint(row_cells), np.random.randint(row_cells), 0
    
    current_point = Point(latitude, longitude, t)
           
    valid_position = True
    while t < timesteps:
        while valid_position:
            x_, y_ = np.random.randint(3), np.random.randint(3)
            
            if x_ == 0:
                x_vec = -1
            elif x_ == 1:
                x_vec = 0
            elif x_ == 2:
                x_vec = 1
                
            if y_ == 0:
                y_vec = -1
            elif y_ == 1:
                y_vec = 0
            elif y_ == 2:
                y_vec = 1
                       
            new_position = [current_point[0] + x_vec, current_point[1] + y_vec]
            
            valid_position= invalid_position(new_position, bounds)
        
        new_point = Point(new_position[0], new_position[1], t)
        t += 1
        path.add_point(new_point)
        
    return path

            
if __name__ == "__main__":
    dim_rows = 5
    dim_columns = 5
    time_steps = 5
    num_paths = 5
    
    grid = Grid(dim_rows, dim_columns)
        
    for _ in range(num_paths):
        grid.add_path(generate_random_paths(dim_rows, dim_columns, time_steps))

    for t in range(time_steps):
        grid.add_plane(Plane(dim_rows, dim_columns, t))        
        
    grid.gen_hash()
    print(grid.hashes)

        