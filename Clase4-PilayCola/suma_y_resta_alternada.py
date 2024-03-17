
def suma_resta_alternada(lista: list[int]) -> int:
    def suma_resta_recursiva(lista: list[int], acumulado: int, suma: bool) -> int:
        if not lista:
            return acumulado
        if suma:
            return suma_resta_recursiva(lista[1:], acumulado + lista[0], False)
        else:
            return suma_resta_recursiva(lista[1:], acumulado - lista[0], True)

    return suma_resta_recursiva(lista[1:], lista[0], False)


resultado = suma_resta_alternada([1, 2, 3, 4, 5])
print(resultado)  # Output: 1
