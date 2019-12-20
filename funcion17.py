# funcion 17
# funcion---pedir pais
import libreria
import os

# pedir variables
precio=float(os.sys.argv[1])
cant_pasaj=int(os.sys.argv[2])

precio_t=libreria.precio_pasaje(precio,cant_pasaj)
print("el precio del pasaje es:",precio_t)