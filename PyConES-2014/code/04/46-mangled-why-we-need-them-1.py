class Habitacion(object):
    __PIN = 9348

class CamaraAcorazada(Habitacion):
    def __init__(self, PIN):
        self.__PIN = PIN

p = CamaraAcorazada(2222)
print "PIN1:", p._Habitacion__PIN
print "PIN2:", p._CamaraAcorazada__PIN
