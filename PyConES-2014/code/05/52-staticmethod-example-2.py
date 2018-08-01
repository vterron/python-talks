class Calculadora(object):

    def __init__(self, nombre):
        self.nombre = nombre

    def modelo(self):
        return self.nombre

    @staticmethod
    def suma(x, y):
        return x + y

print Calculadora.suma(4, 8)
