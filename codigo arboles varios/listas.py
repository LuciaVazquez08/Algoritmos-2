from typing import TypeVar, Generic, TypeAlias, Optional
from copy import copy
T = TypeVar('T')
ListaGenerica: TypeAlias = "Lista[T]"

class Nodo(Generic[T]):
    def __init__(self, dato: T, sig: Optional[ListaGenerica] = None):
        self.dato = dato
        if sig is None:
            self.sig= Lista()
        else:
            self.sig = sig

class Lista(Generic[T]):
    def __init__(self):
        self._head: Optional[Nodo[T]] = None
    
    def copy(self) -> ListaGenerica:
        if self.es_vacia():
            return Lista()
        else:
            parcial = self._head.sig.copy()
            actual = Lista()
            actual._head = Nodo(copy(self._head.dato), parcial)
            return actual
    
    def tail(self) -> ListaGenerica:
        if self.es_vacia():
            raise IndexError('lista vacia')
        else:
            return self._head.sig.copy()
    
    def insertar(self, dato: T):
        actual = copy(self)
        self._head = Nodo(dato, actual)
    
    def es_vacia(self) -> bool:
        return self._head is None

    def head(self) -> T:
        if self.es_vacia():
            raise IndexError('lista vacia')
        else:
            return self._head.dato
    
    def __len__(self):
        if self.es_vacia():
            return 0
        else:
            return 1 + self.tail().__len__()
    
    def inv_lista_iter(self):
        cop = self.copy()
        new = Lista()
        while not cop.es_vacia():
            new.insertar(cop.head())
            cop = cop.tail()
        return new
        
    def inv_lista_cola(self):
        new = Lista()
        def mini(ori: Lista, rev: Lista):
            if not ori.es_vacia():
                elem = ori.head()
                rev.insertar(elem)
                mini(ori.tail(), rev)

        rev = Lista()
        mini(self, rev)
        return rev

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        def internal(lista: ListaGenerica):
            if lista.es_vacia():
                return ""
            return f"{lista.head()} {internal(lista.tail())}"
        return f"[{internal(self)}]"
    
    def __iter__(self):
        c = self._head
        while c is not None:
            yield c.dato
            c = c.sig._head
        return StopIteration()

lisa = Lista()
lisa.insertar(3)
lisa.insertar(2)
lisa.insertar(1)

print(lisa.inv_lista_cola())
for i in lisa:
    print(i)