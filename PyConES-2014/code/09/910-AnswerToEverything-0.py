# encoding: UTF-8

class AnswerToEverything(object):

    def __new__(cls, x):
        print "¡En __new__()!"
        obj = super(AnswerToEverything, cls).__new__(cls)
        return obj

    def __init__(self, valor):
        print "¡En __init__()!"
        self.valor = 42 # ignora 'valor'

    def __str__(self):
        return str(self.valor)

respuesta = AnswerToEverything(23)
print "Respuesta:", respuesta

