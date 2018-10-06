# No podemos usar 'import' por los guiones
modulo = __import__("608-property-deleter")

hucha = modulo.CajaFuerte(7814)
print "PIN:", hucha.PIN
hucha.PIN = 8808
print "PIN:", hucha.PIN
print "Historial:", hucha._PINs
del hucha.PIN
print "PIN:", hucha.PIN
