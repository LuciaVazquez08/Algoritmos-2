from functools import reduce

def contar_elementos(lista):
    reducer = lambda acumulado, elemento: {**acumulado, elemento: acumulado.get(elemento,0) +1}

    return reduce(reducer, lista, {})

