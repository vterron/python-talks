import collections

import math

Punto = collections.namedtuple("Punto", "x y z")
class Punto(Punto):

    def distancia(self, other):
        """ Distancia entre dos puntos. """
        x_axis = (self.x - other.x) ** 2
        y_axis = (self.y - other.y) ** 2
        z_axis = (self.z - other.z) ** 2
        return math.sqrt(x_axis + y_axis + z_axis)

p1 = Punto(3, 1, 5)
p2 = Punto(5, 2, 7)
print "Distancia:", p1.distancia(p2)
print
print "MRO:", Punto.__mro__
