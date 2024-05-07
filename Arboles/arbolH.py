from typing import Generic, TypeVar

T = TypeVar('T')
S = TypeVar('S')

class ArbolH(Generic[T, S]):
    def __init__(self, dato: T | S):
        self._dato: T | S = dato
        self._subarboles: list[ArbolH[T, S]] = []
        self._tipo_hoja = type(dato)
        self._tipo_nodo = None

    @staticmethod
    def crear_nodo_y_hojas(dato_raiz: S, *datos_hojas: T) -> "ArbolH[T, S]":
        if not datos_hojas:
            raise ValueError("Se requiere al menos un dato para las hojas")
        if (not all([isinstance(dato, type(datos_hojas[0])) for dato in datos_hojas])):
            raise ValueError("Todos los datos de las hojas deben ser del mismo tipo")
        
        nuevo = ArbolH(dato_raiz)
        for dato in datos_hojas:
            subarbol = ArbolH(dato)
            subarbol._tipo_nodo = type(dato_raiz)
            nuevo._subarboles.append(subarbol)
        nuevo._tipo_nodo = type(dato_raiz)
        nuevo._tipo_hoja = type(datos_hojas[0])
        return nuevo
    
    def __init__(self, dato: T | S, *datos_hojas: T):
        self._dato: T | S = dato
        self._subarboles: list[ArbolH[T, S]] = []
        self._tipo_nodo = None
        self._tipo_hoja = type(dato)
        if datos_hojas:
            if not all([isinstance(hoja, type(datos_hojas[0])) for hoja in datos_hojas]):
                raise ValueError("Todos los datos de las hojas deben ser del mismo tipo")
            for hoja in datos_hojas:
                subarbol = ArbolH(hoja)
                subarbol._tipo_nodo = type(dato)
                self._subarboles.append(subarbol)
            self._tipo_nodo = type(dato)
            self._tipo_hoja = type(datos_hojas[0])

    def insertar_subarbol(self, subarbol: "ArbolH[T,S]"):
        if self.es_hoja():
            raise ValueError("No se pueden insertar subárboles en un nodo hoja")

        if not self._son_mismos_tipos(subarbol):
            raise ValueError("El árbol a insertar no es consistente con los tipos de datos del árbol actual")

        subarbol._tipo_nodo = self._tipo_nodo
        self.subarboles.append(subarbol)

    def _son_mismos_tipos(self, otro: "ArbolH[T,S]") -> bool:
        return (
            isinstance(otro, ArbolH) and (
                self._tipo_nodo == otro._tipo_nodo or self.es_hoja() or otro.es_hoja()
            ) and self._tipo_hoja == otro._tipo_hoja
        )
    

# Ejercicio: Validar árbol completo
# Implementar un método es_valido() que devuelva si el árbol es consistente en sus tipos de datos. Esto implica que todos los nodos intermedios son del mismo tipo, y que todos los nodos hoja son del mismo tipo.