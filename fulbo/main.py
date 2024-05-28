from metegol import Metegol
from jugador import Jugador
from jugador import Pase

metegol = Metegol()

jugador10 = Jugador(10, "delantero10", {})
jugador11 = Jugador(11, "delantereo11", {10:jugador10})
jugador9 = Jugador(9,"delantero9", {10:jugador10})

jugador8 = Jugador(8, "central8", {9: jugador9, 10: jugador10, 11:jugador11})
jugador6 = Jugador(6, "central6", {9: jugador9, 10: jugador10, 11:jugador11})
jugador5 = Jugador(5, "central5", {9: jugador9, 10: jugador10, 11:jugador11, 7: jugador6})
jugador7 = Jugador(7, "central7", {9: jugador9, 10: jugador10, 11:jugador11, 8: jugador8, 5: jugador5})

jugador4 = Jugador(4, "defenso4", {8:jugador8, 6:jugador6})
jugador3 = Jugador(3, "defensor3", {7:jugador7, 5:jugador5})
jugador2 = Jugador(2,"defensor2", {4:jugador4, 3:jugador3})

jugador1 = Jugador(1, "arquero", {10: jugador10, 2:jugador2, 3:jugador3, 4:jugador4, 5: jugador5, 8:jugador8})

#etc...
