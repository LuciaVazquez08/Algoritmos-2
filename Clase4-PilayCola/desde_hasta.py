def desde_hasta_no_inclusiva(x:int, y:int) -> list[int]:
    if y < x:
        raise ValueError("No es posible con ese orden de numeros")
    def desde_hasta_intrna(x,y,acumulado):
        if x == y:
            return acumulado
        else:
            return desde_hasta_intrna(x+1,y,acumulado+x)
    return desde_hasta_intrna(x,y,0)

def desde_hasta_inclusiva(x:int, y:int) -> list[int]:
    if y < x:
        raise ValueError("No es posible con ese orden de numeros")
    def desde_hasta_intrna(x,y,acumulado):
        if x == y:
            return acumulado + x
        else:
            return desde_hasta_intrna(x+1,y,acumulado+x)
    return desde_hasta_intrna(x,y,0)

print(desde_hasta_no_inclusiva(0,3))   
