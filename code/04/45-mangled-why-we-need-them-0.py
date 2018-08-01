class Habitacion(object):
    _PIN = 9348

class CamaraAcorazada(Habitacion):
    def __init__(self, PIN):
        self._PIN = PIN

p = CamaraAcorazada(2222)
print "PIN:", p._PIN # sobreescribe PIN de Habitacion
