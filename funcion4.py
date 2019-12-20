# si la clave es la correcta

import libreria
import os

# pedir la clave

clave=int(os.sys.argv[1])
clave_correct=libreria.contraseña(clave)
print(clave_correct)