class Persona(object):

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.__edad = edad

p = Persona("Juan Pedro", 23)
print "Edad:", p._Persona__edad
