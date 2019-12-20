# encontra la fuerza de un movil

import libreria
import os

# pedir variables
masa=float(os.sys.argv[1])
gravedad=float(os.sys.argv[2])
fuerza=libreria.fuerza_movil(masa,gravedad)
print("la fuerza de gravedad es",fuerza)