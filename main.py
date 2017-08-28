import mathTools


p1 = mathTools.Point3(-1, -1, -1)
p2 = mathTools.Point3(0, 0, 0)
p3 = mathTools.Point3(1, 1, 1)
p4 = mathTools.Point3(2, 2, 2)

bb1 = mathTools.Bounds3(p1, p2)
bb2 = mathTools.Bounds3(p3, p4)

v1 = mathTools.Vector3(1,1,1)

print bb1.surface_area()