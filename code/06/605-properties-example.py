# encoding: UTF-8

class CajaFuerte(object):

    def __init__(self, PIN):
        self.PIN = PIN

    @property
    def PIN(self):
        print "Enviando copia a la NSA..."
        return self._PIN

    @PIN.setter
    def PIN(self, PIN):
        if len(str(PIN)) != 4:
            raise ValueError("'PIN' ha de tener cuatro dígitos")
        self._PIN = PIN

hucha = CajaFuerte(7814)
print "PIN:", hucha.PIN
hucha.PIN = 880

