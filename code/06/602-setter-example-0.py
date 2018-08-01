class Circulo(object):

    def __init__(self, radio):
        self.radio = radio

c = Circulo(13)
print "Radio:", c.radio
c.radio = -2
print "Radio:", c.radio

