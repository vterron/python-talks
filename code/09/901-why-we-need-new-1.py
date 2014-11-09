class Pesos(tuple):
    pass

p = Pesos([0.50, 0.75, 0.25])
print "Pesos:", p
print "Total:", sum(p)
