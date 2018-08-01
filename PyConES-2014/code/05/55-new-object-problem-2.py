# encoding: UTF-8
class Ameba(object):

    def __init__(self, nombre):
        self.nombre = nombre

    def fision(self):
        cls1 = self.__class__
        h1 = cls1("Primogénito")
        # O también...
        cls2 = type(self)
        h2 = cls2("Benjamín")
        return h1, h2

ameba = Ameba("Foraminifera")
hijo1, hijo2 = ameba.fision()
print "Hijo 1:", hijo1.nombre
print "Hijo 2:", hijo2.nombre
