# encoding: UTF-8

import math

class Circulo(object):

    def __init__(self, radio):
        self.radio = radio

    @property
    def area(self):
        return math.pi * self.radio ** 2

c = Circulo(1.5)
print "Área:", c.area
del c.area
