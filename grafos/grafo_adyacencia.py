"""
Conjunto de Nodos y Aristas
Nodos: lista, tupla, etc.
Aristas: lista de tuplas

Implementar Grafo Simple

Se puede crear Grafo Vacio

- agregar_nodo
- agregar arista
- eliminar_nodo
- eliminar_arista
- existe_conexion
- es_vecino_de
- vecinos_de

"""
from typing import Generic, TypeVar, Optional
T = TypeVar('T')

class GrafoAdyacencia(Generic[T]):
    def __init__(self, vertices: set[T]=set(),aristas: dict[T : set[T] ]= {}) -> None:
        self.vertices = vertices
        self.aristas = aristas

    def agregar_nodo(self,nodo:T) -> None:
        self.vertices.add(nodo)
        self.aristas[nodo] = set()

    def agregar_arista(self,arista:tuple[T]) -> None:
        self.aristas[arista[0]].add(arista[1])
        self.aristas[arista[1]].add(arista[0])

    def eliminar_nodo(self,nodo:T) -> None:
        self.vertices.discard(nodo)

    def eliminar_arista(self,arista:tuple[T]) -> None:
        self.aristas[arista[0]].discard(arista[1])
        self.aristas[arista[1]].discard(arista[0])

    def es_vecino_de(self,nodoA:T,nodoB:T) -> bool:
        return nodoB in self.aristas[nodoA]
    
    def vecinos_de(self,nodo:T) -> list[T]:
        return self.aristas[nodo]
    
    def __str__(self) -> str:
        return f"Vertices = {self.vertices} \n Aristas = {self.aristas}"