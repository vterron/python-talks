import collections

Punto = collections.namedtuple("Punto", "x y z")
p = Punto(8, 1, 3)
print p._asdict()

for atributo, valor in p._asdict().items():
    print atributo, "->", valor

