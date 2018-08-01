class Triangulo(object):

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def __repr__(self):
        clase = type(self).__name__
        msg = "{0}({1}, {2})"
        return msg.format(clase, self.base, self.altura)

t = Triangulo(2, 3)
print str(t)
print repr(t)
