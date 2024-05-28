#Representacion por lista de adyacencia
from typing import Generic, Optional, TypeVar

T = TypeVar("T")

class Nodo(Generic[T]):
    def __init__(self, valor: T) -> None:
        self.valor = valor
        self.aristas: set[Grafo[T]] = set()

    def __str__(self) -> str:
        return f"Nodo({self.valor})"

# Grafo de adyacencia
class Grafo(Generic[T]):
    def __init__(self) -> None:
        self.nodos: set[Nodo[T]] = set()
    
    def crear_grafo(valor: T) -> "Grafo[T]":
        nuevo = Grafo()
        nuevo.nodos.add(Nodo(valor))
        return nuevo
    
    def agregar_nodo(self, valor: T) -> None:
        if valor not in self.nodos:
            nuevo_nodo = Nodo(valor)
            self.nodos[valor] = nuevo_nodo
            return nuevo_nodo

    def agregar_arista(self, arista: tuple[T, T]) -> None:
        if arista[0] in self.nodos:
            if arista[1] in self.nodos[arista[0]]
        

    def eliminar_nodo():
        pass

    def eliminar_arista():
        pass

    def es_vecino_de():
        pass

    def vecinos_de():
        pass
    
    def __str__(self) -> str:
        txt = ""
        for nodo in self.nodos:
            txt += str(nodo) + "\n"
        return txt


if __name__ == "__main__":
    g = Grafo.crear_grafo(1)
    print(g)