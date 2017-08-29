from point import Point3
from vector import Vector3


class Matrix4x4(object):
    def __init__(self, *args):

        self.m = [[0]*4]*4

        if len(args) == 1 and isinstance(args[0], float) or isinstance(args[0], int):
            self.m[0] = [args[0], 0, 0, 0]
            self.m[1] = [0, args[0], 0, 0]
            self.m[2] = [0, 0, args[0], 0]
            self.m[3] = [0, 0, 0, args[0]]

        if len(args) == 4:
            self.m[0] = args[0]
            self.m[1] = args[1]
            self.m[2] = args[2]
            self.m[3] = args[3]

        if len(args) == 16:
            self.m = [[args[0], args[1], args[2], args[3]],
                      [args[4], args[5], args[6], args[7]],
                      [args[8], args[9], args[10], args[11]],
                      [args[12], args[13], args[14], args[15]]]

    def __repr__(self):
        return '<Matrix4x4>\n{0}\n{1}\n{2}\n{3}'.format(self.m[0], self.m[1], self.m[2], self.m[3])

    def __getitem__(self, item):
        return self.m[item]

    def __add__(self, other):
        if isinstance(other, Matrix4x4):
            return Matrix4x4(self[0][0] + other[0][0],
                             self[0][1] + other[0][1],
                             self[0][2] + other[0][2],
                             self[0][3] + other[0][3],
                             self[1][0] + other[1][0],
                             self[1][1] + other[1][1],
                             self[1][2] + other[1][2],
                             self[1][3] + other[1][3],
                             self[2][0] + other[2][0],
                             self[2][1] + other[2][1],
                             self[2][2] + other[2][2],
                             self[2][3] + other[2][3],
                             self[3][0] + other[3][0],
                             self[3][1] + other[3][1],
                             self[3][2] + other[3][2],
                             self[3][3] + other[3][3])

    def __sub__(self, other):
        if isinstance(other, Matrix4x4):
            m = other * -1
            return self + m

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Matrix4x4(self[0][0] * other,
                             self[0][1] * other,
                             self[0][2] * other,
                             self[0][3] * other,
                             self[1][0] * other,
                             self[1][1] * other,
                             self[1][2] * other,
                             self[1][3] * other,
                             self[2][0] * other,
                             self[2][1] * other,
                             self[2][2] * other,
                             self[2][3] * other,
                             self[3][0] * other,
                             self[3][1] * other,
                             self[3][2] * other,
                             self[3][3] * other)

        if isinstance(other, Matrix4x4):
            m = Matrix4x4(1)
            for i in range(4):
                for j in range(4):
                    m[i][j] = self[i][0] * other[0][j] + \
                              self[i][1] * other[1][j] + \
                              self[i][2] * other[2][j] + \
                              self[i][3] * other[3][j]
            return m

        if isinstance(other, Point3):
            pass

        if isinstance(other, Vector3):
            pass

    def __eq__(self, other):
        if not isinstance(other, Matrix4x4):
            return False
        for i in range(4):
            for j in range(4):
                if self[i][j] != other[i][j]:
                    return False
        return True

    def solve_linear_system_2x2(self):
        pass

    def transpose(self, other):
        pass

    def inverse(self, other):
        pass
