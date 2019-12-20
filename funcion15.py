# funcion 15
#forrmula para saaber la energia gravitatoria de un cuerpo
import libreria
import os

#variables
masa=float(os.sys.argv[1])
gravedad=float(os.sys.argv[2])
altura=float(os.sys.argv[3])

energia=libreria.energia_gravitatoria(masa,gravedad,altura)
print("la energia potencial gravitatoria es:",energia)