# encoding: UTF-8

class Pesos(tuple):

    @property
    def total(self):
        return sum(self)

    def __init__(self, valores):
        valores = [v / self.total for v in valores]
        super(Pesos, self).__init__(valores)

p = Pesos([2, 1]) # [0.66, 0.33]... ¿no?
print p
