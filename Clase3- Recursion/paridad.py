def es_par(n: int) -> bool:
    if n < 0:
        return es_par(-n)
    if n == 0:
        return True
    else:
        return es_impar(n - 1)

def es_impar(n: int) -> bool:
    if n < 0:
        return es_impar(-n)
    if n == 0:
        return False
    else:
        return es_par(n - 1)

test = es_par(-2)
test1 = es_impar(-2)

print(test)
print(test1)