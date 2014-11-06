# encoding: UTF-8
class Circulo(object):

    def __init__(self, radio):
        self.radio = radio

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def set_radio(self, radio):
        if radio < 0:
            raise ValueError("'radio' debe ser un número no negativo")
        self._radio = radio

c = Circulo(13)
print "Radio:", c.radio
