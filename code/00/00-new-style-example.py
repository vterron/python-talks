class Perro(object):

    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

mascota = Perro("Lassie", "Collie", 18)
print "Clase:", mascota.__class__
print "Tipo:", type(mascota)

