#Programa que ejecuta el volumen de un prisma
import os
import libreria_villavicencio

a_base=float(os.sys.argv[1])
ari=float(os.sys.argv[2])

m=libreria_villavicencio.vol_prisma(a_base, ari)
print("El volumen del prisma es:",m)
