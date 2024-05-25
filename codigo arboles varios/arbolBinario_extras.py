from typing import Optional, Callable, Any, TypeVar, List
from functools import wraps

T = TypeVar('T')

class Node:
    def __init__(self, valor: T):
        self.valor = valor
        self.left = ArbolBinario[T]()
        self.right = ArbolBinario[T]()

class ArbolBinario:
    class Decoradores:
        @classmethod
        def validar_no_vacio(cls, func: Callable[..., Any]) -> Callable[..., Any]:
            @wraps(func)
            def wrapper(self: "ArbolBinario[T]", *args, **kwargs):
                if self.es_vacio():
                    raise TypeError("El árbol está vacío")
                return func(self, *args, **kwargs)
            return wrapper

    def __init__(self):
        self.root: Optional[Node[T]] = None

    def es_vacio(self) -> bool:
        return self.root is None

    @staticmethod
    def crear_nodo(valor: T) -> "ArbolBinario[T]":
        arbol = ArbolBinario[T]()
        arbol.root = Node[T](valor)
        return arbol

    @Decoradores.validar_no_vacio
    def left(self) -> "ArbolBinario[T]":
        return self.root.left

    @Decoradores.validar_no_vacio
    def right(self) -> "ArbolBinario[T]":
        return self.root.right

    @Decoradores.validar_no_vacio
    def valor(self) -> T:
        return self.root.valor

    @Decoradores.validar_no_vacio
    def insertar_left(self, arbol: "ArbolBinario[T]") -> None:
        self.root.left = arbol

    @Decoradores.validar_no_vacio
    def insertar_right(self, arbol: "ArbolBinario[T]") -> None:
        self.root.right = arbol

    def set_root(self, valor: T) -> None:
        self.root = Node[T](valor)

    def inorden(self) -> List[T]:
        if self.es_vacio():
            return []
        return self.left().inorden() + [self.valor()] + self.right().inorden()

    def preorden(self) -> List[T]:
        if self.es_vacio():
            return []
        return [self.valor()] + self.left().preorden() + self.right().preorden()

    def postorden(self) -> List[T]:
        if self.es_vacio():
            return []
        return self.left().postorden() + self.right().postorden() + [self.valor()]

    def __str__(self) -> str:
        def recorrer(t: ArbolBinario[T], nivel: int) -> str:
            if t.es_vacio():
                return ""
            tab = "." * 2 * nivel
            tab += str(t.valor()) + "\n"
            tab += recorrer(t.left(), nivel + 1)
            tab += recorrer(t.right(), nivel + 1)
            return tab

        return recorrer(self, 0)

    def bfs(self) -> List[T]:
        def recorrer(q: List[ArbolBinario[T]], camino: List[T]) -> List[T]:
            if not q:
                return camino
            actual = q.pop(0)
            if not actual.es_vacio():
                camino.append(actual.valor())
                q.append(actual.left())
                q.append(actual.right())
            return recorrer(q, camino)

        return recorrer([self], [])

    def altura(self) -> int:
        if self.es_vacio():
            return 0
        return 1 + max(self.left().altura(), self.right().altura())

    def altura_minima(self) -> int:
        if self.es_vacio():
            return 0
        return 1 + min(self.left().altura_minima(), self.right().altura_minima())

    def insertar(self, valor: T) -> None:
        if self.es_vacio():
            self.root = Node[T](valor)
        else:
            if self.left().altura_minima() > self.right().altura_minima():
                self.right().insertar(valor)
            elif self.left().altura_minima() < self.right().altura_minima():
                self.left().insertar(valor)
            else:
                self.left().insertar(valor)

    def espejo(self) -> "ArbolBinario[T]":
        if self.es_vacio():
            return ArbolBinario[T]()
        copia = ArbolBinario.crear_nodo(self.valor())
        copia.insertar_left(self.right().espejo())
        copia.insertar_right(self.left().espejo())
        return copia

if __name__ == "__main__":
    def main():
        arbol = ArbolBinario[int]()
        n = 15
        for i in range(1, n + 1):
            arbol.insertar(i)

        print(arbol.bfs())
        print(arbol)
        espejo = arbol.espejo()
        print(espejo.bfs())
        print(espejo)

    main()
