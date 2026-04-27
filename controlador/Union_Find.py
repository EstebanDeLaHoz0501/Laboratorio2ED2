class UnionFind:
    #todo esto es para el MST 
    
    def __init__(self, n:int):

        self.parent = list(range(n)) #cada entrada n es la raiz del n esimo objeto
        self.rank = [0] * n #la altura de cada "arbol" que representan los conjuntos
    
    def find(self, objetivo):

        root = self.parent[objetivo]
        if self.parent[ root] !=  root: #si root no es el root de su conjunto ...

            self.parent[ objetivo] = self.find(root)  
            return self.parent[objetivo]
        
        return root
    
    def union(self, m_grupo_1, m_grupo_2):
        m1, m2 = self.find( m_grupo_1), self.find(m_grupo_2) #raiz de los grupos de m1 y m2
        if m1 == m2:
            return False #no se pueden unir
        
       #se mete el grupo mas chiquito al mas grande, si son de igual tamaño da igual el otden
        if self.rank[m1] < self.rank[m2]: #
            self.parent[m1] = m2

        elif self.rank[m2] < self.rank[m1]:
            self.parent[m2] = m1
        else:
            self.parent[m2] = m1 
            self.rank[m1] += 1
        return True