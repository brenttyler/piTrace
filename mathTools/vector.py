import math


class Vector3(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return 'Vector3 <<{0}, {1}, {2}>>'.format(self.x, self.y, self.z)

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, vector):
        return self.x * vector.x + self.y * vector.y + self.z * vector.z

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

    def dot(self, other):
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)

    def normalize(self):
        mag = math.sqrt((self.x * self.x) + (self.y * self.y) + (self.z * self.z))
        return Vector3(self.x / mag, self.y / mag, self.z / mag)

    def scale(self, x):
        return self.x * x + self.y * x + self.z * x

    def as_list(self):
        return [self.x, self.y, self.z]
