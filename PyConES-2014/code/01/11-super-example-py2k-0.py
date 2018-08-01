# encoding: UTF-8

class ListaLogger(list):
    def append(self, x):
        print "Añadiendo", x, "a la lista (¡ahora sí!)"
        super(ListaLogger, self).append(x)

numeros = ListaLogger()
numeros.append(7)
print numeros
