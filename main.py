import folium
from modelos.lista_info_aeropuertos import cargar_datos
from modelos.lista_adj_aeropuertos import lista_adyacencia
from collections import deque
from controlador.Operaciones_Grafo import operaciones_grafo
from Mapa.mapa import punto5
Opgrafo = operaciones_grafo("flights/flights_final.csv")

aereopuertos = cargar_datos("flights/flights_final.csv")
adyacencia = lista_adyacencia("flights/flights_final.csv")
listaComponentes = Opgrafo.componentes_conexas()


punto5("DFW", "TYN")






#print("soy el peso del arbol", Opgrafo.peso_arbol_expansion_minima(adyacencia))


#Este bloque prueba el punto 1 y 2 del lab

# if len(listaComponentes) == 0:
#     print("El grafo esta vacio")
# elif len(listaComponentes) == 1:
#     print("El grafo es conexo")
#     if(Opgrafo.bipartito(adyacencia)==True):
#         print("Y es bipartito")
#     else:
#         print("Pero no es bipartito")
# else:
#     print("El grafo no es conexo y tiene", len(listaComponentes)
#           , "componentes conexas, a continuación la cantidad de vertices"
#           "de cada componente conexa.")
#     for componente in listaComponentes:
#         print(len(componente))
#     if(Opgrafo.bipartito(Opgrafo.mayorCompConex())==True):
#         print("Y su mayor componente es bipartita")
#     else:
#         print("Y su mayor componente no es bipartita")

