from typing import Generic, TypeVar, Optional
T = TypeVar('T')

class Grafo(Generic[T]):
    def __init__(self, vertices: set[T]=set(),aristas: list[tuple[T]]=[]) -> None:
        self.vertices = vertices
        self.aristas = aristas

    def agregar_nodo(self,nodo:T) -> None:
        if not nodo in self.vertices:
            self.vertices.add(nodo)
        else:
            raise ValueError(f"El nodo {nodo} ya pertenece al grafo.")

    def agregar_arista(self,arista:tuple[T]) -> None:
        opuesta = arista[::-1]
        if arista in self.aristas:
            raise ValueError(f"La arista {arista} ya pertenece al grafo")
        elif opuesta in self.aristas:
            raise ValueError(f"La arista {opuesta} ya pertenece al grafo")
        else:
            self.aristas.append(arista)

    def eliminar_nodo(self,nodo:T) -> None:
        if not nodo in self.vertices:
            raise ValueError(f"El nodo {nodo} no pertenece al grafo.")
        else:
            self.vertices.remove(nodo)

    def eliminar_arista(self,arista:tuple[T]) -> None:
        if arista not in self.aristas:
            raise ValueError(f"El nodo {arista} no pertenece al grafo.")
        else:
            self.aristas.remove(arista)

    def es_vecino_de(self,nodoA:T,nodoB:T) -> bool:
        ab = (nodoA,nodoB)
        ba = (nodoB,nodoA)
        if ab in self.aristas or ba in self.aristas:
            return True
        else:
            return False
    
    def vecinos_de(self,nodo:T) -> list[T]:
        vecinos = []
        for arista in self.aristas:
            if nodo in arista:
                vecinos.append(arista[not arista.index(nodo)])
        return vecinos
    
    def dfs(self) -> list[T]:
        def dfs(actual : T,recorrido : list[T] = []):
            recorrer = self.vecinos_de(actual)
            for nodo in recorrer:
                if not nodo in recorrido:
                    recorrido.append(nodo)
                    dfs(nodo,recorrido)


        recorrido = [list(self.vertices)[0]]
        dfs(list(self.vertices)[0],recorrido)
        return recorrido

    def dfs2(self)->list[T]:
        def dfs2(recorrido,pila):
            actual = pila.pop()
            vecinos_actual = self.vecinos_de(actual) 
            recorrer = [vecino for vecino in vecinos_actual if not vecino in recorrido+pila]    
            pila = pila + recorrer
            recorrido.append(actual)
            if pila:    
                dfs2(recorrido,pila)
        recorrido = [list(self.vertices)[0]]
        dfs2(recorrido,recorrido)
        return recorrido
    
    def bfs(self) -> list[T]:
        def bfs(recorrido:list[T],cola:list[T]):
            actual = cola.pop(0)
            recorrido.append(actual)
            encolables = [vecino for vecino in self.vecinos_de(actual) if not vecino in recorrido+cola]
            cola += encolables
            if cola:
                bfs(recorrido,cola)
        recorrido = []
        primer_nodo = list(self.vertices)[0]
        bfs(recorrido,[primer_nodo])
        return recorrido
    
    def dfs_origen(self,origen) -> list[T]:
        def dfs(actual : T,recorrido : list[T] = []):
            recorrer = self.vecinos_de(actual)
            for nodo in recorrer:
                if not nodo in recorrido:
                    recorrido.append(nodo)
                    dfs(nodo,recorrido)


        recorrido = [origen]
        dfs(origen,recorrido)
        return recorrido 



    def existe_conexion(self,a:T,b:T) -> bool: #Tarea
        def dfs(actual : T,buscado:T,recorrido : list[T] = []):
            if actual not in recorrido:
                recorrido.append(actual)
                recorrer = self.vecinos_de(actual)
                encontrado = False
                while recorrer and not encontrado:
                    nodo = recorrer.pop()
                    if nodo == buscado:
                        encontrado=True
                        recorrido.append(nodo)
                    else:
                        if not nodo in recorrido:
                            encontrado = dfs(nodo,buscado,recorrido)
                return encontrado
            else:
                return False
                    
        recorrido = []
        return dfs(a,b,recorrido)
    
    # def existe_conexion(self,a,b):
    #     def bfs(recorrido:list[T],cola:list[T]):
    #         actual = cola.pop(0)
    #         recorrido.append(actual)
    #         encolables = [vecino for vecino in self.vecinos_de(actual) if not vecino in recorrido+cola]
    #         cola += encolables
    #         if cola:
    #             bfs(recorrido,cola)

    #     recorrido = []


if __name__ == "__main__":
    graf = Grafo()
    for i in range(1,9):
        graf.agregar_nodo(i)
    
    aristas = [(1,2),(2,4),(2,5),(4,7),(5,6),(6,3),(1,3)]

    for arista in aristas:
        graf.agregar_arista(arista)

    print(graf.aristas)
    print(graf.vertices)
    print(graf.dfs())
    print(graf.dfs_origen(8))
    print(graf.bfs())
    print(graf.existe_conexion(1,8))

    