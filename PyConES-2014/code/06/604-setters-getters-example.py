# encoding: UTF-8

class CajaFuerte(object):

    def __init__(self, PIN):
        self._PIN = PIN

    def get_PIN(self):
        print "Enviando copia a la NSA..."
        return self._PIN

hucha = CajaFuerte(7821)
print "PIN:", hucha.get_PIN()
