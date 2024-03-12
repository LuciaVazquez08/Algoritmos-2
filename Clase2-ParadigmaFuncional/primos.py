from math import isqrt

def generadoraPrimos():
    yield 2  
    primos = [2]  
    num = 3  
    
    while True:
        flag = True
        for p in primos:
            if p < isqrt(num):  
                if num % p == 0:
                    flag = False
        if flag:
            primos.append(num)
            yield num
        num += 2 

primes_generator = generadoraPrimos()

for _ in range(100):
    print(next(primes_generator))             