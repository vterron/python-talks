# encoding: UTF-8
class CajaFuerte(object):
    def __init__(self, PIN):
        self._PINs = []
        self.PIN = PIN

    @property
    def PIN(self):
        try:
            return self._PINs[-1]
        except IndexError:
            return None

    @PIN.setter
    def PIN(self, PIN):
        if len(str(PIN)) != 4:
            raise ValueError("'PIN' ha de tener cuatro dígitos")
        self._PINs.append(PIN)

    @PIN.deleter
    def PIN(self):
        del self._PINs[:]
