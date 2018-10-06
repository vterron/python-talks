# encoding: UTF-8

class Humano(object):
    def ataca(self):
        print "Puñetazo"

class Cyborg(Humano):
    def ataca(self):
        print "Láser"

class Ninja(Humano):
    def ataca(self):
        print "Shuriken"

class T1000(Cyborg, Ninja):
    def ataca(self, n):
        for _ in xrange(n):
            super(T1000, self).ataca()

print "MRO:", T1000.__mro__
robot = T1000()
robot.ataca(5)
