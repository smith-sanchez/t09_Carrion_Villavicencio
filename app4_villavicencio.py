#Programa que ejecuta la distancia
import os
import libreria_villavicencio

m=int(os.sys.argv[1])
n=int(os.sys.argv[2])

res=libreria_villavicencio.distancia(m, n)
print("La distancia que recorre el cuerpo es:",res)
