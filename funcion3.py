#calcular el precio total de abarrotes

import libreria
import os

# variables
papa=float(os.sys.argv[1])
mais=float(os.sys.argv[2])

precio_total=libreria.precio_abarrotes(papa,mais)
print(precio_total)