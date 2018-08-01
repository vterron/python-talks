# encoding: UTF-8
import math

class Circulo(object):

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

c = Circulo(1)
print "Radio:", c.radio
print "Área:", c.area()
c.radio = 2
print "Radio:", c.radio
print "Área:", c.area()

