from math import asin, atan

def readInt(msg, domain):
    while True:
        try:
            x = raw_input(msg)
            if x == 'continuar': return None
            x = int(x)
            if eval(domain):
                return x
            else:
                print '\nError: Fuera de rango [{}]'.format(domain)
        except NameError:
            print '\nError: Tienes que ingresar un numero'
        print 'Intenta de nuevo...'

def readExpression(msg, desiredType):
    s, x = 0.0, 0.0
    while True:
        expression = raw_input(msg)
        try:
            if expression == 'break': return None
            typeValue = type(eval(expression))
            if typeValue == int: typeValue = float
            if typeValue == desiredType:
                return expression
        except:
            print '\nError: Favor de leer las reglas'
            print 'Intente de nuevo...'