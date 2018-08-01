# encoding: UTF-8

import collections

Punto = collections.namedtuple("Punto", "x y z")

p = Punto(4, 3, 7)
print "x:", p.x
print "y:", p[1]
print "z:", p[-1]
print "Tamaño:", len(p)

