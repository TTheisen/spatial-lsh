'''
Take a image from google maps, construct node/edge paths
from image, and model traffic patterns
'''


import sys
sys.path.insert(0, '..')

import os
import json
import pickle
import requests
import shutil
import random
import numpy as np 

from collections import defaultdict
from scipy import ndimage
from datetime import date
from datetime import datetime

import matplotlib.pyplot as plt

from owslib.wms import WebMapService
import shapefile
import cv2

sf = shapefile.Reader(r"C:/Users/Thomas_Theisen/Documents/roads/tl_2016_us_primaryroads.shp")

import sklearn.neighbors

class Kdtree():
    def __init__(self, points):
        self.tree = sklearn.neighbors.KDTree(points, leaf_size = 2)
    def query(self, point, radius):
        all_nearest_neighbor_indices = self.tree.query_radius(point, r = radius)
        all_nearest_neighbors = [
            [point[idx] for idx in nearest_neighbor_indices if idx != i] 
            for i, nearest_neighbor_indices in enumerate(all_nearest_neighbor_indices)
        ]
        return all_nearest_neighbors

class Network():
    def __init__(self):
        self.nodes = []
        self.kdtree = None
    def add_node(self, *nodes):
        for n in nodes:
            self.nodes.append(n)
    def fill_kdtree(self):
        points = [(n.lat, n.long) for n in self.nodes]
        self.kdtree = Kdtree(points)
    def contains(self, kdtree, node):
        if kdtree is None:
            if not self.nodes:
                raise NotImplementedError
            else:
                self.fill_kdtree()
        point = (node.lat, node.long)
        neighbors = self.kdtree.query(point, 0.001)
        for n in neighbors:
            if point[0] >= n.bbox[0] and point[0] <= n.bbox[1] and point[1] >= n.bbox[2] and point[1] <= n.bbox[3]:
                node.close_nodes.append(n)

class Node():
    def __init__(self, latitude, longitude, bbox_buffer):
        self.buffer = bbox_buffer
        self.lat = latitude
        self.long = longitude
        self.link = None
        self.bbox = self.set_bounding_box(self.buffer, self.buffer)
        self.close_nodes = []
    def add_node_pair(self, Node):
        self.link = Node
    def set_bounding_box(self, x_buffer, y_buffer):
        left_x, right_x = self.lat - x_buffer, self.lat + x_buffer
        low_y, up_y = self.long - y_buffer, self.long + y_buffer
        bbox = [left_x, right_x, low_y, up_y]
        return bbox

if __name__ == "__main__":
    network = Network()
    plt.figure()
    for shape in sf.shapeRecords()[0:1]:
        x = [i[0] for i in shape.shape.points[:]]
        y = [i[1] for i in shape.shape.points[:]]
        if min(x) > -150 and min(y) > 20: #Exclude Alaska and Hawaii for now
            plt.plot(x,y)
            node1 = Node(x[0], y[0], 1e-6)
            node2 = Node(x[-1], y[-1], 1e-6)
            node1.add_node_pair(node2)
            node2.add_node_pair(node1)
            network.add_node(node1)
            network.add_node(node2)
    plt.show()


