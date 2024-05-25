from abc import ABC, abstractmethod
from typing import TypeAlias
from arbolH import ArbolH

Number: TypeAlias = int | float

class Operador(ABC):
    simbolo: str

    @staticmethod
    @abstractmethod
    def operar(a: Number, b: Number) -> Number:
        ...
    
    def __str__(self) -> str:
        return self.simbolo

class Suma(Operador):
    simbolo: str = '+'

    @staticmethod
    def operar(a: Number, b: Number) -> Number:
        return a + b

class Producto(Operador):
    simbolo: str = '*'
    
    @staticmethod
    def operar(a: Number, b: Number) -> Number:
        return a * b
    
class Resta(Operador):
    simbolo: str = '-'
    
    @staticmethod
    def operar(a: Number, b: Number) -> Number:
        return a - b
    
class Division(Operador):
    simbolo: str = '/'

    @staticmethod
    def operar(a: Number, b: Number) -> Number:
        return a / b
    

class ExpresionAritmetica(ArbolH[Number,Operador]):
    def __init__(self, dato: Number):
        super().__init__(dato)

    @staticmethod
    def valor(valor: Number) -> "ExpresionAritmetica":
        return ExpresionAritmetica(valor)
    
    @staticmethod
    def _crear_operacion(operador: Operador, operando_1: "ExpresionAritmetica", operando_2: "ExpresionAritmetica") -> "ExpresionAritmetica":
        nuevo = ExpresionAritmetica(operador)
        nuevo._insertar_subarbol_nocheck(operando_1)
        nuevo._insertar_subarbol_nocheck(operando_2)
        return nuevo
    
    @staticmethod
    def suma(operando_1: "ExpresionAritmetica", operando_2: "ExpresionAritmetica") -> "ExpresionAritmetica":
        return ExpresionAritmetica._crear_operacion(Suma(), operando_1, operando_2)
    
    @staticmethod
    def resta(operando_1: "ExpresionAritmetica", operando_2: "ExpresionAritmetica") -> "ExpresionAritmetica":
        return ExpresionAritmetica._crear_operacion(Resta(), operando_1, operando_2)
    
    @staticmethod
    def producto(operando_1: "ExpresionAritmetica", operando_2: "ExpresionAritmetica") -> "ExpresionAritmetica":
        return ExpresionAritmetica._crear_operacion(Producto(), operando_1, operando_2)
    
    @staticmethod
    def division(operando_1: "ExpresionAritmetica", operando_2: "ExpresionAritmetica") -> "ExpresionAritmetica":
        return ExpresionAritmetica._crear_operacion(Division(), operando_1, operando_2)
    
    def es_valor(self) -> bool:
        return self.es_hoja()
    
    def evaluar(self) -> Number:
        if self.es_valor():
            return self.dato_hoja()
        operador = self.dato_nodo()
        operando_1, operando_2 = self.subarboles
        return operador.operar(operando_1.evaluar(), operando_2.evaluar())
    
    def __str__(self) -> str:
        return super().__str__()
    
def main():
    # Crea expresion: 2 ∗ 9 / (2 + 1) + 8 − 3 ∗ 4
    expresion = ExpresionAritmetica.suma(
        ExpresionAritmetica.producto(
            ExpresionAritmetica.valor(2),
            ExpresionAritmetica.division(
                ExpresionAritmetica.valor(9),
                ExpresionAritmetica.suma(
                    ExpresionAritmetica.valor(2),
                    ExpresionAritmetica.valor(1)
                )
            )
        ),
        ExpresionAritmetica.resta(
            ExpresionAritmetica.valor(8),
            ExpresionAritmetica.producto(
                ExpresionAritmetica.valor(3),
                ExpresionAritmetica.valor(4)
            )
        )
    )

    print(expresion)
    print(f'El resultado es: {expresion.evaluar()}')

if __name__ == "__main__":
    main()


# Ejercicio: Construir desde tuplas anidadas
# Implementar un método que permita construir una expresión aritmética a partir de una estructura de tuplas anidadas, donde cada tupla tenga 3 elementos: (expresión_1, operación, _expresión_2). Como una expresión puede ser otra tupla, la tupla que le pasemos para construir la expresión final puede ser anidada.

# Por ejemplo: ( (2, *, (9, /, (2, +, 1) ) ), +, (8, -, (3, *, 4) ) )

# Ejercicio: Extender a operaciones n-arias
# Extender la clase ExpresionAritmetica de forma que soporte operaciones n-arias, incluyendo unarias, ternarias, etc.

