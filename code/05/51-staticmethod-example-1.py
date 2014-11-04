class Calculadora(object):

    def __init__(self, nombre):
        self.nombre = nombre

    def modelo(self):
        return self.nombre

    @staticmethod
    def suma(x, y):
        return x + y

c = Calculadora("Multivac")
print c.modelo()
print c.suma(4, 8)
