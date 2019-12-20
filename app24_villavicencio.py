#Programa que ejecuta el total de precio de motos
import os
import libreria_villavicencio

honda=int(os.sys.argv[1])
yamaha=int(os.sys.argv[2])

total=libreria_villavicencio.precio_moto(honda, yamaha)
print(total)
