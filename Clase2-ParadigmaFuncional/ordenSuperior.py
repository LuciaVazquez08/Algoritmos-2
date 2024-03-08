from typing import Callable

def wrapper(fn: Callable[[None],None], *args, **kwargs):
    fn(*args,*kwargs)
    print("Ejecutada "+fn.__name__)

def ejemplo():
    print("Eejcucion de la funcion de prueba")

def ejemplo2(mensaje):
    print(mensaje)

wrapper(ejemplo)
wrapper(ejemplo2,"ejecusion con argumentos")
