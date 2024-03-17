def cantidad_de_digitos(n: int) -> int:
    if abs(n) < 10 :
        return 1
    else:
        return 1 + cantidad_de_digitos(n / 10)


def reversa_num(n: int) -> int:
    if n < 0:
        return -reversa_num(-n)
    if n < 10:
        return n
    else:
        return (n % 10) * (10 ** cantidad_de_digitos(n//10)) + reversa_num(n//10)


def suma_digitos(n: int) -> int:
    if n < 0:
        return -suma_digitos(-n)
    if n < 10:
         return n
    else:
        return (n % 10) + suma_digitos(n//10)

def conjunto(n: int) -> tuple[int,int]:
    if n < 10 and n > 0:
        return n,n
    else: 
        return reversa_num(n), suma_digitos(n)

test1 = conjunto(-123)
print(test1)