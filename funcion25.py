# funcion 25
# precio de helados

import libreria
import os

# import os

cant_helados=int(os.sys.argv[1])
precio_helados=float(os.sys.argv[2])

#import libreria
precio_total_h=libreria.precio_total(cant_helados,precio_helados)
print(" el precio total de helados es:",precio_total_h)