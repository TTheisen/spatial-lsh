from point import Point
from plane import Plane
from path import Path
from partition import Partition
import hashing


if __name__ == "__main__":
    point = Point(1, 1, 1)
    path1 = Path(1, [0,0], [5,5])
    path2 = Path(2, [5,5], [0,0])
    path1 = path1.generate()
    path2 = path2.generate()
    paths = [path1, path2]

    for path in paths:
        h = []
        for p in path:
            partition = Partition(1, 10, 1, 0, 10, 0, 10)
            _, s = hashing.hash(p, partition.get_planes())
            h.append(s)
        print(h)
