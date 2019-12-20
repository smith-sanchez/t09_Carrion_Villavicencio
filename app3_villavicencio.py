#Programa que ejecuta el area de un trapecio
import libreria_villavicencio
import os

ma=int(os.sys.argv[1])
me=int(os.sys.argv[2])
h=int(os.sys.argv[3])

res=libreria_villavicencio.area_trapecio(ma, me, h)
print("El area del trapecio es:",res)
