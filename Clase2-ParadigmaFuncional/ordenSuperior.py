from typing import Callable

def wrapper(fn: Callable[[None],None], *args, **kwargs):
    fn(*args,*kwargs)
    print("Ejecutada "+fn.__name__)

def ejemplo():
    print("Ejcucion de la funcion de prueba")

def ejemplo2(mensaje):
    print(mensaje)

wrapper(ejemplo)
print("")
wrapper(ejemplo2,"ejecutada con argumentos")
