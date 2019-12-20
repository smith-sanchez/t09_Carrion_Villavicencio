#Programa que ejecuta la energia cinetica
import os
import libreria_villavicencio

masa=float(os.sys.argv[1])
vel=float(os.sys.argv[2])

res=libreria_villavicencio.energ_cin(masa, vel)
print("La energia cinetica es igual a:",res)
