import mathTools
import math

a = mathTools.Point3(5.65, 0, 0)
b = mathTools.Point3(1, 0, 0)

print a.lerp(0.5, b)
print math.ceil(a)


