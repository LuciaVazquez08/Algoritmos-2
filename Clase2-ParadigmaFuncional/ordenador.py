from functools import reduce

def orden(lista):
    def ordenar(acumulado, elemento):
        index = 0
        while index < len(acumulado) and acumulado[index] < elemento:
            index += 1
        acumulado.insert(index, elemento)
        return acumulado
    return reduce(ordenar, lista[1:], [lista[0]])

lista_numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 15, -1 , 0 , -4.5]
lista_ordenada = orden(lista_numeros)
print(lista_ordenada)

