def invertir(secuencia: str) -> str:
    if len(secuencia) == 0:
        return secuencia
    else:
        return secuencia[-1] + invertir(secuencia[:-1])

test = invertir("123456789")
print(test)