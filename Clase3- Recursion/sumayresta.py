def sumar1(lista : list[int]) -> int:
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + restar1(lista[1:])

def restar1(lista : list[int]) -> int:
    if len(lista) == 0:
        return 0
    else:
        return - lista[0] + sumar1(lista[1:])

lista = [1,2,3]

print(restar1(lista))