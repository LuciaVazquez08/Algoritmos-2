def desde_hasta_no_inclusiva(x:int, y:int) -> list[int]:
    if y < x:
        raise ValueError("No es posible con ese orden de numeros")
    acumulado =[]
    def desde_hasta_intrna(x,y,acumulado):
        if x == y:
            return acumulado
        else:
            acumulado.append(x)
            return desde_hasta_intrna(x+1,y,acumulado)
    return desde_hasta_intrna(x,y, acumulado)

def desde_hasta_inclusiva(x:int, y:int) -> list[int]:
    if y <= x:
        raise ValueError("No es posible con ese orden de numeros")
    acumulado =[]
    def desde_hasta_intrna(x,y,acumulado):
        if x == y:
            acumulado.append(x)
            return acumulado
        else:
            acumulado.append(x)
            return desde_hasta_intrna(x+1,y,acumulado)
    return desde_hasta_intrna(x,y,acumulado)

print(desde_hasta_inclusiva(0,3))   



