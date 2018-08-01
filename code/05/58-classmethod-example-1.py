# encoding: UTF-8

class Ameba(object):

    def __init__(self, nombre):
        self.nombre = nombre

    def fision(self):
        cls = type(self)
        ascendencia = ", hijo de " + self.nombre
        h1 = cls("Primogénito" + ascendencia)
        h2 = cls("Benjamín" + ascendencia)
        return h1, h2

ameba = Ameba("Foraminifera")
hijo1, hijo2 = ameba.fision()
print "Hijo 1:", hijo1.nombre
print "Hijo 2:", hijo2.nombre
