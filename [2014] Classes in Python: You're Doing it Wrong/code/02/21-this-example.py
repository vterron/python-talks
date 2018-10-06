class Punto(object):
    def __init__(this, x, y):
        this.x = x
        this.y = y

class Circulo(Punto):
    def __init__(this, x, y, radio):
        super(Circulo, this).__init__(x, y)
        this.radio = radio

c = Circulo(2, 7, 5)
print "x:", c.x
print "y:", c.y
print "r:", c.radio

