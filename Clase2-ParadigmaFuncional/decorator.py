from typing import Callable, TypeVar, Union

T = TypeVar('T')
S = TypeVar('S')

def acepta_no_valor(func: Callable[[T], S]) -> Callable[[T | None], S | None]:
    def fnc(arg: T | None) -> S | None:
        if arg is not None:
            return func(arg)
        else:
            return None
    return fnc


@acepta_no_valor
def inversa(x: int) -> int:
    return -x 

print(inversa(5))  
print(inversa(None))  
