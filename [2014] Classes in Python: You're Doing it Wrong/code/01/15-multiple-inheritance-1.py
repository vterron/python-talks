# encoding: UTF-8

class Humano(object):
    def ataca(self):
        print "Puñetazo"

class Cyborg(Humano):
    pass

class Ninja(Humano):
    def ataca(self):
        print "Shuriken"

class T1000(Cyborg, Ninja):
    def ataca(self, n):
        for _ in xrange(n):
            super(T1000, self).ataca()

robot = T1000()
robot.ataca(5)
