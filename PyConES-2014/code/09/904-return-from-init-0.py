class Pesos(tuple):

    @property
    def total(self):
        return sum(self)

    def __init__(self, valores):
        valores = [v / self.total for v in valores]
        self = super(Pesos, self).__init__(valores)
        return self

p = Pesos([2, 1]) # sigue sin funcionar
print p
