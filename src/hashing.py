import numpy as np 

def distance(plane, point):
    p1, p2, p3 = plane[0:2], plane[2:4], point[0:2]
    with np.errstate(divide='ignore', invalid='ignore'):
        d = np.cross(p2 - p1, p1 - p3) / np.linalg.norm(p2 - p1)
    return d

def hash(point, planes):
    hash_value = []
    func = np.arange(1, len(planes) + 1, 1)
    for plane in planes:
        dist = distance(plane, point)
        if dist >= 0.0:
            hash_value.append(1)
        else:
            hash_value.append(0)
    h = np.array(hash_value) * func
    s = np.sum(h)
    return h, s 

def convolution(hashes, padding):
    return np.add.reduceat(hashes, np.arange(0, len(hashes), padding))