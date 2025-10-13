from monticulo import HeapMax

trabajo_prioridad = HeapMax()

#A
trabajo_prioridad.arrive('Hugo', 1)
trabajo_prioridad.arrive('Nilda', 1)
trabajo_prioridad.arrive('Patricio', 1)

#B
trabajador = trabajo_prioridad.elements[0]
print(trabajador[1])
print()

#C
trabajo_prioridad.arrive("Laura", 2)
trabajo_prioridad.arrive('Bruno', 2)

#D
trabajo_prioridad.arrive('Carla', 3)

#E
trabajador = trabajo_prioridad.elements[0]
print(trabajador[1])
trabajador = trabajo_prioridad.elements[1]
print(trabajador[1])
print()

#F
trabajo_prioridad.arrive('Esteban', 1)
trabajo_prioridad.arrive('Bianca', 1)
trabajo_prioridad.arrive('Leandro', 3)

#G
while trabajo_prioridad.size()>0:
    print(trabajo_prioridad.attention())





