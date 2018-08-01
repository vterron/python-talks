import collections
import math

_Punto = collections.namedtuple("_Punto", "x y z")
class Punto(_Punto):

    def distancia(self, other):
        """ Distancia entre dos puntos. """
        x_axis = (self.x - other.x) ** 2
        y_axis = (self.y - other.y) ** 2
        z_axis = (self.z - other.z) ** 2
        return math.sqrt(x_axis + y_axis + z_axis)

print "MRO:", Punto.__mro__
