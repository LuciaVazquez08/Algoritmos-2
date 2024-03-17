def desde_hasta(x:int, y:int) -> list[int]:
    if y < x:
        raise ValueError("No es posible con ese orden de numeros")
    elif x == y:
        return [x]
    else:
        return [x] + desde_hasta(x+1, y)
    
def sumatoria(n):
    return sum(desde_hasta(1,n))

def factorial(n):
    res = 1
    for num in desde_hasta(1,n):
        res *= num
    return res
