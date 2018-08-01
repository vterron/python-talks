import math

class Punto(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otro):
        x_delta = self.x - otro.x
        y_delta = self.y - otro.y
        return math.sqrt(x_delta ** 2 + y_delta ** 2)

c1 = Punto(4, 1.5)
c2 = Punto(3, 3.1)
print c1.distancia(c2) == Punto.distancia(c1, c2)
