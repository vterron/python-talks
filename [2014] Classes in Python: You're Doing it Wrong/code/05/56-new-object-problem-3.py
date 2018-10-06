# encoding: UTF-8
class Ameba:

    def __init__(self, nombre):
        self.nombre = nombre

    def fision(self):
        clase = type(self)
        print "Mi tipo es:", clase
        h1 = clase("Primogénito")
        h2 = clase("Benjamín")
        return h1, h2

ameba = Ameba("Foraminifera")
ameba.fision()

