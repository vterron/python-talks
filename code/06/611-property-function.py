class CajaFuerte(object):
    def __init__(self, PIN):
        self.PIN = PIN

    def get_PIN(self):
        return self._PIN

    def set_PIN(self, PIN):
        print "Enviando copia a la NSA..."
        self._PIN = PIN

    def delete_PIN(self):
        self.PIN = None

    PIN = property(get_PIN, set_PIN, delete_PIN, "La clave de acceso")

hucha = CajaFuerte(7814)
print "PIN:", hucha.PIN
print "Docstring:", CajaFuerte.PIN.__doc__
