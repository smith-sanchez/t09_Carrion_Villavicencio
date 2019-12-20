#Programa que ejecuta el resultado del calor sensible
import os
import libreria_villavicencio

m=int(os.sys.argv[1])
n=int(os.sys.argv[2])
l=int(os.sys.argv[3])

res=libreria_villavicencio.calor_sensible(m, n, l)
print("El calor sensible es:",res)
