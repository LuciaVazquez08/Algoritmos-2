from functools import reduce
from typing import Any, Generic, TypeVar

T = TypeVar('T')

class ArbolN(Generic[T]):
    def __init__(self, dato: T):
        self._dato: T = dato
        self._subarboles: list[ArbolN[T]] = []

    @property
    def dato(self) -> T:
        return self._dato

    @dato.setter
    def dato(self, valor: T):
        self._dato = valor

    @property
    def subarboles(self) -> list[ArbolN[T]]: # type: ignore
        return self._subarboles

    @subarboles.setter
    def subarboles(self, subarboles: list[ArbolN[T]]): # type: ignore
        self._subarboles = subarboles

    def insertar_subarbol(self, subarbol: ArbolN[T]): # type: ignore
        self.subarboles.append(subarbol)

    def es_hoja(self) -> bool:
        return self.subarboles == []
    
    def altura(self) -> int:
        def altura_n(bosque: list[ArbolN[T]]) -> int:
            if not bosque:
                return 0
            else:
                return max(bosque[0].altura(), altura_n(bosque[1:]))
        
        return 1 + altura_n(self.subarboles)
        
    def __len__(self) -> int:
        if self.es_hoja():
            return 1
        else:
            return 1 + sum([len(subarbol) for subarbol in self.subarboles])
        
    def __eq__(self, other: ArbolN) -> bool: # type: ignore
        if not isinstance(other, ArbolN):
            return False
        if self.dato != other.dato or len(self.subarboles) != len(other.subarboles):
            return False
        
        i = 0
        diferencia = False
        while i < len(self.subarboles) and not diferencia:
            diferencia = not self.subarboles[i].__eq__(other.subarboles[i])
            i += 1
        
        return not diferencia
    
    #paradigma funcional
    def preorder(self) -> list[T]:
        return reduce(
            lambda recorrido, subarbol: recorrido + subarbol.preorder(), 
            self.subarboles, 
            [self.dato]
        )
    
    #imperativo
    def preorder(self) -> list[T]:
        recorrido = [self.dato]
        for subarbol in self.subarboles:
            recorrido += subarbol.preorder()
        return recorrido
    
    #recursion mutua
    def preorder(self) -> list[T]:
        def preorder_n(bosque: list[ArbolN[T]]) -> list[T]:
            if not bosque:
                return []
            else:
                return bosque[0].preorder() + preorder_n(bosque[1:])

        return [self.dato] + preorder_n(self.subarboles)
    
    #recursion multiple directa
    def postorder(self) -> list[T]:
        return reduce(
            lambda recorrido, subarbol: subarbol.postorder() + recorrido, 
            self.subarboles, 
            [self.dato]
        )
    
    #recursion mutua
    def postorder(self) -> list[T]:
        def postorder_n(bosque: list[ArbolN[T]]) -> list[T]:
            if not bosque:
                return []
            else:
                return postorder_n(bosque[1:]) + bosque[0].postorder()

        return postorder_n(self.subarboles) + [self.dato]
    
    def bfs_n(self):
        def recorrer():
            while q:
                actual = q.pop(0)                    
                visitar(actual.dato)
                for subarbol in actual.subarboles:  
                    q.append(subarbol)           
        visitados = []
        visitar = lambda dato: visitados.append(dato)        
        q: list[ArbolN[T]] =[self]                
        recorrer()
        return visitados
    
    def copy(self) -> ArbolN: # type: ignore
        raiz = ArbolN(self.dato.copy())

        for subarbol in self.subarboles:
            raiz.insertar_subarbol(subarbol.copy())
        
        return raiz
    
    def recorrido_guiado(arbol: ArbolN, camino: list[int]) ->list[T]: # type: ignore
        valores = []
        if not camino: 
            return arbol.dato
        else:
            for n in camino:
                if len(arbol.subarboles) > n:
                    valores.append(arbol.subarboles[n])
                else: 
                    raise ValueError("No se puede seguir el camino, el índice está fuera de rango.")

            




    

        
     