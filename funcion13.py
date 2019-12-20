# precio total de un menu
import libreria
import os

#pedir ceviche
cant=int(os.sys.argv[1])
precio_ceviche=float(os.sys.argv[2])
precio_total=libreria.ceviche_menu(cant,precio_ceviche)
print(precio_total)