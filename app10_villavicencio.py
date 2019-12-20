#Programa que ejecuta la potencia mecanica
import os
import libreria_villavicencio

trabajo=float(os.sys.argv[1])
tiempo=float(os.sys.argv[2])

res=libreria_villavicencio.potencia(trabajo, tiempo)
print("La potencia mecanica es igual a:",res)
