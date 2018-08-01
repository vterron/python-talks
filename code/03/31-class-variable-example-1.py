class T1000(object):
    jefe = "Skynet"

robot1 = T1000()
robot2 = T1000()

# Esto no cambia T1000.jefe
robot2.jefe = "James Cameron"

print robot1.jefe
print robot2.jefe
