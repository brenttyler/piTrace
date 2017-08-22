

class Ray(object):

    def __int__(self, origin, direction):
        self.origin = self.o = origin
        self.direction = self.d = direction

        self.tMax = float()
        self.time = float()
        self.medium = None

