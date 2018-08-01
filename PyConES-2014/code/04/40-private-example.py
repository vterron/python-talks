class Persona(object):

    def __init__(self, nombre, secreto):
        self.nombre = nombre
        self._secreto = secreto

p = Persona("Raquel", "Prefiere Perl")
print "Nombre:", p.nombre
print "Secreto:", p._secreto
