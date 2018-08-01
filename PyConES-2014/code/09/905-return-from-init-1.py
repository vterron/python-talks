# encoding: UTF-8

class Pesos(tuple):

    @property
    def total(self):
        return sum(self)

    def __init__(self, valores):
        valores = [v / self.total for v in valores]
        return tuple(valores)

p = Pesos([2, 1]) # ¡tampoco!
print p
