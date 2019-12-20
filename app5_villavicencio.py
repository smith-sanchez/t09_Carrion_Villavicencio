#Funcion que ejecuta el volumen de una piramide
import os
import libreria_villavicencio

x=int(os.sys.argv[1])
y=int(os.sys.argv[2])

res=libreria_villavicencio.volumen_piramide(x, y)
print("El volumen de la piramide es:",res)
