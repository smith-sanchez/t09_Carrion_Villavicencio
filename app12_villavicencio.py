#Programa que ejecutala energia gravitatoria
import os
import libreria_villavicencio

masa=float(os.sys.argv[1])
gravedad=float(os.sys.argv[2])
altura=float(os.sys.argv[3])

res=libreria_villavicencio.energ_gra(masa, gravedad, altura)
print("La energia gravitatoria es:",res)
