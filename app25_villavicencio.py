#Programa que ejecuta el total de precio de electredomesticos
import os
import libreria_villavicencio

her=int(os.sys.argv[1])
micro=int(os.sys.argv[2])
lic=int(os.sys.argv[3])

total=libreria_villavicencio.precio_electrodomesticos(her, micro, lic)
print(total)
