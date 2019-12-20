# encontrar la distancia de un movil
def distancia_movil(v,t):
    if ( isinstance(v,str)==True or isinstance(t,str)==True):
        return False
    #fin_if
    else:
        resulatado=v*t
        return resulatado
#fin_def

# pedir el peso y talla de un hombre
def peso_hombre(peso,talla):
    if (peso>0 or peso < 500 or talla>0 or talla<300):
        return False
    #fin_if
    else:
        return exit()
#fin_def

# calcular el precio total porla compra de dos productos

def precio_abarrotes(papa,mais):
    precio=0
    if (papa):
        resultado=papa*1.50
        precio+=resultado

    if(mais):
        resultado=mais*2
        precio+=resultado
    return (precio)

# si la contraseña es correcta

def contraseña(clave):
    if (clave == 123):
        res = "la clave es correcta: puede pasar"
        return res
    else:
        res = "ingrese otra clave"
        exit(res)


# el volumen de un cubo

def volumen(a,b,c):
    vol=a*b*c
    if (vol<=0):
        res=str(vol)+" error: el area no puede ser negativa"
    #fin_if
    else:
        res=str(vol)+" es area correcta"

    return (res)

#fin_def


# encontra el area d un cilindro

def area_circulo(radio,pi):
    area=pi*radio**2
    return area
#fin_def

# encontrar la fuerza de un movil

def fuerza_movil(masa,gravedad):
    if (masa<=0 or gravedad!=10):
        return False
    else:
        return masa*gravedad

    #fin_if
#fin_def


# pedir lugar de nacimiento

def lugar_nacimiento(lugar):
    if(lugar.isdigit()):
        return False

    else:
        return lugar
    #fin_if

#fin_def


# 9.-funcion==> es masculino o femenino
def ingrese_sexo(sexo):
    if(sexo=="m"):
        msg="es del tipo masculino"
        return msg
    if(sexo=="f"):
        msg="es del tipo femenino"
        return msg

#10.-funcion==> pedir nombre en que universidad estudia
def ingrese_uni(universidad):
    if(universidad=="unprg"):
        msg="estudia en la universidad nacional pedro ruiz gallo"

    if(universidad=="uni"):
        msg="estudia en la universidad nacional de ingenierias"

    return msg



#11.-funcion==> encontar el trabajo que hace un objeto en movimiento
def trabajo(fuerza,distancia):
    res=fuerza*distancia
    return res


#12.-funcion==> pedir un numero de celular
def numero_celular(msg):
    if(len(msg)==9 ):
        return msg
    else:
        return "error"
#13.-funcion ==> precio para pagar u ceviche
def ceviche_menu(cant,precio_ceviche):
    resultado=cant*precio_ceviche

    if(resultado>30):
        msg="por su compra se ha ganado un platillo gratis"
        text=msg+"====> el precio es: "+str(resultado)
        return text
    else:
        msg="gracias por su compra"

        return resultado

#14.-funcion ==> bonificacion para trabajadores
def bonificacion(contratado,horas_extra):


    if(contratado=="contratado"):
        boni=horas_extra*30
        return boni



#15.-funcion ==> formula para la energia potencialgravitatoria
def energia_gravitatoria(masa,graveadad,altura):
    resultado=masa*graveadad*altura
    return resultado

#16.-funcion ==>pedir codigo
def pedir_codigo (msg):
    if (msg[:6].isdigit()==False):
        res=msg+"no es un numero"

    else:
        ultima_letra=msg[6:]
        if (ultima_letra.isalpha()==True):
            return ("puede pasar")
        else:
            return ("el codigo no existe ")
    return res

#17.-funcion ==> pedir precio total del pasaje

def precio_pasaje(precio,cant_pasaj):
    res=precio*cant_pasaj
    return res


#18.-funcion ==> energia cinetica de un cuerpo en movimientos
def energia_cinetica(masa,velocidad):
    res=(masa*velocidad**2)/2
    return res

#19.-funcion ==> pedir nota promedio

def nota_promedio(nota1,bonus1,nota2,bonus2):
    res=(nota1+bonus1)+(nota2+bonus2)/2
    return res

#20.-funcion ==>calcular la potencia de un motor
def potencia(trabajo,tiempo):
    resultado=trabajo*tiempo
    return resultado

#21.-funcion ==> area trapecio
def area_trapecio(base_mayor,base_menor,altura):
    res=(base_menor+base_mayor)*altura/2
    return res

#22.-funcion ==> lo que gana un youtuber por el numero de vistas
def pago(num_visas,precio_vista):
    res=num_visas*precio_vista
    return res


#23.-funcion ==> el salario de un chef

def salario(dias,precio_dia):
    res=dias*precio_dia
    return res
#24.-funcion ==> el precio de un jugador
def precio_jugador(num_partidos,precio_partido):
    res=num_partidos*precio_partido
    return res

#25.-funcion ==> precio de helados
def precio_total(cant_helados,precio_helados):
    res=cant_helados*precio_helados
    return res

