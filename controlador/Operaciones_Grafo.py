import folium
import heapq
from modelos import lista_adj_aeropuertos
from modelos import lista_info_aeropuertos

from collections import deque

#puse las funciones aca para no tener todo en el main :/
class operaciones_grafo:
    def __init__(self, ruta_csv: str):

        self.aereopuertos = lista_adj_aeropuertos.lista_adj_airport(ruta_csv)
        self.adyacencia = lista_info_aeropuertos.lista_info_airport(ruta_csv)


    def mayor_CompConex():
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


    #no estoy segura de esto, habra que cambiarlo
    def arbol_expansion_minima(lista_adyacencia, punto_inicio: int):
        cola =[]

        #lista de los valores, todos inicializados como "infinito"
        key = [float("inf")]*lista_adyacencia.size()

        parent = [-1] * lista_adyacencia.size()

        #para tomar nota de los que ya estan en el arbol
        en_arbol = [False] * lista_adyacencia.size()

        heapq.heappush(cola, (0, punto_inicio))
        key[punto_inicio] = 0

        while cola:
                u = heapq.heappop(cola)[1]

                if en_arbol[u]:
                    continue
                
                #lo mete al arbol
                en_arbol[u] = True  

                # revisa los vertices adjacentes al vertice
                for v, peso in lista_adyacencia[u]:
                    # If v is not in MST and the weight of (u, v) is smaller than the current key of v
                    if not en_arbol[v] and key[v] > peso:

                        key[v] = peso
                        heapq.heappush(cola, (key[v], v))
                        parent[v] = u

    #regresa lista de componentes 
    def lista_componentes(lista_adyacencia):
        num_vectores = len(lista_adyacencia)
        visitados = [False] * num_vectores
        componentes = []

        for i in range(V):
            if not visitados[i]:
                componente = []
                dfs(lista_adyacencia, visitados, i, componente)
                componentes.append(componente)

        return componentes