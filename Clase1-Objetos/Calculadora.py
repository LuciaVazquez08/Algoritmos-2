class Calculadora:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

    def suma(self) -> float:
        return self.x + self.y
    
    def resta(self) -> float:
        return self.x - self.y
    
    def multiplicacion(self) -> float:
        return self.x * self.y
    
    def division(self) -> float:
        if (self.y != 0):
            return self.x/self.y
        else:
            return "No se puede dividir por cero"
