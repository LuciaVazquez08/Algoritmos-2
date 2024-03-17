def procedimiento_pares(n: int, flag = 1) -> None:
    if n == 1:
        return
    else:
        print(n-1,flag)
        procedimiento_pares(n-1,flag+1)

procedimiento_pares(56)