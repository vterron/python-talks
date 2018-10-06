class C(object):
    pass

def init_x(clase, valor):
    clase.x = valor

C.init_x = init_x

c = C()
c.init_x(23)
print c.x
