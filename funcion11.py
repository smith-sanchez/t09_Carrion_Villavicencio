# funcion 11
# encontrar el trabajo que se realiza

import libreria
import os

# declaramos variables
fuerza=float(os.sys.argv[1])
distancia=float(os.sys.argv[2])
trabajo_realizado=libreria.trabajo(fuerza,distancia)
print(trabajo_realizado)