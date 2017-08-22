from vector import Vector3


class Point3(object):
    """ Standard 3 dimensional point class """

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return 'Point3 <<{0}, {1}, {2}>>'.format(self.x, self.y, self.z)

    def __add__(self, other):
        if isinstance(other, Vector3) or isinstance(other, Point3):
            return Point3(self.x + other.x, self.y + other.y, self.z + other.z)
        if isinstance(other, float) or isinstance(other, int):
            return Point3(self.x + other, self.y + other, self.z + other)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Point3):
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, Vector3):
            return Point3(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, float):
            return Point3(self.x - other, self.y - other, self.z - other)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if isinstance(other, Vector3):
            return Point3(self.x * other.x, self.y * other.y, self.z * other.z)
        if isinstance(other, float):
            return Point3(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        return self.__mul__(other)

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

    def to_vector3(self):
        return Vector3(self.x, self.y, self.z)
