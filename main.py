# abandon all hope, ye who enter here -luna
import folium
from modelos.lista_info_aeropuertos import cargar_datos
from modelos.lista_adj_aeropuertos import lista_adyacencia
from collections import deque
from controlador.Operaciones_Grafo import operaciones_grafo
from Mapa.mapa import punto5
from Mapa.mapa import punto6
from Mapa.mapa import adyacencia
from Mapa.mapa import Opgrafo
from punto4 import punto_4

# Opgrafo = operaciones_grafo("flights/flights_final.csv")


# aereopuertos = cargar_datos("flights/flights_final.csv")
# adyacencia = lista_adyacencia("flights/flights_final.csv")
listaComponentes = Opgrafo.componentes_conexas()


#print("soy el peso del arbol", Opgrafo.peso_arbol_expansion_minima(adyacencia))

#Este bloque prueba el punto 1 y 2 del lab



def Menu1():
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

def Menu2():
    if len(listaComponentes) == 0:
        print("El grafo esta vacio")
    elif len(listaComponentes) == 1:
        print("El grafo es conexo")
        if(Opgrafo.bipartito(adyacencia)==True):
            print("Y es bipartito")
        else:
            print("Pero no es bipartito")
    else:
        print("El grafo no es conexo y tiene", len(listaComponentes)
            , "componentes conexas,")
        if(Opgrafo.bipartito(Opgrafo.mayorCompConex())==True):
            print("y su mayor componente es bipartita")
        else:
            print("y su mayor componente no es bipartita")

def Menu3():
    print("soy el peso del arbol", Opgrafo.peso_arbol_expansion_minima(adyacencia))

def Menu4():
    print("Ingresa el codigo del aeropuerto de origen")
    Ori = input("").strip().upper()
    punto_4(Ori)

def Menu5():
    print("Ingresa el codigo del aeropuerto de origen")
    Ori = input("").strip().upper()
    print("Ingresa el codigo del aeropuerto destino")
    Des = input("").strip().upper()
    if(not punto5(Des,Ori)):
        print("Verifica el codigo de origen y destino")
    else:
        print("Exito!")

def Menu6():
    punto6()
    print("Exito!")
    
def Menu7():
    print("Adios!")

def choice(opcion):
    casos = {
        "1":Menu1,
        "2":Menu2,
        "3":Menu3,
        "4":Menu4,
        "5":Menu5,
        "6":Menu6,
        "7":Menu7
    }
    funcion = casos.get(opcion)
    if funcion:
        funcion()
        return True
    else:
        print("Verifique el dato introducido")
        return False


print("Bienvenido al menú de nuestro laboratorio 2")
opcion = 0
while opcion != "7":
    print("A continuación, digite el número correspondiente a la funcionalidad que desee")
    print("1. Verifique si el grafo es conexo")
    print("2. Verifique si el grafo es bipartito")
    print("3. Determine el peso del arbol de expansión minima")
    print("4. Determine los 10 caminos mas cortos dado un nodo")
    print("5. Muestre el camino mínimo entre 2 nodos y sus intermedios")
    print("6. Muestre todos los aeropuertos")
    print("7. Salir")
    while True:
        opcion = input("").strip().upper()
        if choice(opcion):
                break
    



