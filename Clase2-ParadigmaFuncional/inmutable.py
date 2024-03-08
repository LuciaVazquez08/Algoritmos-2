from collections import namedtuple
from dataclasses import dataclass

class ConjuntoInmutableProperty:
    def __init__(self, *elementos):
        self._elementos = list(elementos)

        @property
        def elementos(self):
            return self._elementos 

inmutablep = ConjuntoInmutableProperty(2,3,4)

# anda  a chequear
class ConjuntoInmutableSetattr:
    __slots__ = ('_elementos')

    def __init__(self, *elementos) -> None:
        super().__setattr__('_elementos', list(elementos))
    
    def __setattr__(self, name, value) -> None:
        raise AttributeError(f'No es posible setear el atributo {name}')

    def __delattr__(self, name) -> None:
        raise AttributeError(f'No es posible eliminar el atributo {name}')
    
    def elementos(self):
        return self._elementos

inmutables = ConjuntoInmutableSetattr(1,2,3)
print(inmutables.elementos)

class ConjuntoInmutableTupla(namedtuple("ConjuntoInmutableTupla", "elemento1 elemento2")):
    __slots__ = ()
    def __repr__(self) -> str:
        return f"{super().__repr__()} INMUTABLE"

