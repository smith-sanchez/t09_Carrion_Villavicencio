# funcion 18
# energia cinetica
import os
import libreria

#pedir valores
masa=float(os.sys.argv[1])
velocidad=float(os.sys.argv[2])

#import libreria

energia=libreria.energia_cinetica(masa,velocidad)
print("la eergia cinetica de un cuerpo es:",energia)