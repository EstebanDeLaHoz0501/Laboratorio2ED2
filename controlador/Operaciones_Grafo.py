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


    def mayor_Comp_Conex(self):
        componentes = self.lista_componentes()
        mayor = []
        for componente in componentes:
            if len(componente) > len(mayor):
                mayor = componente

        return mayor

    def bipartito(self):
        conjuntos = {}  
        for nodo in self.adyacencia:
            if nodo not in conjuntos:
                
                cola = deque([nodo])
                conjuntos[nodo] = 0

                while cola:
                    actual = cola.popleft()

                    for vecino, i in self.adyacencia[actual]:
                        if vecino not in conjuntos:
                            #asigna el color opuesto
                            conjuntos[vecino] = 1 - conjuntos[actual]
                            cola.append(vecino)
                        else:
                            if conjuntos[vecino] == conjuntos[actual]:
                                return False

        return True

    #dfs para lo del arbol
    def dfs_aux(self, visitado:list, s, resultado:list, adjacencia: list):
        visitado[s] = True
        resultado.append(s)

        for i in adjacencia[s]:
            if not visitado[i]:
                self.dfs_aux(visitado,i, resultado, adjacencia)
        pass
    
    def dfs(self):
        visitado = [False]*len(self.adyacencia)
        resultado = []

        self.dfs_aux(visitado, 0, resultado, self.adyacencia)

        return resultado
    
    #no estoy segura de esto, habra que cambiarlo
    def arbol_expansion_minima(self, punto_inicio: int):
        cola =[]

        #lista de los valores, todos inicializados como "infinito"
        key = [float("inf")]*len(self.adyacencia)

        parent = [-1] * self.adyacencia.size()

        #para tomar nota de los que ya estan en el arbol
        en_arbol = [False] * self.adyacencia.size()

        heapq.heappush(cola, (0, punto_inicio))
        key[punto_inicio] = 0

        while cola:
                u = heapq.heappop(cola)[1]

                if en_arbol[u]:
                    continue
                
                #lo mete al arbol
                en_arbol[u] = True  

                # NO entendi como se organizo el peso en la lista, hay que cambiar eso
                for v, peso in self.adyacencia[u]:
                    # If v is not in MST and the weight of (u, v) is smaller than the current key of v
                    if not en_arbol[v] and key[v] > peso:

                        key[v] = peso
                        heapq.heappush(cola, (key[v], v))
                        parent[v] = u

    #regresa lista de componentes 
    def lista_componentes(self):
        num_vectores = len(self.adyacencia)
        visitados = [False] * num_vectores
        componentes = []

        for i in range(num_vectores):
            if not visitados[i]:
                componente = []
                dfs(self.adyacencia, visitados, i, componente)
                componentes.append(componente)

        return componentes
    
    def mst_de_los_componentes(self):
        pass