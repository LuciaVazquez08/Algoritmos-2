def suma_resta_alternada(lista: list[int]) -> int:
    def suma_interna(lista, acumulado):
        if not lista:
            return acumulado
        else:
            return  resta_interna(lista[1:],acumulado + lista[0])
    def resta_interna(lista, acumulado):
        if not lista:
            return acumulado
        else:
            return  suma_interna(lista[1:], acumulado - lista[0])
    return suma_interna(lista,0)

print(suma_resta_alternada([1,2,3,4,5]))    