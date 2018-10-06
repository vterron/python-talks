# encoding: UTF-8

class Ameba(object):

    def __init__(self, nombre):
        self.nombre = nombre

    def fision(self):
        h1 = Ameba("Primogénito")
        h2 = Ameba("Benjamín")
        return h1, h2

class AmebaCyborg(Ameba):
    pass

ameba = AmebaCyborg("Foraminifera T-800")
hijo1, hijo2 = ameba.fision()
print "Hijo 1 es", type(hijo1)
print "Hijo 2 es", type(hijo2)
