from notificacion import Notificacion
from Cola import Queue
from Pila import Pila

cola_notificaciones = Queue()

notificacion1 = Notificacion(15, 00,"Facebook", "tiene una solicitud de mensaje")
notificacion2 = Notificacion(17, 00, "Instagram", "Notificaciones sin ver")
notificacion3 = Notificacion(17, 30, "Facebook", "mensaje2")
notificacion4 = Notificacion(12, 00, "Twitter", "nuevo seguidor: Python")
notificacion5 = Notificacion(15, 00, "Instagram", "mensaje3")

cola_notificaciones.arrive(notificacion1)
cola_notificaciones.arrive(notificacion2)
cola_notificaciones.arrive(notificacion3)
cola_notificaciones.arrive(notificacion4)
cola_notificaciones.arrive(notificacion5)

def eliminar_notificaciones(cola = Queue(), app = str):
    on_front = Notificacion()

    for i in range (cola.size()):
        on_front = cola.on_front()
        if on_front.app == app:
            cola.attention()
        else:
            cola.move_to_end()
    if cola:
        return cola
    else:
        return "sin notificaciones"

eliminar_notificaciones(cola_notificaciones, "Facebook")

for i in range(cola_notificaciones.size()):
    on_top = Notificacion()
    on_top = cola_notificaciones.on_front()
    print(f"[{on_top.hora}: {on_top.min}] {on_top.app} : {on_top.msj}")
    cola_notificaciones.move_to_end()


def buscar_mensaje (cola = Queue(),app=str, palabra = str):
    cola_aux = Queue()
    for i in range (cola.size()):
        on_front = cola.on_front()

        if (palabra in on_front.msj) and (on_front.app == app):
            cola_aux.arrive(on_front)
        cola.move_to_end()
    return cola_aux

por_aplicacion = "Twitter"
por_mensaje = "Python"

filtrar_cola = buscar_mensaje(cola_notificaciones, por_aplicacion, por_mensaje)

print()
print ("filtro aplicado:")
for i in range (filtrar_cola.size()):
    on_top= filtrar_cola.move_to_end()
    print(f"[{on_top.hora} : {on_top.min}] {on_top.app}: {on_top.msj}")

def almacenar_segun_hora (cola= Queue(), desde_hora =int,desde_min=int, hasta_hora=int, hasta_min = int):
    on_top= Notificacion()
    pila = Pila()
    tiempo_inicio = desde_hora * 60 + desde_min
    tiempo_fin = hasta_hora * 60 + hasta_min

    for i in range(cola.size()):
        on_top = cola.on_front()
        tiempo_notif = on_top.hora * 60 + on_top.min
        cola.move_to_end()
        if tiempo_notif>tiempo_inicio and tiempo_notif<tiempo_fin:
            pila.push(on_top)
    return pila

hora_inicial =11
min_inicial =43
hora_final = 15
min_final = 57

filtro_hora = almacenar_segun_hora(cola_notificaciones,hora_inicial, min_inicial, hora_final, min_final)

print()
print(f"{filtro_hora.size()} notificaciones entre las {hora_inicial}:{min_inicial} y las {hora_final}: {min_inicial}:")
while filtro_hora.size() > 0:
    on_top = filtro_hora.on_top()
    print(f"[{on_top.hora} : {on_top.min}] {on_top.app}: {on_top.msj}")
    filtro_hora.pop()




