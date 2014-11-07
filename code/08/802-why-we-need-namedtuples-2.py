class Punto(object):
    """ Punto (x, y, z) en un espacio tridimensional. """

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        args = (type(self).__name__, self.x, self.y, self.z)
        return "{0}({1}, {2}, {3})".format(*args)

p1 = Punto(3, 1, 5)
p2 = Punto(3, 1, 5)

print p1, "==", p2, "?"
print p1 == p2
