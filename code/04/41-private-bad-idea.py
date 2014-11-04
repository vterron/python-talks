class Persona(object):

    def __init__(self, nombre, secreto):
        self.nombre = nombre
        self._secreto = secreto

p = Persona("Raquel", "Prefiere Perl")
print "Secreto:", p._secreto

p._secreto = "Programa en Notepad"
print "Secreto:", p._secreto
