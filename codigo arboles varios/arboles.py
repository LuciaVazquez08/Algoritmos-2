from abc import abstractmethod, ABC
from typing import Any, Generic, TypeVar, Optional

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, valor: T):
        self.valor = valor
        self.left: Optional['Node[T]'] = None
        self.right: Optional['Node[T]'] = None
    
    def __repr__(self) -> str:
        return f"Node(valor={self.valor}, left={repr(self.left)}, right={repr(self.right)})"

    def copy(self) -> 'Node[T]':
        copia = Node(self.valor)
        if self.left is not None:
            copia.left = self.left.copy()
        if self.right is not None:
            copia.right = self.right.copy()
        return copia


class ArbolABC(Generic[T], ABC):
    "Clase abstracta Arbol"
    def __init__(self, nodo: Optional[Node[T]] | Optional[T] = None):
        if nodo is None:
            self.root: Optional[Node[T]] = None
        elif isinstance(nodo, Node):
            self.root = nodo.copy()
        else:
            self.root = Node(nodo)
    
    def cant_nodos(self) -> int:
        def interno(nodo: Optional[Node[T]]) -> int:
            if nodo is None:
                return 0
            return 1 + interno(nodo.left) + interno(nodo.right)
        
        return interno(self.root)

    def in_orden(self) -> list[T]:
        def interna(nodo: Optional[Node[T]], valores: list[T]):
            if nodo is None:
                return
            interna(nodo.left, valores)
            valores.append(nodo.valor)
            interna(nodo.right, valores)

        valores: list[T] = []
        interna(self.root, valores)
        return valores

    def __str__(self) -> str:
        return str(self.in_orden())

    def altura(self) -> int:
        def interna(nodo: Optional[Node[T]]) -> int:
            if nodo is None:
                return 0
            altura_left = interna(nodo.left)
            altura_right = interna(nodo.right)
            return 1 + max(altura_left, altura_right)
        return interna(self.root)

    def valores_nivel(self, nivel: int) -> list[T]:
        def interna(nodo: Optional[Node[T]], nivel: int, nivel_actual: int, valores: list[T]):
            if nodo is None:
                return
            if nivel_actual == nivel:
                valores.append(nodo.valor)
                return
            interna(nodo.left, nivel, nivel_actual + 1, valores)
            interna(nodo.right, nivel, nivel_actual + 1, valores)

        valores: list[T] = []
        interna(self.root, nivel, 1, valores)
        return valores

    def hojas(self) -> list[T]:
        def interna(nodo: Optional[Node[T]], valores: list[T]):
            if nodo is None:
                return
            if nodo.left is None and nodo.right is None:
                valores.append(nodo.valor)
                return
            interna(nodo.left, valores)
            interna(nodo.right, valores)

        valores: list[T] = []
        interna(self.root, valores)
        return valores

    def altura_minima(self) -> int:
        def interna(nodo: Optional[Node[T]]) -> int:
            if nodo is None:
                return 0
            altura_left = interna(nodo.left)
            altura_right = interna(nodo.right)
            return 1 + min(altura_left, altura_right)

        return interna(self.root)
    
    def nivel(self, valor: T) -> int:
        def interna(nodo: Optional[Node[T]], valor: T, nivel_actual: int) -> int:
            if nodo is None:
                return 0
            if nodo.valor == valor:
                return nivel_actual
            nivel_left = interna(nodo.left, valor, nivel_actual + 1)
            if nivel_left != 0:
                return nivel_left
            return interna(nodo.right, valor, nivel_actual + 1)

        nivel = interna(self.root, valor, 1)
        return nivel if nivel != 0 else self.altura() + 1
    
    @abstractmethod
    def insertar(self, valor: T) -> None:
        pass


