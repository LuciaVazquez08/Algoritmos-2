def cociente(n1, n2):
    if n1 < n2:
        return 0
    else:
        return 1 + cociente(n1 - n2, n2)

def resto(n1, n2):
    if n1 < n2:
        return n1
    else:
        return resto(n1 - n2, n2)


num1 = 21
num2 = 3

print("Cociente:", cociente(num1, num2))
print("Resto:", resto(num1, num2))
