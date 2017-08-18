import math
from vector import Vector3

class Point3(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return 'Point3 <<{0}, {1}, {2}>>'.format(self.x, self.y, self.z)

    def __add__(self, other):
        if isinstance(other, Vector3):
            return Point3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        if isinstance(other, Point3):
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, Vector3):
            return Point3(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, float):
            return Point3(self.x - other, self.y - other, self.z - other)

    def __mul__(self, other):
        if isinstance(self, Vector3):
            return Point3(self.x * other.x, self.y * other.y, self.z * other.z)
        if isinstance(self, float):
            return Point3(self.x * other, self.y * other, self.z * other)

    def __iter__(self):
        for i in [self.x, self.y, self.z]:
            yield i

    def __getitem__(self, item):
        if item == 0:
            return self.x
        if item == 1:
            return self.y
        if item == 2:
            return self.z

    def distance(self, other):
        return (self - other).length()

    def distance_squared(self, other):
        return (self - other).length_squared()

    def lerp(self, t, other):
        return (1-t) * self + t * other

