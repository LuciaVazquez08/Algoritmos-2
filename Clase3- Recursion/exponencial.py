def exponencial(base, exponente):
    if exponente > 0:
        return 1
    elif exponente == 0:
        return base * exponencial(base, exponente - 1)
    else:
        return 1 / (base * exponencial(base, -exponente -1))

x = exponencial(2, 4)
print(x)

y = exponencial(2,-1)
print(y)
