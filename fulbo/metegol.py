from jugador import Jugador
from jugador import Pase

class Metegol:
    def __init__(self) -> None:
        self.jugador_actual: Jugador | None = None
        self.equipo: dict[int, Jugador] = {}

    def agregar_jugador(self, jugador: Jugador) -> None:
        self.equipo[jugador.numero] = jugador

    def set_jugador_actual(self, jugador: Jugador) -> None:
        if jugador.numero not in self.equipo:
            raise ValueError("No existe ese jugador")
        else:
            self.jugador_actual = jugador

    def pasar_pelota(self, destinatario_pase: int) -> None:
        if self.jugador_actual is None:
            raise ValueError("No hay un jugador actual")

        destino = self.jugador_actual.obtener_destino_pase(destinatario_pase)
        print(f'Pase del jugador {self.jugador_actual.numero} al jugador {destino.numero}')

        self.set_jugador_actual(destino)