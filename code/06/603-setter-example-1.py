# encoding: UTF-8
class Circulo(object):

    def __init__(self, radio):
        self._radio = radio

    def set_radio(self, radio):
        if radio < 0:
            raise ValueError("'radio' debe ser un número no negativo")
        self._radio = radio

c = Circulo(3.5)
print "Radio:", c._radio
c.set_radio(-2)
print "Radio:", c._radio
