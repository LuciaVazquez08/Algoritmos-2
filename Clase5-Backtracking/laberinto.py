from random import choice

def romper(laberinto, posicion_actual, salida) -> (bool, list[list[bool]]):
    if posicion_actual == salida:
        return True, laberinto
    else:
        direcciones = ['N', 'S', 'O', 'E']
        salida_encontrada = False
        while not salida_encontrada and direcciones:
            direccion = choice(direcciones)
            direcciones.remove(direccion)
            nueva_posicion = avanzar(posicion_actual, direccion)
            if hay_muro(laberinto, nueva_posicion):
                x, y = nueva_posicion
                laberinto[x][y] = False
                salida_encontrada, laberinto = romper(laberinto, nueva_posicion, salida)
        return salida_encontrada, laberinto

def avanzar(posicion_actual, direccion) -> (int, int):
    x, y = posicion_actual
    if direccion == 'N':
        return x, y +1
    elif direccion == 'S':
        return x, y - 1
    elif direccion == 'O':
        return x - 1, y
    else: 
        return x + 1, y
    
def hay_muro(laberinto, nueva_posicion) -> bool:
    x, y = nueva_posicion
    return 0 <= x < len(laberinto) and 0 <= y < len(laberinto[0]) and laberinto[x][y]

def generar_laberinto(n: int) -> list[list[bool]]:
    laberinto = [[True for __ in range(n)] for _ in range (n)]
    laberinto[0][0] = False
    entrada = (0, 0)
    salida = (n-1,n-1)
    return romper(laberinto, entrada, salida)[1]

def recorrer(camino_previo: list[(int,int)], laberinto) -> (bool, list[(int,int)]):
    if camino_previo:
        posicion_actual = camino_previo[-1]
    else:
        posicion_actual = (0, 0)
    if es_salida(posicion_actual, laberinto):
        return True, camino_previo
    else:
        salida_encontrada = False
        direcciones = ['N', 'S', 'O', 'E']
        while direcciones and not salida_encontrada:
            nueva_posicion = avanzar(posicion_actual, direcciones.pop())
            if hay_paso(nueva_posicion, laberinto) and nueva_posicion not in camino_previo:
                camino_actual = camino_previo.copy()
                camino_actual.append(nueva_posicion)
                salida_encontrada, solucion = recorrer(camino_actual, laberinto)
            
        return salida_encontrada, solucion
    
def es_salida(posicion: (int, int), laberinto):
    x, y = posicion
    lado = len(laberinto) - 1
    return x == lado == y 
    
def hay_paso(laberinto, nueva_posicion) -> bool:
    x, y = nueva_posicion
    return 0 <= x < len(laberinto) and 0 <= y < len(laberinto[0]) and not laberinto[x][y]

laberinto = generar_laberinto(5)
for i in range(len(laberinto)):
    print(laberinto[i]) 

camino = recorrer([], laberinto)
print(camino)