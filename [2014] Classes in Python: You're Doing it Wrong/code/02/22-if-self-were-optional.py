import math

class Punto(object):
    def __init__(x, y):
        self.x = x
        self.y = y

    def distancia(otro):
        x_delta = self.x - otro.x
        y_delta = self.y - otro.y
        return math.sqrt(x_delta ** 2 + y_delta ** 2)

