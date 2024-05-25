from typing import TypeVar, Protocol, Optional
from arbol_binario import ArbolBinario, NodoAB

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
        super().__init__(dato, ArbolBinarioOrdenado(), ArbolBinarioOrdenado())
    
    def __lt__(self, otro: "NodoABO[T]") -> bool:
        return isinstance(otro, NodoABO) and self.dato < otro.dato
    
    def __gt__(self, otro: "NodoABO[T]") -> bool:
        return isinstance(otro, NodoABO) and self.dato > otro.dato

    def __eq__(self, otro: "NodoABO[T]") -> bool:
        return isinstance(otro, NodoABO) and self.dato == otro.dato

class ArbolBinarioOrdenado(ArbolBinario[T]):
    @staticmethod
    def crear_nodo(dato: T) -> "ArbolBinarioOrdenado[T]":
        nuevo = ArbolBinarioOrdenado()
        nuevo.set_raiz(NodoABO(dato))
        return nuevo
    
    def __init__(self):
        self.raiz: Optional[ArbolBinarioOrdenado[T]] = None

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
        elif self.dato() == valor:
            raise ValueError(f"el valor {valor} ya se encuentra en el arbol")
        elif valor < self.dato():
            self.si().insertar(valor)
        else:
            self.sd().insertar(valor)

    def max(self) -> "ArbolBinarioOrdenado[T]":
        if self.es_vacio():
            raise ValueError("El arbol esta vacio")
        if self.sd().es_vacio():
            return self
        return self.sd().max()

    def min(self) -> "ArbolBinarioOrdenado[T]":
        if self.es_vacio():
            raise ValueError("El arbol esta vacio")
        if self.si().es_vacio():
            return self
        return self.si().min()
    
    def buscar(self, valor: T) -> bool:
        if self.es_vacio():
            return False
        if self.dato() == valor:
            return True
        elif valor > self.dato():
            return self.sd().buscar(valor)
        else:
            return self.si().buscar(valor)
    
    def buscar_2(self, valor: T) -> "ArbolBinarioOrdenado[T]":
        if self.es_vacio():
            raise ValueError(f"El arbol no contiene el valor {valor}")
        if self.dato() == valor:
            return self
        elif valor > self.dato():
            return self.sd().buscar_2(valor)
        else:
            return self.si().buscar_2(valor)
    
    def __str__(self) -> str:
        def recorrer(t: ArbolBinarioOrdenado[T], nivel: int):
            if t.es_vacio():
                return "AV"
            txt = " "*2*nivel + "└" + str(t.dato()) + "\n"
            if not t.si().es_vacio():
                txt += recorrer(t.si(), nivel+1)
            else:
                txt += " "*2*(nivel+1)  + "└" +  "AV" + "\n"
            if not t.sd().es_vacio():
                txt += recorrer(t.sd(), nivel+1)
            else:
                txt += " "*2*(nivel+1)  + "└" +  "AV" + "\n"

            return txt
        return recorrer(self, 0)
    
    def predecesor(self, valor: T) -> "ArbolBinarioOrdenado[T]":
        def recorrer(t: ArbolBinarioOrdenado[T], valor: T, pred: ArbolBinarioOrdenado[T]):
            if t.es_vacio():
                raise ValueError("Arbol Vacio")
            if t.dato() == valor:
                return pred
            if valor > t.dato():
                return recorrer(t.sd(), valor, t)
            else:
                return recorrer(t.si(), valor, t)
        return recorrer(self, valor, None)

    def eliminar(self, valor: T):
        # Este eliminar seguramente este mal hecho porque no usa ninguna recursion
        aux = self.buscar_2(valor) # Hay que eliminar a aux
        if aux.es_hoja():
            aux.raiz = None
            return
        pred = self.predecesor(valor) # predecesor de aux
        if pred is None:
            max_si:ArbolBinarioOrdenado[T] = aux.si().max()
            max_si.insertar_sd(aux.sd())
            self.raiz = max_si.raiz
        elif not aux.si().es_vacio() and aux.sd().es_vacio():
            pred.insertar_si(aux.si())
        elif aux.si().es_vacio() and not aux.sd().es_vacio():
            pred.insertar_sd(aux.sd())
        else:
            maxi_si_aux: ArbolBinarioOrdenado[T] = aux.si().max()
            maxi_si_aux.insertar_sd(aux.sd())
            pred.insertar_sd(maxi_si_aux)
        


def main():
    t = ArbolBinarioOrdenado.crear_nodo(10)
    t.insertar(4)
    t.insertar(1)
    t.insertar(12)
    t.insertar(22)
    t.insertar(13)
    t.insertar(30)
    # t.eliminar(10)
    print(t)

if __name__ == "__main__":
    main()