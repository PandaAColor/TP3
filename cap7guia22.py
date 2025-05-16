from Cola import Queue
from personaje import Personaje

cola_pjs = Queue()

pj1 = Personaje("Carol Danvers", "Capitana Marvel", "F")
pj2 = Personaje("Scott Lang", "Ant-Man", "M")
pj3 = Personaje("Peter Parker", "Spiderman", "M")
pj4 = Personaje("Snombre4", "supernombre4", "F")

cola_pjs.arrive(pj1)
cola_pjs.arrive(pj2)
cola_pjs.arrive(pj3)
cola_pjs.arrive(pj4)

def filtrar_por_supernombre(cola = Queue(), nombre = str):
    personaje = Personaje()
    encontrado = False
    for i in range (cola.size()):
        personaje = cola.on_front()
        if personaje.snombre == nombre:
            encontrado = True
            return f"{personaje.nombre} es {nombre}"
        cola.move_to_end()
    if encontrado == False:
        return "no se encuntra"
    
buscar_supernombre = "Capitana Marvel"

filtrar_supernombre = filtrar_por_supernombre(cola_pjs, buscar_supernombre)

print(filtrar_supernombre)
print()

def filtrar_por_genero(cola = Queue(), genero = str):
    lista_buscados = []
    personaje = Personaje()
    for i in range (cola.size()):
        personaje = cola.on_front()
        if personaje.genero == genero:
            lista_buscados.append(f"nombre: {personaje.nombre}, superhéroe: {personaje.snombre}")
        cola.move_to_end()
    if len(lista_buscados)>0:
        return lista_buscados
    else:
        return "no encontrado"

buscar_genero = "F"

busco_genero = filtrar_por_genero(cola_pjs, buscar_genero)

for personaje in busco_genero:
    print("-", personaje)

buscar_genero= "M"

busco_genero = filtrar_por_genero(cola_pjs, buscar_genero)
print()
for personaje in busco_genero:
    print("-", personaje)

print()

def filtrar_por_nombre(cola=Queue(), nombre = str):
    on_front = Personaje()

    for i in range(cola.size()):
        on_front = cola.on_front()
        encontrado = False
        if on_front.nombre == nombre:
            encontrado = True
            return on_front.snombre
        cola.move_to_end()
    if encontrado == False:
        return "no se encontró"

nombre_a_buscar = "Scott Lang"
buscar_nombre = filtrar_por_nombre(cola_pjs, nombre_a_buscar)

print(f"{nombre_a_buscar}, superhéroe: {buscar_nombre}")

nombre_a_buscar = "Carol Danvers"
buscar_nombre = filtrar_por_nombre(cola_pjs, nombre_a_buscar)

print(f"{nombre_a_buscar}, superhéroe: {buscar_nombre}")
print()

def filtrar_por_inicial (cola = Queue(), inicial=str):
    lista_personajes = []
    on_front = Personaje()

    for i in range (cola.size()):
        on_front = cola.on_front()
        if inicial in on_front.nombre or inicial in on_front.snombre:
            lista_personajes.append(f"nombre: {on_front.nombre}, nombre de superhéroe: {on_front.snombre}, género: {on_front.genero}")
        cola.move_to_end()
    if len(lista_personajes)>0:
        return lista_personajes
    else:
        return "no encontrado"
    
inicial_a_buscar= "S"

buscador_por_inicial= filtrar_por_inicial(cola_pjs, inicial_a_buscar)

for personaje in buscador_por_inicial:
    print(personaje)