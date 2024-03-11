class Rectangulo:
    def __init__(self, base, altura) -> None:
        self.base = base
        self.altura = altura
    
    def area(self)-> float:
        return self.base * self.altura
    
    def perimetro(self) -> float:
        return 2* (self.base + self.altura)
