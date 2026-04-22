import folium
from flights.dataLoader import cargar_datos
from flights.dataLoader import listaAdyacencia
from collections import deque

#carga el mapa
#LOS METODOS DE GRAFOS VAN EN OPERACIONES GRAFO, NO CAMBIE ESTE ARCHIVO PQ HAY FUNCIONES QUE NO ENTIENDO
#Y NO LAS QUIERO DAÑAR
aereopuertos = cargar_datos("flights/flights_final.csv")
adyacencia = listaAdyacencia("flights/flights_final.csv")


mapa = folium.Map(location=[0, 0], zoom_start=2)

#que quede casi vacio el main
for aeropuerto in aereopuertos.values():
    folium.Marker(
        location=[aeropuerto.lat, aeropuerto.lon],
        popup=aeropuerto.code
    ).add_to(mapa)

mapa.save("mapa.html")

def dfsComponentes(n, visitados, componente):
    visitados.add(n)
    componente.append(n)
    for vecino, i in adyacencia[n]:
        if vecino not in visitados:
            dfsComponentes(vecino, visitados, componente)


def componentes_conexas(adyacencia):
    visitados = set()
    componentes = []

    for nodo in adyacencia:
        if nodo not in visitados:
            componente = []
            dfsComponentes(nodo, visitados, componente)

            componentes.append(componente)

    return componentes

listaComponentes = componentes_conexas(adyacencia)

if len(listaComponentes) == 0:
    print("El grafo esta vacio")
elif len(listaComponentes) == 1:
    print("El grafo es conexo")
else:
    print("El grafo no es conexo y tiene", len(listaComponentes)
          , "componentes conexas, a continuación la cantidad de vertices"
          "de cada componente conexa.")
    for componente in listaComponentes:
        print(len(componente))

#esto es para la componente conexa con mas vertices
#
# mayor = len(listaComponentes[0])
# for i in listaComponentes:
#     if mayor < len(listaComponentes[i]):  
#         mayor = len(listaComponentes[i])

def mayorCompConex():
    mayor = max(listaComponentes, key=len)
    mayorComp = {}
    for n in mayor:
        vecinosEnMayor = []
        for v,p in adyacencia[n]:
            if(v in mayor):
                vecinosEnMayor.append((v,p))
        mayorComp[n]=vecinosEnMayor
    return mayorComp


def bipartito(adyacencia):
    conjuntos = {}  
    for nodo in adyacencia:
        if nodo not in conjuntos:
            
            cola = deque([nodo])
            conjuntos[nodo] = 0

            while cola:
                actual = cola.popleft()

                for vecino, i in adyacencia[actual]:
                    if vecino not in conjuntos:
                        #asigna el color opuesto
                        conjuntos[vecino] = 1 - conjuntos[actual]
                        cola.append(vecino)
                    else:
                        if conjuntos[vecino] == conjuntos[actual]:
                            return False

    return True

if len(listaComponentes) == 0:
    print("El grafo esta vacio")
elif len(listaComponentes) == 1:
    print("El grafo es conexo")
    if(bipartito(adyacencia)==True):
        print("Y es bipartito")
    else:
        print("Pero no es bipartito")
else:
    print("El grafo no es conexo y tiene", len(listaComponentes)
          , "componentes conexas, a continuación la cantidad de vertices"
          "de cada componente conexa.")
    for componente in listaComponentes:
        print(len(componente))
    if(bipartito(mayorCompConex())==True):
        print("Y su mayor componente es bipartita")
    else:
        print("Y su mayor componente no es bipartita")