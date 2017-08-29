import mathTools as mt

class Shape(object):

    def __init__(self):
        self.objectToWorld = mt.Matrix4x4(1)
        self.worldToObject = mt.Matrix4x4(1).inverse()
        self.reverseOrientation = False
        self.transformSwapsHandedness = False

    def object_bound(self):
        pass

    def world_bound(self):
        pass

    def intersect_p(self):
        pass