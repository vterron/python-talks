PI = 3.141592653589793

class Circulo(object):
    def __init__(self, x, y, radio):
        self.x = x
        self.y = y
        self.radio = radio

    def area(self):
        return PI * (self.radio ** 2)

c = Circulo(0, 0, 4.5)
print "Pi:", c.area()
