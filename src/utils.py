from point import Point
from plane import Plane
from path import Path
from partition import Partition
import hashing
import random

def rn(upper):
    return random.randint(0, upper)

def random_point():
    return Point(rn(100), rn(100), rn(100))

def random_path():
    p = Path(rn(100), [rn(100), rn(100)], [rn(100), rn(100)])
    return p.generate()

def hash_all(paths):
    for path in paths:
        h = []
        for p in path:
            partition = Partition(1, 10, 1, 0, 1000, 0, 1000)
            _, s = hashing.hash(p, partition.get_planes())
            h.append(s)
        print(h)
