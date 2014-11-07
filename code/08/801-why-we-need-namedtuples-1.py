class Punto(object):
    """ Punto (x, y, z) en un espacio tridimensional. """

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

p = Punto(3, 1, 5)
print p
