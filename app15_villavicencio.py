#Programa que ejecuta el area de una elipse
import os
import libreria_villavicencio

eje1=float(os.sys.argv[1])
eje2=float(os.sys.argv[2])

res=libreria_villavicencio.area_elip(eje1, eje2)
print("El area de la elipse es:",res)
