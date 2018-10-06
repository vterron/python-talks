from __future__ import division

class Pesos(tuple):

    def __new__(cls, valores):
        total = sum(valores)
        valores = [v / total for v in valores]
        return super(Pesos, cls).__new__(valores)

    def __init__(self, valores):
        pass

print Pesos([2, 1, 3])
