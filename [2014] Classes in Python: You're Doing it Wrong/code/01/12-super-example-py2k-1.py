class Punto(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circulo(Punto):
    def __init__(self, x, y, radio):
        super(Circulo, self).__init__(x, y)
        self.radio = radio

c = Circulo(3, 4, 5.5)
print "x:", c.x
print "y:", c.y
print "r:", c.radio
