from __future__ import division

class Pesos(tuple):

    def __new__(cls, valores):
        total = sum(valores)
        valores = (v / total for v in valores)
        return super(Pesos, cls).__new__(cls, valores)

    @property
    def total(self):
        return sum(self)

p = Pesos([2, 1, 3])
print "Pesos:", p
print "Total:", p.total
