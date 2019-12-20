# funcion24
# precio de un jugador

import libreria
import os

#import os

num_partidos=int(os.sys.argv[1])
precio_partido=float(os.sys.argv[2])

#import libreria
precio_total_jugador=libreria.precio_jugador(num_partidos,precio_partido)
print("el precio que gana el jugador es:",precio_total_jugador)
