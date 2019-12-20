#Programa que ejecuta la velocidad final de un movil
import os
import libreria_villavicencio

vel_ini=float(os.sys.argv[1])
tie=float(os.sys.argv[2])
acel=float(os.sys.argv[3])

m=libreria_villavicencio.vel_fin(vel_ini, tie, acel)
print("La velocidad final de un movil es:",m)
