# encontrar la distancia de un movil

import libreria
import os

#variables
v=(os.sys.argv[1])
t=float(os.sys.argv[2])

distancia=libreria.distancia_movil(v,t)
print("la distancia que recorrio el movil es:",distancia)