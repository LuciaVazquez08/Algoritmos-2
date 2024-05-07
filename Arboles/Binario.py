from typing import Generic, Optional, TypeVar

T = TypeVar('T')

class NodoAB(Generic[T]):
    def __init__(
        self, 
        dato: T, 
        si: Optional["ArbolBinario[T]"] = None, 
        sd: Optional["ArbolBinario[T]"] = None
    ):
        self.dato: T = dato
        self.si: ArbolBinario[T] = ArbolBinario() if si is None else si
        self.sd: ArbolBinario[T] = ArbolBinario() if sd is None else sd

class ArbolBinario(Generic[T]):
    def __init__(self):
        self.raiz: Optional[NodoAB[T]] = None

    def es_vacio(self) -> bool:
        return self.raiz is None
    
    def si(self) -> "ArbolBinario[T]":
        if self.es_vacio():
            raise TypeError('Arbol Vacio') 
        return self.raiz.si

    def sd(self) -> "ArbolBinario[T]":
        if self.es_vacio():
            raise TypeError('Arbol Vacio') 
        return self.raiz.sd

    def dato(self) -> T:
        if self.es_vacio():
            raise TypeError('Arbol Vacio') 
        return self.raiz.dato

    def es_hoja(self) -> bool:
        return not self.es_vacio() and self.si().es_vacio() and self.sd().es_vacio()
    
    def insertar_si(self, si: "ArbolBinario[T]"):
        if self.es_vacio():
            raise TypeError('Arbol Vacio') 
        self.raiz.si = si

    def insertar_sd(self, sd: "ArbolBinario[T]"):
        if self.es_vacio():
            raise TypeError('Arbol Vacio') 
        self.raiz.sd = sd

    def altura(self) -> int:
        if self.es_vacio():
            return 0
        else:
            return 1 + max(self.si().altura(), self.sd().altura())
        
    def __len__(self) -> int:
        if self.es_vacio():
            return 0
        else:
            return 1 + len(self.si()) + len(self.sd())
    
    def bfs(self):
        def recorrer(q: list[ArbolBinario[T]]):
            if q:
                actual = q.pop()                # desencolar árbol visitado
                if not actual.es_vacio():
                    visitar(actual.dato()) # type: ignore
                    q.insert(0, actual.si())    # encolar subárbol izquierdo
                    q.insert(0, actual.sd())    # encolar subárbol derecho
                recorrer(q, recorrido) # type: ignore
                
        q: list[ArbolBinario[T]] = []
        q.insert(0, self)                       # encolar raíz
        recorrer(q)

# Ejercicio: Nivel de un nodo
# Implementar una operación que, dado un valor o etiqueta de un nodo, devuelva cuál es el nivel del mismo dentro del árbol.

# Ejercicio: Igualdad en árboles
# Implementar la operación __eq__() para un árbol que permita identificar si dos árboles son iguales.

# Ejercicio: Recorrido guiado
# Implementar una función recursiva que, dado un árbol binario y una lista de instrucciones ('izquierda' o 'derecha') que conforma un camino guiado comenzando desde el nodo raíz, devuelva el contenido del nodo que sea accesible utilizando el camino guiado.

# Ejercicio: Generar listas de recorridos
# Adaptar los diversos recorridos de árbol binario propuestos de forma que la operación de visita sea la de incoporar el dato del nodo en una lista, lo cual nos permita reflejar el orden del recorrido en una estructura lineal list[T].

# Ejercicio: Recorrido bottom-up
# Implementar un algoritmo que devuelva el recorrido de un árbol desde las hojas hasta la raíz, y de izquierda a derecha. El primer nodo del recorrido debería ser la hoja más profunda y a la derecha, y último nodo debería ser el nodo raíz.

# Ejercicio: Eliminar recursión en DFS
# Implementar una versión de recorrido DFS inorder con recursión de cola.