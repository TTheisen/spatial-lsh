# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 11:33:36 2019

@author: ThomasTheisen
"""

import numpy as np
import math

class Grid():
    
    def __init__(self, l, w):
        self.grid = np.zeros((l,w))
                
class Path():
    
    def __init__(self, moves):
        self.pos_start = np.array((np.random.randint(11), np.random.randint(11)))
        self.chain = np.array(self.pos_start)
        self.length = 1
        
    def move(self):
        
        if self.length == 1:
            current_position = self.chain
        else:
            current_position = self.chain[-1]
            
        valid_position = True
        while valid_position:
            h_, v_ = np.random.randint(3), np.random.randint(3)
            
            if h_ == 0:
                h_vec = -1
            elif h_ == 1:
                h_vec = 0
            elif h_ == 2:
                h_vec = 1
                
            if v_ == 0:
                v_vec = -1
            elif v_ == 1:
                v_vec = 0
            elif v_ == 2:
                v_vec = 1
                       
            new_position = np.array((current_position[0] + h_vec, current_position[1] + v_vec))
            
            valid_position = invalid_position(new_position, 0, 10, 0, 10)
        
        self.chain = np.vstack((self.chain, new_position))
        self.length += 1
        
        
def invalid_position(position, x_lower, x_upper, y_lower, y_upper):
    h, v = position[0], position[1]
    
    if h < x_lower or h > x_upper:
        return True
    elif v < y_lower or v > y_upper:
        return True
    else:
        return False
    
def generate_plane(x_lower, x_upper, y_lower, y_upper):
    p1 = np.array((0, np.random.randint(y_lower, y_upper+1)))
    p2 = np.array((x_upper, np.random.randint(y_lower, y_upper+1)))
    return p1, p2


def distance(plane, x, y):
    pp1, pp2 = plane
    n = abs(pp2[0] - pp1[0]) * (pp1[1] - y) - (pp1[0] - x) * (pp2[1] - pp1[1])
    d = math.sqrt(math.pow((pp2[0] - pp1[0]), 2) + math.pow((pp2[1] - pp1[1]),2))
    return n/d

def hashfunc(plane1, plane2, x, y):
    p1_sign = distance(plane1, x, y)
    p2_sign = distance(plane2, x, y)
    if p1_sign > 0 and p2_sign > 0:
        return 3
    elif p1_sign > 0 and p2_sign < 0:
        return 2
    elif p1_sign < 0 and p2_sign > 0:
        return 1
    else: 
        return 0
    

    

if __name__ == "__main__":
    g = Grid(10,10)
    p1 = Path(5)
    p2 = Path(5)
    for _ in range(5):
        p1.move()
        p2.move()
    
    plane1 = generate_plane(0, 10, 0, 10)
    plane2 = generate_plane(0, 10, 0, 10)
    plane3 = generate_plane(0, 10, 0, 10)
    plane4 = generate_plane(0, 10, 0, 10)
    plane5 = generate_plane(0, 10, 0, 10)
    plane6 = generate_plane(0, 10, 0, 10)
    plane7 = generate_plane(0, 10, 0, 10)
    plane8 = generate_plane(0, 10, 0, 10)
    plane9 = generate_plane(0, 10, 0, 10)
    plane10 = generate_plane(0, 10, 0, 10)
    plane11 = generate_plane(0, 10, 0, 10)
    plane12 = generate_plane(0, 10, 0, 10)
    plane_group1 = [plane1, plane2, plane3, plane4, plane5, plane6]
    plane_group2 = [plane7, plane8, plane9, plane10, plane11, plane12]
    
    #Both planes and points change throughout t time steps
    for i in range(len(p1.chain)):
        print(hashfunc(plane_group1[i], plane_group2[i], p1.chain[i][0], p1.chain[i][1]), end='')
