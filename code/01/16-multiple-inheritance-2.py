# encoding: UTF-8

class Humano(object):
    def ataca(self):
        print "Puñetazo"

class Cyborg(Humano):
    def defiende(self):
        print "Armadura"

class Ninja(Humano):
    def ataca(self):
        print "Shuriken"

class T1000(Cyborg, Ninja):
    pass

robot = T1000()
robot.defiende()
robot.ataca()
