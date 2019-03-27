# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 12:38:11 2019

@author: ThomasTheisen
"""

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
                hash_value = hashfunc(path[index_plane][0], path[index_plane][1], plane)
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
   

if __name__ == "__main__":
    dim_rows = 100
    dim_columns = 100
    
    grid = Grid(dim_rows, dim_columns)
    path1 = Path()
    path2 = Path()
    
    p1 = Point(1,1,0)
    p2 = Point(1,2,1)
    p3 = Point(1,3,2)
    p4 = Point(2,3,3)
    
    p5 = Point(4,1,0)
    p6 = Point(4,2,1)
    p7 = Point(5,2,2)
    p8 = Point(5,3,3)
    
    plane0 = Plane(dim_rows, dim_columns, 0)
    plane1 = Plane(dim_rows, dim_columns, 1)
    plane2 = Plane(dim_rows, dim_columns, 2)
    plane3 = Plane(dim_rows, dim_columns, 3)
    
    path1.add_point(p1)
    path1.add_point(p2)
    path1.add_point(p3)
    path1.add_point(p4)
    
    path2.add_point(p5)
    path2.add_point(p6)
    path2.add_point(p7)
    path2.add_point(p8)
    
    grid.add_path(path1)
    grid.add_path(path2)
    
    grid.add_plane(plane0)
    grid.add_plane(plane1)
    grid.add_plane(plane2)
    grid.add_plane(plane3)
    
    grid.gen_hash()
    
    
    print(path1)
    print(path2)
    print(grid.hashes)
        