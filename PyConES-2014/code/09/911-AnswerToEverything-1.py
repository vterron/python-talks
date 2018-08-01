# encoding: UTF-8

class AnswerToEverything(object):

    def __new__(cls, x):
        print "¡En __new__()!"
        return 42

    def __init__(self, valor):
        # nada que hacer aquí
        print "¡En __init__()!"

respuesta = AnswerToEverything(23)
print "Respuesta:", respuesta

