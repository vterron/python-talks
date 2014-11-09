class Pesos(tuple):

    @property
    def total(self):
        return sum(self)

    def __init__(self, valores):
        if sum(self) != 1:
            msg = "la suma de los pesos ha de ser uno"
            raise ValueError(msg)

p1 = Pesos([0.25, 0.75])
print "Pesos 1:", p1

print
p2 = Pesos([0.50, 0.75, 0.25]) # ValueError
