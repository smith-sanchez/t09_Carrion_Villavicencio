#Programa que ejecuta el trabajo
import os
import libreria_villavicencio

fuerza=float(os.sys.argv[1])
distancia=float(os.sys.argv[2])

res=libreria_villavicencio.trabajo(fuerza, distancia)
print("El trabajo es igual a:",res)
