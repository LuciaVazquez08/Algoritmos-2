from typing import Optional, Protocol, TypeVar
from Binario import ArbolBinario, NodoAB

class Comparable(Protocol):
    def __lt__(self: 'T', otro: 'T') -> bool: ...
    def __le__(self: 'T', otro: 'T') -> bool: ...
    def __gt__(self: 'T', otro: 'T') -> bool: ...
    def __ge__(self: 'T', otro: 'T') -> bool: ...
    def __eq__(self: 'T', otro: 'T') -> bool: ...
    def __ne__(self: 'T', otro: 'T') -> bool: ...

T = TypeVar('T', bound=Comparable)

class NodoABO(NodoAB[T]):
    def __init__(self, dato: T):
        super().__init__(dato)
    
    def __lt__(self, otro: "NodoABO[T]") -> bool:
        return isinstance(otro, NodoABO) and self.dato < otro.dato
    
    def __gt__(self, otro: "NodoABO[T]") -> bool:
        return isinstance(otro, NodoABO) and self.dato > otro.dato

    def __eq__(self, otro: "NodoABO[T]") -> bool:
        return isinstance(otro, NodoABO) and self.dato == otro.dato

class ArbolBinarioOrdenado(ArbolBinario[T]):
    
    @staticmethod
    def crear_nodo(dato: T) -> ArbolBinarioOrdenado[T]: # type: ignore
        nuevo = ArbolBinarioOrdenado()
        nuevo.set_raiz(NodoABO(dato))
        return nuevo
    
    def es_ordenado(self) -> bool:
        def es_ordenado_interna(
            arbol: "ArbolBinarioOrdenado[T]", 
            minimo: Optional[T] = None, 
            maximo: Optional[T] = None
        ) -> bool:
            if arbol.es_vacio():
                return True
            if (minimo is not None and arbol.dato() <= minimo) or (maximo is not None and arbol.dato() >= maximo):
                return False
            return es_ordenado_interna(arbol.si(), minimo, arbol.dato()) and es_ordenado_interna(arbol.sd(), arbol.dato(), maximo)
        
        return es_ordenado_interna(self)
    
    def insertar_si(self, arbol: "ArbolBinarioOrdenado[T]"):
        si = self.si()
        super().insertar_si(arbol)
        if not self.es_ordenado():
            super().insertar_si(si)
            raise ValueError("El árbol a insertar no es ordenado o viola la propiedad de orden del árbol actual")

    def insertar_sd(self, arbol: "ArbolBinarioOrdenado[T]"):
        sd = self.sd()
        super().insertar_sd(arbol)
        if not self.es_ordenado():
            super().insertar_sd(sd)
            raise ValueError("El árbol a insertar no es ordenado o viola la propiedad de orden del árbol actual")
        
    
    def insertar(self, valor: T):
        if self.es_vacio():
            self.set_raiz(NodoABO(valor))
        elif valor < self.dato():
            self.si().insertar(valor)
        else:
            self.sd().insertar(valor)
        
    def busqueda(self, n: T) -> bool:
        if self.dato == n:
            return True
        elif n < self.dato() and not self.si().es_vacio():
            return self.si().busqueda(n)
        elif n > self.dato() and not self.sd().es_vacio():
            return self.sd().busqueda(n)
        else:
            return False
        
    def busqueda_referencia(self, n) -> Optional['ArbolBinarioOrdenado[T]']:
        if self.dato == n:
            return self
        elif n < self.dato() and not self.si().es_vacio():
            return self.si().busqueda_referencia(n)
        elif n > self.dato() and not self.sd().es_vacio():
            return self.sd().busqueda_referencia(n)
        else:
            return None

# Ejercicio: Eliminación
# Implementar la operación de eliminación de un nodo según el valor pasado, incluyendo todos los casos vistos y ambas estrategias (fusión y copia).

# Ejercicio: Convertir a Ordenado
# Dado un árbol binario clásico, definir una operación que permita convertirlo en un árbol binario ordenado si se cumplen las restricciones de orden. De lo contrario, devolver una excepción. Tener en cuenta que el nuevo árbol debe ser una copia del original y con el tipo de dato adecuado (ArbolBinarioOrdenado).