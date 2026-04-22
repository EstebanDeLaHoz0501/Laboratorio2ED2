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


    def dfs_componentes(self, vertice, visitados, componente):
        visitados.add(vertice)
        componente.append(vertice)
        #puesto asi porque adyacencia es un diccionario 
        for vecino, i in self.adyacencia[vertice]:
            if vecino not in visitados:
                self.dfs_componentes(vecino, visitados, componente)


    def componentes_conexas(self):
        visitados = set()
        componentes = []

        for nodo in self.adyacencia:
            if nodo not in visitados:
                componente = []
                self.dfs_componentes(nodo, visitados, componente)

                componentes.append(componente)

        return componentes


    def mayor_Comp_Conex(self): 
            componentes = self.lista_componentes()
            mayor = []
            for componente in componentes:
                if len(componente) > len(mayor):
                    mayor = componente

            return mayor

    def es_bipartito(self):
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
    def dfs_aux(self, visitado:list, s, resultado:dict, adjacencia:dict):
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
    def peso_arbol_expansion_minima(self, clave_inicial: int):
        peso_arbol = 0
        numero_vertices = len(self.adyacencia)
        visitados = set()
        #[punto, costo]
        minHeap = [[0,0]]

        while len(visitados) < numero_vertices:
            codigo, distancia = heapq.heappop(minHeap)
            if codigo in visitados:
                continue
            res += distancia

            visitados.add(codigo)

            for vecino, cost_vecino in self.adyacencia[codigo]:
                if vecino not in visitados:
                    heapq.heappush(minHeap, [vecino, cost_vecino])

        return res

        pass

    
    
    def mst_de_los_componentes(self):
        componentes = self.lista_componentes()
        mst_componentes = []

        for componente in componentes:
            arbol = self.arbol_expansion_minima
        pass