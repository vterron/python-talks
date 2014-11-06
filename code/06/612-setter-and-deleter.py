class CajaFuerte(object):

    def __init__(self, PIN):
        self.PIN = PIN

    def set_PIN(self, PIN):
        print "Enviando copia a la NSA..."
        self._PIN = PIN

    def delete_PIN(self):
        self.PIN = None

    PIN = property(fset=set_PIN, fdel=delete_PIN)

hucha = CajaFuerte(7814)
del hucha.PIN
print "PIN:", hucha.PIN

