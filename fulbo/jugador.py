class Jugador:
    def __init__(
            self,
            numero: int,
            posicion: str
         ) -> None:
        
        self.numero = numero
        self.posicion = posicion
        self.pases_posibles: dict[int, Pase] = {}

    def agregar_Pase(self, numero_jugador: int, destino: "Jugador"):
        self.pases_posibles[numero_jugador] = Pase(numero_jugador, destino)
    
    def obtener_destino_pase(self, numero: int) -> "Jugador":
        if numero not in self.pases_posibles:
            raise ValueError('Pase inexistente')
        
        return self.pases_posibles[numero].get_destino()

    def __str__(self):
        return f'''
        Jugador {self.numero}\n 
        ------------------------------ \n
        {self.posicion} \n
        ------------ \n
        <pases_posibles>: {list(self.pases_posibles.keys())}
        '''

class Pase:
    def __init__(self, numero_jugador: int, destino: Jugador) -> None:
        self.numero_jugador = numero_jugador
        self.destino = destino

    def get_destino(self) -> Jugador:
        return self.destino

    def __str__(self) -> str:
        return f'Pase al jugador {self.numero_jugador}'