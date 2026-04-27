import folium
import heapq
from modelos import lista_adj_aeropuertos
from modelos import lista_info_aeropuertos

from collections import deque
from controlador import Union_Find #para el kruskal

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
    

    
    #PUNTO 3
    #esta funcion es para que sirva el kruskal
    def get_aristas(self, diccionario_adjacencia: dict):

        aristas = []
        visitados = set()
        
        #al parecer .items() se demora menos que .keys()???? que loquera
        for vertice, vecinos in diccionario_adjacencia.items():
            for vecino, distancia in vecinos:

                #organiza los vertices para ver si ya tenemos la arista guardada
                edge = tuple(sorted([vertice,vecino]))
                if edge not in visitados:
                    visitados.add(edge)
                    aristas.append((distancia, vertice, vecino))
        #aaam
        return aristas  # Aristas guardadas como (peso, nodo1, nodo2)
    
    
    #MST, ahora con kruskal
    def kruskal_peso(self, diccionario_adjacencia: dict):


        edges = self.get_aristas(diccionario_adjacencia) #lista de tuplas (peso, nodo1, nodo2)
        edges.sort(key=lambda x: x[0])  # las sortea por el peso de su index 0 (el peso)
        
        # Diccionario con todos los las mismas claves, con valories de 0 hasta el tamaño-1
        node_a_idx = {node: i for i, node in enumerate(diccionario_adjacencia.keys())}

        uf = Union_Find(len(node_a_idx))
        
        peso_mst  = 0
        num_visitadas = 0
        
        for peso_arista, nodo1, nodo2 in edges: 
            if uf.union(node_a_idx[nodo1], node_a_idx[nodo2]):
                peso_mst += peso_arista
                num_visitadas += 1
                if num_visitadas == len(diccionario_adjacencia) - 1:
                    break  # se acabo
        
        return peso_mst
        
      
    #regresa el peso de los componentes en una lista en orden de los componentes conexos
    def mst_de_los_componentes(self):
        componentes = self.componentes_conexas()
        mst_componentes = []

        for componente in componentes:
            mst_componentes.append(self.kruskal_peso(componente))
        
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




