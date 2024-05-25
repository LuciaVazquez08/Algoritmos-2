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
    
    @staticmethod
    def crear_grafo(valor: T) -> "Grafo[T]":
        nuevo = Grafo()
        nuevo.nodos.add(Nodo(valor))
        return nuevo
    
    def __str__(self) -> str:
        txt = ""
        for nodo in self.nodos:
            txt += str(nodo) + "\n"
        return txt


if __name__ == "__main__":
    g = Grafo.crear_grafo(1)
    print(g)