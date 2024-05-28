from functools import reduce
from typing import Generic, TypeVar, Optional

T = TypeVar("T")

class ArbolN(Generic[T]):
    def __init__(self, dato: T):
        self._dato = dato
        self._subarboles:list[ArbolN] = []

    @property
    def dato(self) -> T:
        return self._dato
    
    @dato.setter
    def dato(self, valor: T):
        self._dato = valor

    @property
    def subarboles(self) -> list[ArbolN[T]]:
        return self._subarboles
    
    @subarboles.setter
    def subarboles(self, arboles: list["ArbolN[T]"]):
        self._subarboles = arboles
    
    def insertar_subarbol(self, arbol: "ArbolN[T]"):
        self._subarboles.append(arbol)
    
    def es_hoja(self) -> bool:
        return len(self._subarboles) == 0
    
    def altura(self) -> int:
        if self.es_hoja():
            return 1
        return 1 + max([a.altura() for a in self.subarboles])
    
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
    
    def __str__(self):
        def mostrar(t: ArbolN[T], nivel: int):
            tab = '.' * 4
            indent = tab * nivel
            out = indent + str(t.dato) + '\n'
            for subarbol in t.subarboles:
                out += mostrar(subarbol, nivel + 1)
            return out
            
        return mostrar(self, 0)

    def preorder(self) -> list[T]:
        recorrido: list[T] = [self.dato]
        for arbol in self.subarboles:
            recorrido += arbol.preorder()
        return recorrido

    def postorder(self) -> list[T]:
        recorrido: list[T] = []
        for arb in self.subarboles:
            recorrido = arb.postorder() + recorrido
        return recorrido
    
    def postorder_mutua(self) -> list[T]:
        def postorder_n(bosque: list[ArbolN]):
            if len(bosque) == 0:
                return []
            else:
                return bosque[0].postorder() + postorder_n(bosque[1:])
        return postorder_n(self.subarboles) + [self.dato]
    
    def postorder_reduce(self) -> list[T]:
        parcial = reduce(lambda recor, subarb: recor +subarb.postorder_reduce(), self.subarboles, [])
        parcial.append(self.dato)
        return parcial

    def bfs(self) -> list[T]:
        def recorrer(q: list[ArbolN[T]], recorrido: list[T]):
            if len(q) == 0:
                return recorrido
            actual = q.pop(0)
            recorrido.append(actual.dato)
            for arb in actual.subarboles:
                q.append(arb)
            return recorrer(q, recorrido)
        return recorrer([self], [])

    def recorrido(self, camino: list[int] | tuple[int]) -> list[T]:
        if len(camino) == 1:
            return self.subarboles[camino[0]].dato
        return self.subarboles[camino[0]].recorrido(camino[1:])
    
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

    def copy(self) -> "ArbolN[T]":
        nuevo = ArbolN(self.dato)
        for arb in self.subarboles:
            nuevo.insertar_subarbol(arb.copy())
        return nuevo
    
    def sin_hojas(self) -> Optional["ArbolN[T]"]:
        if self.es_hoja():
            return None
        nuevo = ArbolN(self.dato)
        for arb in self.subarboles:
            a = arb.sin_hojas()
            if a is not None:
                nuevo.insertar_subarbol(a)
        return nuevo

    def nivel(self, valor: T) -> int:
        def bfs(q: list[tuple[ArbolN[T], int]], valor: T):
            if len(q) == 0:
                return 0
            actual, nivel = q.pop(0)
            if actual.dato == valor:
                return nivel
            for arb in actual.subarboles:
                q.append((arb, nivel+1))
            return bfs(q, valor)
        
        n = bfs([(self, 1)], valor)
        if n == 0:
            raise ValueError(f"El arbol no contiene el valor {valor}")
        else:
            return n
        
    def nivel(self,x:T) -> int:
        def nivel_n(lista,acum) -> int:
            if not lista:
                return 0
            else:
                index = max([n.nivel(x) for n in lista])
                return index + acum if index>0 else 0
        if self.es_hoja():
            return 0
        elif self.dato == x:
            return 1
        else:
            return nivel_n(self.subarboles,0) 



    def nivel2(self, x: T) -> int: #type:ignore
        if self.es_hoja():
            return  0
        elif self.dato == x:
            return 1
        else:
            lista_busqueda = [n.nivel(x) for n in self.subarboles]
            return max(lista_busqueda) + 1 if sum(lista_busqueda)>0 else 0
        
    def nivel3(self,x:T): #de tomi
        def buscar(t,x):
            if x== t.dato:
                return 1,True
            elif t.es_hoja():
                return 2,False
            else:
                found = False
                n=0
                i=0
                while not found and i< len(t.subarboles):
                    m,found = buscar(t.subarboles[i],x)
                    if not found:
                        n = max(n,m)
                    i +=1
                return n+1,found
        return buscar(self,x)[0]
        


    def ramas(self) -> list[list[T]]:
        if self.es_hoja():
            return [[self.dato]]
        else:
            ramas = []
            for subarbol in self.subarboles:
                ramas += subarbol.ramas()
            return [ [self.dato]+rama for rama in ramas]
        
    def ramas2(self) -> list[list[T]]:
        if self.es_hoja():
            return [[self.dato]]
        else:
            return [[self.dato]+rama[0] for rama in [[]+subarbol.ramas() for subarbol in self.subarboles]]
        
            

    #antecesores y sin ramas
    
    def antecesores(self,dato:T) ->list[T]:
        # caso base 1: self.dato == dato
        # caso base 2: self.es_hoja() y no es valor
        # caso recursivo: no es hoja y 
        if self.dato == dato:
            return [dato]
        elif self.es_hoja():
            return []
        else:
            i=0
            res = []
            while i< len(self.subarboles) and not res:
                res = self.subarboles[i].antecesores(dato)
                i+=1
            if res:
                if res[0] == dato:
                    res.pop()
                res.insert(0,self.dato)
            return res
    
    def antecesores2(self,dato:T) -> list[T]:
        def interna(arbol:ArbolN) ->list[T]:
            if arbol.dato == dato:
                return [dato]
            elif arbol.es_hoja():
                return []
            else:
                i=0
                res = []
                while i<len(arbol.subarboles) and not res:
                    res = interna(arbol.subarboles[i])
                    i+=1
                if res:
                    res.insert(0,arbol.dato)
                return res
        res = interna(self)
        res.pop()
        return res
    
    
    def antecesores3(self,dato:T) ->list[T]:
        # caso base 1: self.dato == dato
        # caso base 2: self.es_hoja() y no es valor
        # caso recursivo: no es hoja y 
        if self.dato == dato or self.es_hoja():
            return []
        else:
            i=0
            res = []
            encontrado = False
            while i< len(self.subarboles) and not encontrado:
                if self.subarboles[i]==dato:
                    encontrado = True
                else: 
                    res = self.subarboles[i].antecesores(dato)
                    encontrado = bool(res)
                i+=1
            if encontrado:
                res.insert(0,self.dato)
            return res
        
    def antecesores4(self,dato:T)->list[T]:
        def interna(arbol:ArbolN,antecesores : list[T])->list[T]:
            if arbol.dato == dato:
                return antecesores
            elif arbol.es_hoja():
                return []
            else:
                antecesores.append(arbol.dato)
                i=0
                res = []
                while i<len(arbol.subarboles) and not res:
                    res = interna(arbol.subarboles[i],antecesores.copy())
                    i+=1
                return res        
        return interna(self,[])

    def recorrido_guiado(self, direcciones: list[int]) -> Optional[T]:#type:ignore
        if not direcciones:
            return self.dato
        else:
                direc = direcciones.pop(0)
                if direc >= len(self.subarboles):
                    raise ValueError("No existe la direccion")
                return self.subarboles[direc].recorrido_guiado(direcciones)

def main():
    t = ArbolN("00")
    for i in range(5):
        t.insertar_subarbol(ArbolN(f"A{i}"))
    for i in range(3):
        t.subarboles[0].insertar_subarbol(ArbolN(f"B{i}"))
    for i in range(6):
        t.subarboles[1].insertar_subarbol(ArbolN(f"C{i}"))
    for i in range(4):
        t.subarboles[4].insertar_subarbol(ArbolN(f"D{i}"))
    for i in range(3):
        t.subarboles[0].subarboles[1].insertar_subarbol(ArbolN(f"E{i}"))
    print(t.postorder())
    print(t.postorder_mutua())
    print(t.postorder_reduce())

if __name__ == "__main__":
    main()