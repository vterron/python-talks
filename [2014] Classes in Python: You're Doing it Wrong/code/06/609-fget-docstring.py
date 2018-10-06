# encoding: UTF-8

import math

class Circulo(object):

    def __init__(self, radio):
        self.radio = radio

    @property
    def area(self):
        """Devuelve al área del círculo. """
        return math.pi * self.radio ** 2

c = Circulo(3.4)
print "Radio:", c.radio
print "Área:", c.area
print "Docstring:", Circulo.area.__doc__

