from point import Point3
from vector import Vector3


class Bounds3(object):
    """Axis aligned bounding box."""
    def __init__(self, p1, p2):
        self.p_min = Point3(min(p1.x, p2.x), min(p1.y, p2.y), min(p1.z, p2.z))
        self.p_max = Point3(max(p1.x, p2.x), max(p1.y, p2.y), max(p1.z, p2.z))

    def __repr__(self):
        return "Bounds3 Min {0} Max {1}".format(self.p_min, self.p_max)

    def __iter__(self):
        for i in [self.p_min, self.p_max]:
            yield i

    def corner(self, index):
        pass

    def union(self, other):
        if isinstance(other, Bounds3):
            return Bounds3(Point3(min(self.p_min.x, other.p_min.x),
                                  min(self.p_min.y, other.p_min.y),
                                  min(self.p_min.z, other.p_min.z)),
                           Point3(max(self.p_max.x, other.p_max.x),
                                  max(self.p_max.y, other.p_max.y),
                                  max(self.p_max.z, other.p_max.z)))
        if isinstance(other, Point3):
            return Bounds3(Point3(min(self.p_min.x, other.x),
                                  min(self.p_min.y, other.y),
                                  min(self.p_min.z, other.z)),
                           Point3(max(self.p_max.x, other.x),
                                  max(self.p_max.y, other.y),
                                  max(self.p_max.z, other.z)))

    def intersection(self, other):
        return Bounds3(Point3(max(self.p_min.x, other.p_min.x),
                              max(self.p_min.y, other.p_min.y),
                              max(self.p_min.z, other.p_min.z)),
                       Point3(min(self.p_max.x, other.p_max.x),
                              min(self.p_max.y, other.p_max.y),
                              min(self.p_max.z, other.p_max.z)))

    def overlaps(self, other):
        x = self.p_max.x >= other.p_min.x and self.p_min.x <= other.p_max.x
        y = self.p_max.y >= other.p_min.y and self.p_min.y <= other.p_max.y
        z = self.p_max.z >= other.p_min.z and self.p_min.z <= other.p_max.z
        return all([x, y, z])

    def inside(self, other):
        x = self.p_max.x > other.x >= self.p_min.x
        y = self.p_max.y > other.x >= self.p_min.y
        z = self.p_max.z > other.x >= self.p_min.z
        return all([x, y, z])

    def expand(self, delta):
        return Bounds3(self.p_min - Vector3(delta, delta, delta),
                       self.p_max + Vector3(delta, delta, delta))

    def diagonal(self):
        return self.p_max - self.p_min

    def surface_area(self):
        d = self.diagonal()
        return 2 * (d.x * d.y + d.x * d.z + d.y * d.z)

    def volume(self):
        d = self.diagonal()
        return d.x * d.y * d.z

    def maximum_extent(self):
        d = self.diagonal()
        if d.x > d.y and d.x > d.z:
            return 0
        elif d.y > d.z:
            return 1
        else:
            return 2

    def lerp(self, t):
        """Linear interpolation between p_min and p_max by Point3 t."""
        pass

    def bounding_sphere(self):
        pass

