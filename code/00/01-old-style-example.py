class Perro: # no heredamos de 'object'

    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

sargento = Perro("Stubby", "Bull Terrier", 9)
print "Clase:", sargento.__class__
print "Tipo:", type(sargento)
