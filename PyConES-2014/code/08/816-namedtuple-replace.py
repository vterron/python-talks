import collections

Punto = collections.namedtuple("Punto", "x y z")
p1 = Punto(8, 1, 3)
print "Punto 1:", p1

p2 = p1._replace(x = 7)
print "Punto 2:", p2

p3 = p1._replace(y = p2.z, z = -1)
print "Punto 3:", p3

print
p3.x = 3 # AttributeError
