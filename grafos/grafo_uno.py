# Representacion por conjunto de nodos y aristas
from typing import Generic, Optional, TypeVar

T = TypeVar("T")

# 1 -> [2]
# 2 -> [1, 3]
# 4 -> [3]

class Grafo(Generic[T]):
    def __init__(self) -> None:
        self.vertices: set[T] = set()
        self.aristas: set[tuple[T, T]] = set()

    def agregar_nodo(self, valor: T):
        self.vertices.add(valor)
    
    def agregar_arista(self, arista: tuple[T, T]):
        self.aristas.add(arista) 

    def eliminar_nodo(self, valor: T):
        self.vertices.remove(valor)
        for arista in self.aristas.copy():
            if arista[0] == valor or arista[1] == valor:
                self.aristas.remove(arista)

    def eliminar_arista(self, arista: tuple[T, T]):
        for e in self.aristas.copy():
            if e == arista:
                self.aristas.remove(arista)
            elif (e[0] == arista[1] and e[1] == arista[0]):
                self.aristas.remove(e)

    def es_vecino(self, valor1: T, valor2: T) -> bool:
        for e in self.aristas:
            if e == (valor1, valor2) or e == (valor2, valor1):
                return True
        return False

    def vecinos_de(self, valor: T) -> list[T]:
        vecinos = []
        for e in self.aristas:
            if e[0] == valor:
                vecinos.append(e[1])
            elif e[1] == valor:
                vecinos.append(e[0])
        return vecinos
    
    def dfs(self) -> list[T]:
        visitados = set()
        recorrido = []
        
        def dfs_interna(nodo: T):
            if nodo not in visitados:
                visitados.add(nodo)
                recorrido.append(nodo)
                for vecino in self.vecinos_de(nodo):
                    dfs_interna(vecino)

        return dfs_interna(self.vertices[0])
    
    def bfs(self) -> list[T]:
        def bfs_interna(q,recorrido) -> list[T]:
            if not q:
                return recorrido
            actual = q.pop(0)
            if actual not in recorrido:
                recorrido.append(actual)
                for v in self.vecinos_de(actual):
                    q.append(v)
                return bfs_interna(q,recorrido)
        q=[self.vertices[0]]
        return bfs_interna(q,[])
    

def main():
    g = Grafo()
    g.agregar_nodo(3)
    g.agregar_nodo(2)
    g.agregar_nodo(1)
    g.agregar_nodo(4)
    g.agregar_arista((2,3))
    g.agregar_arista((1,2))
    g.agregar_arista((3,4))
    g.eliminar_arista((2,1))
    print(g.vertices)
    print(g.aristas)
    

    

if __name__ == "__main__":
    main()