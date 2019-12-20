# funcion 19
# funcion promdio de nota
import libreria
import os

# pedir notas
nota1=float(os.sys.argv[1])
bonus1=float(os.sys.argv[2])
nota2=float(os.sys.argv[3])
bonus2=float(os.sys.argv[4])

#import libreria
prom=libreria.nota_promedio(nota1,bonus1,nota2,bonus2)
print(" el promedio de la nota es:",prom)