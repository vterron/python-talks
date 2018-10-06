# encoding: UTF-8

class Triangulo(object):

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    @property
    def area(self):
        return (self.base * self.altura) / 2.0

t = Triangulo(2, 3)
print "Triángulo:", t
print "Área:", t.area
