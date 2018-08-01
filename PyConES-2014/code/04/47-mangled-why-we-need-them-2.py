class Habitacion(object):
    __PIN = 9348

class CamaraAcorazada(Habitacion):
    def __init__(self, PIN):
        self.__PIN = PIN

    def PIN1(self):
        return self._Habitacion__PIN

    def PIN2(self):
        return self.__PIN

p = CamaraAcorazada(2222)
print "PIN1:", p.PIN1()
print "PIN2:"; p.PIN2()
