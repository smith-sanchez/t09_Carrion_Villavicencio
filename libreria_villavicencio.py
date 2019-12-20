# Smith- Libreria de Funciones

#1- Funcion que devuelve la resta de 2 numeros
def restar(x,y):
    return x-y


#2- Funcion que calcula la semisuma de dos numeros
def semisuma(a,b):
    return (a+b)/2


#3- Funcion que devuelve el area de un trapecio
def area_trapecio(base_mayor,base_menor, altura):
    return ((base_mayor+base_menor)/2)*altura


#4- Funcion que calcula la distancia de un cuerpo en MRU
def distancia(velocidad,tiempo):
    return velocidad*tiempo


#5- Funcion que calcula el volumen de una piramide
def volumen_piramide(area_base,altura):
    return (area_base*altura)/3


#6- Funcion que calcula el calor sensible
def calor_sensible(masa,calor_especifico,temperatura):
    return (masa*calor_especifico*temperatura)


#7- Funcion que calcula la diferencia de potencial
def diferencia_potencial(intensidad,resistencia):
    return (intensidad*resistencia)


#8- Funcion que calcula la fuerza que ejerce un cuerpo
def fuerza(masa,aceleracion):
    return (masa*aceleracion)


#9- Funcion que calcula el trabajo
def trabajo(fuerza, distancia):
    return (fuerza*distancia)


#10- Funcion que calcula la potencia mecanica
def potencia(trabajo,tiempo):
    return (trabajo/tiempo)


#11- Funcion que calcula la energia cinetica
def energ_cin(masa,velocidad):
    return ((masa*velocidad**2)/2)


#12- Funcion que calcula la energia potencial gravitatoria
def energ_gra(masa,gravedad,altura):
    return (masa*gravedad*altura)


#13- Funcion que calcula la velocidad final
def vel_fin(vel_ini,tiempo,aceleracion):
    return (vel_ini+tiempo*aceleracion)

#14- Funcion que calcula el volumen de un prisma
def vol_prisma(area_base,arista):
    return (area_base*arista)


#15- Funcion que calcula el area de una elipse
def area_elip(eje_mayor,eje_menor):
    return (eje_mayor*eje_menor)/4


#16- Funcion que calcula cualquier entero
def pedir_entero(msg):
    entero_invalido= True
    while(entero_invalido):
        valor=input(msg)
        entero_invalido=(valor.isdigit() == False)
    #fin_while
    return int(valor)
#fin_def


#17- Funcion que devuelve el numero de celular
def pedir_numero_celular(msg):
    numero_invalido = True
    valor=0
    while(numero_invalido):
        valor=pedir_entero(msg)
        numero_invalido=(valor < 100000000 or valor > 999999999)
    #fin_while
    return valor
#fin_def


#18- Funcion que devuelve el dia del mes diciembre
def pedir_dia(msg):
    dia_invalido = True
    valor=0
    while(dia_invalido):
        valor=pedir_entero(msg)
        dia_invalido=(valor < 1 or valor > 31)
    #fin_while
    return valor
#fin_def


#19- Funcion que devuelve el año que pertenece al siglo 21
def pedir_anio_sigloxxi(msg):
    anio_invalido = True
    valor=0
    while(anio_invalido):
        valor=pedir_entero(msg)
        anio_invalido=(valor < 2001 or valor > 2100)
    #fin_while
    return valor
#fin_def


#20- Funcion que devuelve clave de 5 digitos
def pedir_clave(msg):
    clave_invalido = True
    valor=0
    while(clave_invalido):
        valor=pedir_entero(msg)
        clave_invalido=(valor < 10000 or valor > 99999)
    #fin_while
    return valor
#fin_def


#21- Funcion que devuelve una palabra
def pedir_palabra(msg):
    palabra_invalido= True
    while(palabra_invalido):
        valor=input(msg)
        palabra_invalido=(valor.isalpha() == False)
    #fin_while
    return str(valor)
#fin_def


#22- Funcion que devuelve el nombre de cualquier mes
def pedir_mes(msg):
    mes_invalido = True
    valor=0
    while(mes_invalido):
        valor=pedir_palabra(msg)
        mes_invalido=(valor != "Enero" and valor != "Febrero" and valor != "Marzo" and valor != "Abril" and valor != "Mayo" and valor != "Junio" and valor != "Julio" and
                      valor != "Agosto" and valor != "Setiembre" and valor != "Octubre" and valor != "Noviembre" and valor != "Diciembre")
    #fin_while
    return valor
#fin_def


#23- Funcion que devuelve uno de mis dos nombre
def pedir_nombre(msg):
    nombre_invalido = True
    valor=0
    while(nombre_invalido):
        valor=pedir_palabra(msg)
        nombre_invalido=(valor != "Nelson" and valor != "Smith")
    #fin_while
    return valor
#fin_def


#24- Funcion que calcula el precio de motos
def precio_moto(honda,yamaha):
    valor = 0
    if (honda):
        resultado = honda*3000
        valor += resultado

    if (yamaha):
        resultado = yamaha*5000
        valor += resultado
    return (valor)


#25- Funcion que calcula el precio de electrodomesticos
def precio_electrodomesticos(hervidor,microondas,licuadora):
    valor = 0
    if (hervidor):
        resultado = hervidor*30
        valor += resultado

    if (microondas):
        resultado = microondas*500
        valor += resultado

    if (licuadora):
        resultado = licuadora*150
        valor += resultado
    return (valor)
