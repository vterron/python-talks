# encoding: UTF-8

class Triangulo(object):

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    @property
    def area(self):
        return (self.base * self.altura) / 2.0

    def __str__(self):
        msg = "Triángulo de base {0} y altura {1}"
        return msg.format(self.base, self.altura)

t = Triangulo(2, 3)
print str(t)
print "Área:", t.area
