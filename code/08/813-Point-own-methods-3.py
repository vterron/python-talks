import collections
import math

class Punto(collections.namedtuple("_Punto", "x y z")):

    def distancia(self, other):
        """ Distancia entre dos puntos. """
        x_axis = (self.x - other.x) ** 2
        y_axis = (self.y - other.y) ** 2
        z_axis = (self.z - other.z) ** 2
        return math.sqrt(x_axis + y_axis + z_axis)

    def to_zero(self):
        """ Distancia al origen de coordenadas. """
        cls = type(self)
        origen = cls(0, 0, 0)
        return self.distancia(origen)

p = Punto(3, 4, 2)
print "Distancia:", p.to_zero()
