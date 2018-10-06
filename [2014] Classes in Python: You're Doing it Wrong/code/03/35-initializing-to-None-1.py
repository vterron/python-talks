class Circulo(object):

    x = 0
    y = 0
    radio = 0

    def __init__(self, x, y, radio):
        self.x = x
        self.y = y
        self.raido = radio # typo!

c = Circulo(1, 3, 4)
print "Radio:", c.radio
