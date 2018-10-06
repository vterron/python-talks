class Punto(object):
    """ Punto (x, y, z) en un espacio tridimensional. """

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        args = (type(self).__name__, self.x, self.y, self.z)
        return "{0}({1}, {2}, {3})".format(*args)

    def __eq__(self, other):
        return self.x == other.x and \
               self.y == other.y and \
               self.z == other.z

