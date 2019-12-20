#Programa que ejecuta la diferencia de potencial
import os
import libreria_villavicencio

x=float(os.sys.argv[1])
y=float(os.sys.argv[2])

res=libreria_villavicencio.diferencia_potencial(x, y)
print("La diferencia de potencial es:",res)
