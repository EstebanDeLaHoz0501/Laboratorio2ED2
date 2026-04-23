import folium
import heapq
from modelos import lista_adj_aeropuertos
from modelos import lista_info_aeropuertos

from collections import deque

#puse las funciones aca para no tener todo en el main :/

class operaciones_grafo:
    def __init__(self, ruta_csv: str):

        self.adyacencia = lista_adj_aeropuertos.lista_adj_airport(ruta_csv).lista_adj
        self.aereopuertos = lista_info_aeropuertos.lista_info_airport(ruta_csv).datos


    #obtiene los ids de los vertices que estan dentro del componente conexo
    def dfs_componentes(self, vertice: int, visitados, ids_componente: list):

        visitados.add(vertice)
        ids_componente.append(vertice)

        #puesto asi porque adyacencia es un diccionario 
        for vertices_adyacentes in self.adyacencia[vertice]:
            if vertices_adyacentes[0] not in visitados:
                self.dfs_componentes(vertices_adyacentes[0], visitados, ids_componente)


    def componentes_conexas(self):
        visitados = set()
        #lista de diccionarios
        componentes = []

        for nodo in self.adyacencia:
            if nodo not in visitados:
                ids_del_componente = []
                self.dfs_componentes(nodo, visitados, ids_del_componente)
                
                #crea un diccionario con los aeropuertos del componente conexo para poder hacer el mismo algoritmo de mst
                dict_componentes = {k: self.adyacencia[k] for k in ids_del_componente}
                componentes.append(dict_componentes)

        return componentes


    # def mayor_Comp_Conex(self): 
    #         componentes = self.lista_componentes()
    #         mayor = []
    #         for componente in componentes:
    #             if len(componente) > len(mayor):
    #                 mayor = componente

    #         return mayor

#   Rescaté la función mayorCompConex del main, debe devolver un diccionario, pues la función bipartito
#   trabaja sobre listas de adyacencia, y necesita revisar si la mayor componente conexa es
#   bipartita, la funcion mayorCompConex devuelve la lista de adyacencia de dicha componente

    def mayorCompConex(self):
        mayor = max(self.componentes_conexas(), key=len)
        mayorComp = {}
        for n in mayor:
            vecinosEnMayor = []
            for v,p in self.adyacencia[n]:
                if(v in mayor):
                    vecinosEnMayor.append((v,p))
            mayorComp[n]=vecinosEnMayor
        return mayorComp

    def bipartito(self, adyacencia):
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
    
    #creo que esta listo
    def peso_arbol_expansion_minima(self, lista_adyacencia: dict):
        
        peso_arbol = 0
        numero_vertices = len(self.adyacencia)
        visitados = set()

        primer_clave_lista  = next(iter(lista_adyacencia))

        #[id aeropuerto, distancia]
        minHeap = [[0,0]]

        #mq no se hayan visitado todos
        while len(visitados) < numero_vertices:
            codigo, distancia = heapq.heappop(minHeap)

            #si ya se visito, se salta
            if codigo in visitados:
                continue

            peso_arbol += distancia

            visitados.add(codigo)

            #por cada combo [codigo, distancia] en el valor del aeropuerto se meten los que no han pasado
            for vecino, cost_vecino in self.adyacencia[codigo]:
                if vecino not in visitados:
                    heapq.heappush(minHeap, [vecino, cost_vecino])

        return peso_arbol

        
    #regresa el peso de los componentes en una lista en orden de los componentes conexos
    def mst_de_los_componentes(self):
        componentes = self.lista_componentes()
        mst_componentes = []

        for componente in componentes:
            mst_componentes.append(self.peso_arbol_expansion_minima(componente))
        
        return mst_componentes
    
    def Dijkstra(self, Ori):
        distancias = {nodo:float('inf') for nodo in self.adyacencia}
        distancias[Ori]=0
        visitados = set()
        padre = {nodo:None for nodo in self.adyacencia}

        while len(visitados)<len(self.adyacencia):
            nodoActual = None
            menorDistancia = float('inf')
            for nodo in self.adyacencia:
                if nodo not in visitados and distancias[nodo]<menorDistancia:
                    menorDistancia = distancias[nodo]
                    nodoActual = nodo
            
            if nodoActual == None:
                break

            visitados.add(nodoActual)
            for vecino, peso in self.adyacencia[nodoActual]:
                nueva_dist = distancias[nodoActual] + peso

                if nueva_dist < distancias[vecino]:
                    distancias[vecino] = nueva_dist
                    padre[vecino] = nodoActual

        return distancias, padre
    
    def caminoEntreNodos(self, Ori, Des):
        distancia, predecesor = self.Dijkstra(Ori)
        lista = []
        actual = Des
        while(actual is not None):
            lista.append(actual)
            actual = predecesor[actual]

        listaCoo = []
        for aero in lista:
            listaCoo.append((self.aereopuertos[aero].lat,
                     self.aereopuertos[aero].lon))
        return distancia[Des], listaCoo, lista




