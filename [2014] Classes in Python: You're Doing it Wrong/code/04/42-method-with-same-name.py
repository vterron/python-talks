# encoding: UTF-8

class Persona(object):

    # Máxima edad confesada en público
    MAXIMA_EDAD = 35

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self._edad = edad

    def edad(self):
        return min(self._edad, self.MAXIMA_EDAD)

p = Persona("Juan Pedro", 41)
print "Nombre:", p.nombre
print "Edad:", p.edad()
