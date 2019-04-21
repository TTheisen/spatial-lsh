from point import Point
from plane import Plane
from path import Path
from partition import Partition
import hashing
import random

variability = 10000

def rn(upper):
    return random.randint(0, upper)

def random_point():
    return Point(rn(variability), rn(variability), rn(variability))

def random_path():
    p = Path(rn(variability), [rn(variability), rn(variability)], [rn(variability), rn(variability)])
    return p.generate()

def hash_all(paths):
    coll = []
    for path in paths:
        h = []
        for p in path:
            partition = Partition(1, 10, 1, 0, 1000, 0, 1000)
            _, s = hashing.hash(p, partition.get_planes())
            h.append(s)
        coll.append(h)
    return coll

def convolution_all(hashes, padding):
    c = []
    for h in hashes:
        c.append(hashing.convolution(h, padding))
    return c  