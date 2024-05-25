from functools import reduce
from typing import Generic, TypeVar, Optional

T = TypeVar("T")

class ArbolN(Generic[T]):
    def __init__(self, dato: T):
        self._dato = dato
        self._subarboles:list[ArbolN] = []
    @property
    def dato(self):
        return self._dato
    @dato.setter
    def dato(self, valor: T):
        self._dato = valor
    @property
    def subarboles(self):
        return self._subarboles
    @subarboles.setter
    def subarboles(self, arboles: list["ArbolN[T]"]):
        self._subarboles = arboles
    
    def insertar_arbol(self, arbol: "ArbolN[T]"):
        self._subarboles.append(arbol)
    
    def es_hoja(self):
        return len(self._subarboles) == 0
    
    def altura(self):
        if self.es_hoja():
            return 1
        return 1 + max([a.altura() for a in self.subarboles])
    
    def __len__(self):
        if self.es_hoja():
            return 1
        return 1 + sum([len(a) for a in self.subarboles])

    def __eq__(self, o: object) -> bool:
        def eq__n(bosque1: list[ArbolN], bosque2: list[ArbolN]):
            if len(bosque1) != len(bosque2):
                return False
            elif len(bosque1) == 0:
                return True
            return bosque1[0] == bosque2[0] and eq__n(bosque1[1:], bosque2[1:])
        
        if not isinstance(o, ArbolN):
            return False
        return self.dato == o.dato and eq__n(self.subarboles, o.subarboles)

    def preorder(self):
        recorrido: list[T] = [self.dato]
        for arbol in self.subarboles:
            recorrido += arbol.preorder()
        return recorrido

    def postorder(self):
        recorrido: list[T] = []
        for arb in self.subarboles:
            recorrido += arb.postorder()
        return recorrido + [self.dato]
    
    def postorder_reduce(self):
        parcial = reduce(lambda recorrido, subarbs: recorrido + subarbs.postorder_reduce(), 
        self.subarboles,
        [])
        parcial.append(self.dato)
        return parcial

    def postorder_mutua(self):
        def postorder_n(bosque: list[ArbolN]):
            if len(bosque) == 0:
                return []
            else:
                return bosque[0].postorder() + postorder_n(bosque[1:])
        return postorder_n(self.subarboles) + [self.dato]
    
    def bfs(self):
        def recorrer(q: list[ArbolN[T]], recorrido: list[T]):
            if len(q) == 0:
                return recorrido
            actual = q.pop(0)
            recorrido.append(actual.dato)
            for arb in actual.subarboles:
                q.append(arb)
            return recorrer(q, recorrido)
        return recorrer([self], [])
    
    def __getitem__(self, camino):
        # NOTE: Ignorar este metodo, solo andaba jugando con las formas de hacer 
        # recorridos con slices. Ejemplo arbol[0:3, 1:6] -> list[list[T]]

        # Casos base
        if isinstance(camino, slice):
            # Se esta usando arbol[start:end:step]
            return [a.dato for a in self.subarboles[camino]]
        if isinstance(camino, int):
            # Se esta usando arbol[a]
            return self.subarboles[camino].dato
        if len(camino) == 1:
            if isinstance(camino[0], slice):
                # Se esta usando arbol[a, ..., n, start:end:step]
                return [a.dato for a in self.subarboles[camino[0]]]
            # Se esta usando arbol[..., n]
            if len(self.subarboles) <= camino[0]:
                # NOTE: No se si deberia dejar esto
                return None
            return self.subarboles[camino[0]].dato
        
        # recursion
        if isinstance(camino[0], slice):
            # Se esta usando arbol[start:end:step, ...]
            return [a[camino[1:]] for a in self.subarboles[camino[0]]]
        # Se esta usando arbol[a, ..., n]
        return self.subarboles[camino[0]][camino[1:]]

    def __str__(self) -> str:
        def recorrer(t: ArbolN[T], nivel: int):
            txt = " "*nivel*2 + "└" + str(t.dato) + "\n"
            for arb in t.subarboles:
                txt += recorrer(arb, nivel+1)
            return txt
        return recorrer(self, 0)

    def copy(self):
        nuevo = ArbolN(self.dato)
        for arb in self.subarboles:
            nuevo.insertar_arbol(arb.copy())
        return nuevo
    
    def nivel(self, valor: T):
        def interna(t: ArbolN[T], nivel: int):
            if t.dato == valor:
                return nivel
            if t.es_hoja():
                return 0
            niveles = [interna(a, nivel+1) for a in t.subarboles]
            return [n for n in niveles if n != 0][0]
        niv = interna(self, 1)
        if niv != 0:
            return niv
        else:
            raise ValueError(f"El valor no existe en el arbol")
    
    def sin_hojas(self) -> Optional["ArbolN[T]"]:
        if self.es_hoja():
            return None
        nuevo = ArbolN(self.dato)
        for arb in self.subarboles:
            a = arb.sin_hojas()
            if a is not None:
                nuevo.insertar_arbol(a)
        return nuevo
    
    def antecesores(self, dato: T) -> list[T]:
        if self.dato == dato:
            return [self.dato]
        elif self.es_hoja():
            return []
        i = 0
        resultado = []
        while i < len(self.subarboles) and not resultado:
            resultado = self.subarboles[i].antecesores(dato)
            i += 1
        if resultado:
            if resultado[0] == dato:
                resultado.pop()
            resultado.insert(0, self.dato)
        return resultado
    
    def antecesores_(self, dato: T) -> list[T]:
        def interna(t: ArbolN[T], antecesores: list[T], dato: T):
            if t.dato == dato:
                return antecesores
            if t.es_hoja():
                return []
            antecesores.append(t.dato)
            i = 0
            resultado = []
            while i < len(t.subarboles) and not resultado:
                resultado = interna(t.subarboles[i], antecesores.copy(), dato)
                i += 1
            return resultado
        return interna(self, [], dato)

    def recorrido_guiado(self, camino: list[int]) -> T | None:
        if len(camino) == 0:
            return self.dato
        if self.es_hoja():
            raise IndexError("No existe la direccion")
        return self.subarboles[camino[0]].recorrido_guiado(camino[1:])

def main():
    t = ArbolN("00")
    for i in range(5):
        t.insertar_arbol(ArbolN(f"A{i}"))
    for i in range(3):
        t.subarboles[0].insertar_arbol(ArbolN(f"B{i}"))
    for i in range(6):
        t.subarboles[1].insertar_arbol(ArbolN(f"C{i}"))
    for i in range(4):
        t.subarboles[4].insertar_arbol(ArbolN(f"D{i}"))
    for i in range(3):
        t.subarboles[0].subarboles[1].insertar_arbol(ArbolN(f"E{i+1}"))
    print(t)
    print(t.recorrido_guiado([100,0]))

if __name__ == "__main__":
    main()