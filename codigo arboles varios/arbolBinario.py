from typing import Optional, Generic, TypeVar, Callable, Any
from functools import wraps

T = TypeVar("T")

class Nodo(Generic[T]):
    def __init__(self, dato: T):
        self.dato = dato
        self.si: ArbolBinario[T] = ArbolBinario()
        self.sd: ArbolBinario[T] = ArbolBinario()

class ArbolBinario(Generic[T]):
    def __init__(self):
        self.raiz: Optional[Nodo[T]] = None
    
    class Decoradores:
        @classmethod
        def validar_no_vacio(cls, func: Callable[..., Any]) -> Callable[..., Any]:
            @wraps(func)
            def wrapper(self, *args, **kwargs) -> Any:
                if self.es_vacio():
                    raise TypeError("Arbol vacio")
                return func(self, *args, **kwargs)

            return wrapper

    @staticmethod
    def crear_nodo(dato: T) -> "ArbolBinario[T]":
        nuevo = ArbolBinario()
        nuevo.raiz = Nodo(dato)
        return nuevo
    def es_vacio(self) -> bool:
        return self.raiz is None
    @Decoradores.validar_no_vacio
    def si(self) -> "ArbolBinario[T]":
        return self.raiz.si
    @Decoradores.validar_no_vacio
    def sd(self) -> "ArbolBinario[T]":
        return self.raiz.sd
    @Decoradores.validar_no_vacio
    def dato(self) -> T:
        return self.raiz.dato
    @Decoradores.validar_no_vacio
    def insertar_si(self, si: "ArbolBinario[T]"):
        self.raiz.si = si
    @Decoradores.validar_no_vacio
    def insertar_sd(self, sd: "ArbolBinario[T]"):
        self.raiz.sd = sd
    
    def set_raiz(self, dato: T):
        self.raiz = Nodo(dato)
    
    def altura(self) -> int:
        if self.es_vacio():
            return 0
        else:
            return 1 + max(self.si().altura(), self.sd().altura())
    
    def preorder(self):
        if self.es_vacio():
            return []
        return [self.dato()] + self.si().preorder() + self.sd().preorder()
    
    def inorder(self):
        if self.es_vacio():
            return []
        return self.si().preorder() + [self.dato()] + self.sd().preorder()
    
    def postorder(self):
        if self.es_vacio():
            return []
        return self.si().preorder() + self.sd().preorder() + [self.dato()]

    def __str__(self) -> str:
        def recorrer(t: ArbolBinario[T], nivel: int) -> str:
            if t.es_vacio():
                return ""
            else:
                tab = "." * 2 * nivel
                tab += str(t.dato()) + "\n"
                tab += recorrer(t.si(), nivel+1)
                tab += recorrer(t.sd(), nivel+1)
                return tab
        return recorrer(self, 0)

    def __len__(self) -> int:
        if self.es_vacio():
            return 0
        return 1 + len(self.si()) + len(self.sd())
    
    def copy(self) -> "ArbolBinario[T]":
        if self.es_vacio():
            return ArbolBinario[T]()
        nuevo = ArbolBinario.crear_nodo(self.dato())
        nuevo.insertar_si(self.si().copy())
        nuevo.insertar_sd(self.sd().copy())
        return nuevo
    
    def bfs(self) -> int:
        def recorrido(q: list[ArbolBinario[T]], camino: list[T]) -> list[T]:
            if len(q) == 0:
                return camino
            actual = q.pop(0)
            if not actual.es_vacio():
                camino.append(actual.dato())
                q.append(actual.si())
                q.append(actual.sd())
            
            return recorrido(q, camino)
        return recorrido([self], [])

if __name__ == "__main__":
    t  = ArbolBinario.crear_nodo(1)
    n2 = ArbolBinario.crear_nodo(2)
    n3 = ArbolBinario.crear_nodo(3)
    n4 = ArbolBinario.crear_nodo(4)
    n5 = ArbolBinario.crear_nodo(5)
    n6 = ArbolBinario.crear_nodo(6)
    n7 = ArbolBinario.crear_nodo(7)
    n8 = ArbolBinario.crear_nodo(8)
    n9 = ArbolBinario.crear_nodo(9)

    t.insertar_si(n2)
    t.insertar_sd(n3)

    n2.insertar_si(n4)
    n2.insertar_sd(n5)

    n3.insertar_si(n6)
    n3.insertar_sd(n7)

    n4.insertar_si(n8)
    n4.insertar_sd(n9)

    print(t.bfs())