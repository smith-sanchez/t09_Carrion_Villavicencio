# encontrar el area de un circulo
import libreria
import os

# pedir las variables
radio=float(os.sys.argv[1])
# el valor de pi siempre sera el mismo
pi=3.14

area=libreria.area_circulo(radio,pi)
print("el del circulo es",area)