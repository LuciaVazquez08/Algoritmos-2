def desde_hasta(x:int, y:int) -> list[int]:
    if y < x:
        raise ValueError("No es posible con ese orden de numeros")
    def desde_hasta_intrna(x,y,acumulado):
        if x == y:
            return acumulado
        else:
            return desde_hasta_intrna(x+1,y,acumulado+x)
    else:
        return desde_hasta_intrna(x,y,1)
    