class ArbolBusquedaBinaria(ArbolABC[T]):
    def insertar(self, valor: T):
        def interna(nodo: Node[T], valor: T):
            if nodo.valor > valor:
                if nodo.left is None:
                    nodo.left = Node(valor)
                else:
                    interna(nodo.left, valor)
            else:
                if nodo.right is None:
                    nodo.right = Node(valor)
                else:
                    interna(nodo.right, valor)

        if self.root is None:
            self.root = Node(valor)
        else:
            interna(self.root, valor)

    def minimo(self) -> T:
        nodo = self.root
        if nodo is None:
            raise ValueError("El árbol está vacío")
        while nodo.left is not None:
            nodo = nodo.left
        return nodo.valor

    def maximo(self) -> T:
        nodo = self.root
        if nodo is None:
            raise ValueError("El árbol está vacío")
        while nodo.right is not None:
            nodo = nodo.right
        return nodo.valor

    def contiene(self, valor: T) -> bool:
        def interna(nodo: Optional[Node[T]], valor: T) -> bool:
            if nodo is None:
                return False
            if nodo.valor == valor:
                return True
            elif nodo.valor > valor:
                return interna(nodo.left, valor)
            else:
                return interna(nodo.right, valor)
        return interna(self.root, valor)

    def path(self, valor: T) -> list[T]:
        def interna(nodo: Optional[Node[T]], valor: T, camino: list[T]) -> Optional[list[T]]:
            if nodo is None:
                return None
            camino.append(nodo.valor)
            if nodo.valor == valor:
                return camino
            elif nodo.valor > valor:
                return interna(nodo.left, valor, camino)
            else:
                return interna(nodo.right, valor, camino)
        
        camino = interna(self.root, valor, [])
        if camino is None:
            raise ValueError(f"Valor {valor} no encontrado en el árbol")
        return camino


class ArbolBinario(ArbolABC[T]):
    def insertar(self, valor: T) -> None:
        def interna(nodo: Node[T], valor: T):
            if nodo.left is None:
                nodo.left = Node(valor)
                return
            elif nodo.right is None:
                nodo.right = Node(valor)
                return
            
            left = ArbolBinario(nodo.left)
            right = ArbolBinario(nodo.right)
            if left.altura_minima() > right.altura_minima():
                interna(nodo.right, valor)
            else:
                interna(nodo.left, valor)

        if self.root is None:
            self.root = Node(valor)
        else:
            interna(self.root, valor)

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, ArbolABC):
            raise ValueError(f"No puede comparar {value.__class__} con {self.__class__}")
        if self.altura() != value.altura() or self.altura_minima() != value.altura_minima():
            return False
        
        def interna(nodo_self: Optional[Node[T]], nodo_otro: Optional[Node[T]], iguales: list[bool]):
            if nodo_self is None and nodo_otro is None:
                iguales.append(True)
                return
            if nodo_self is not None and nodo_otro is None:
                iguales.append(False)
                return
            if nodo_self is None and nodo_otro is not None:
                iguales.append(False)
                return
            if nodo_self.valor != nodo_otro.valor:
                iguales.append(False)
                return
            iguales.append(True)
            interna(nodo_self.left, nodo_otro.left, iguales)
            interna(nodo_self.right, nodo_otro.right, iguales)
        
        iguales: list[bool] = []
        interna(self.root, value.root, iguales)
        return all(iguales)

    def acceder(self, movs: list[bool]) -> T:
        if len(movs) >= self.altura():
            raise IndexError("No puede moverse más veces que la altura del árbol")
        
        def interna(nodo: Optional[Node[T]], movs: list[bool]) -> T:
            if nodo is None:
                raise IndexError("No existe esa dirección en el árbol")
            if len(movs) == 0:
                return nodo.valor
            if movs[0] == 0:
                return interna(nodo.left, movs[1:])
            else:
                return interna(nodo.right, movs[1:])
        
        return interna(self.root, movs)

    def pertenece(self, valor: T) -> bool:
        def interna(nodo: Optional[Node[T]], valor: T) -> bool:
            if nodo is None:
                return False
            if nodo.valor == valor:
                return True
            return interna(nodo.left, valor) or interna(nodo.right, valor)
        
        return interna(self.root, valor)


def main():
    arbol = ArbolBinario[int]()
    n = 6
    for i in range(n):
        arbol.insertar(i + 1)

    print(arbol)
    arbol.root.left.left = None
    print(arbol)
    arbol.insertar(4)
    print(arbol)


if __name__ == "__main__":
    main()
