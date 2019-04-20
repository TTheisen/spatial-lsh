from point import Point
from plane import Plane
from partition import Partition
import hashing


if __name__ == "__main__":
    point = Point(1, 1, 1)
    partition = Partition(1, 10, 1, 0, 10, 0, 10)
    h = hashing.hash(point, partition.get_planes())
    print(h)