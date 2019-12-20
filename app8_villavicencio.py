#Programa que ejecuta la fuerza
import os
import libreria_villavicencio

masa=float(os.sys.argv[1])
acel=float(os.sys.argv[2])

res=libreria_villavicencio.fuerza(masa, acel)
print("La fuerza que ejerce el cuerpo es:",res)

