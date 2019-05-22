from math import asin, atan

def leerInt(msg, rango):
    while True:
        try:
            x = raw_input(msg)
            if x == 'continuar': return None
            x = int(x)
            if eval(rango):
                return x
            else:
                print '\nError: Fuera de rango [{}]'.format(rango)
        except NameError:
            print '\nError: Tienes que ingresar un numero'
        print 'Intenta de nuevo...'

def leerExpresion(msg, tipo):
    s, x = 0.0, 0.0
    while True:
        expresion = raw_input(msg)
        try:
            if expresion == 'continuar': return None
            if type(eval(expresion)) == tipo:
                return expresion
        except:
            print '\nError: Favor de leer las reglas'
            print 'Intente de nuevo...'

def leerLetra(msg):
    while True:
        letra = raw_input(msg)
        if letra.isalpha():
            return letra[0].upper()
        print '\nError: Ingresa una letra'