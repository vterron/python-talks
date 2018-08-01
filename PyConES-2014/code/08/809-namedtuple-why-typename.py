import collections

cls = collections.namedtuple("Punto", "x y z")
print cls
print "Nombre:", cls.__name__

p = cls(4, 3, 8)
print p
