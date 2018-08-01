# encoding: UTF-8

class T1000(object):

    JEFE = "Skynet"

    def saluda_uno(self):
        print self.JEFE, "me envía a eliminarte"

    def saluda_dos(self):
        print T1000.JEFE, "me envía a eliminarte"

robot = T1000()
robot.saluda_uno()
robot.saluda_dos()

