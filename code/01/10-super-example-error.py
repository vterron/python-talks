# encoding: UTF-8

class ListaLogger(list):
    def append(self, x):
        print "Intentando añadir", x
        self.append(x)

numeros = ListaLogger()
numeros.append(7)
