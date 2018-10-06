import math

class Punto(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otro):
        x_delta = self.x - otro.x
        y_delta = self.y - otro.y
        return math.sqrt(x_delta ** 2 + y_delta ** 2)

c1 = Punto(8, 1)
c2 = Punto(4, 7)
print c1.distancia(c2)
