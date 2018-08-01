import collections
Punto = collections.namedtuple("Punto", "x y z")

p = Punto(3, 1, 5)
print "x:", p.x
print "y:", p.y
print "z:", p.z

p2 = Punto(3, 1, 5)
print p2
print p == p2
