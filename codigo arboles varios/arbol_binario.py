from typing import TypeVar, Generic, Optional

T = TypeVar("T")

class NodoAB(Generic[T]):
    def __init__(self, dato: T, si: "Optional[ArbolBinario[T]]" = None, sd: "Optional[ArbolBinario[T]]" = None):
        self.dato = dato
        self.si: ArbolBinario[T] = ArbolBinario() if si is None else si
        self.sd: ArbolBinario[T] = ArbolBinario() if sd is None else sd

    def __str__(self) -> str:
        return str(self.dato)

class ArbolBinario(Generic[T]):
    def __init__(self):
        self.raiz: Optional[NodoAB[T]] = None

    def es_vacio(self) -> bool:
        return self.raiz is None
    
    @staticmethod
    def crear_nodo(
        dato: T) -> "ArbolBinario[T]":
        t = ArbolBinario()
        t.raiz = NodoAB(dato)
        return t
    
    def set_raiz(self, nodo: NodoAB[T]):
        self.raiz = nodo

    def insertar_si(self, si: "ArbolBinario[T]"):
        if self.es_vacio():
            raise TypeError('Arbol Vacio') 
        self.raiz.si = si

    def insertar_sd(self, sd: "ArbolBinario[T]"):
        if self.es_vacio():
            raise TypeError('Arbol Vacio') 
        self.raiz.sd = sd

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