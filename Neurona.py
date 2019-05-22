from stdio import *
from math import asin, atan, isnan
from threading import Thread

class Neurona(Thread):
    def __init__(self):
        self.x = [] # Entradas
        self.w = [] # Pesos
        self.s = -1 # Salidas
        self.conexiones = [] # ["Neurona"]
        self.inicializar() # Inicializa las variables anteriores
        # Umbrales y funcion de transicion
        self.funcion = ''
        self.umbrales = {} # {"cond": "return"}
        self.leerUmbrales()
        print self.umbrales
        # Conexiones a otras neuronas
        self.leerConexiones()
        print self.conexiones

    def procesarEntradas(self):
        productos = [self.x[i] * self.w[i] for i in range(len(self.x))]
        x = sum(productos)
        self.s = eval(self.funcion)

    def enviarSalidas(self, red=dict):
        for conx in self.conexiones:
            red[conx].agregarEntrada(float('nan'), self.s)

    def conectar(self, neuronas):
        try:
            for conx in self.conexiones:
                neuronas[conx].agregarEntrada(None, float('nan'))
        except KeyError:
            print 'Neurona [{}] no existe'.format(conx)

    def leerEntradas(self):
        i, lim = 0, len(self.x)
        while i < lim:
            if self.x[i] == None:
                self.x[i] = input('Entrada: ')
            i += 1

    def run(self):
        self.conectar()

#########################################################
########### FUNCIONES UTILIZADAS LOCALMENTE #############
#########################################################
    def inicializar(self):
        n = leerInt('Numero de entradas: ', '1 <= x <= 4')
        self.x = [None for i in range(n)] # Total de entradas
        self.w = [1 for i in range(n)] # Pesos de las entradas
        self.s = leerInt('Numero de salidas: ', '1 <= x <= 4') # Total de salidas
        self.conexiones = [None for i in range(n)] # Crear ese pull de conexiones
        print '\n\t\t\tFUNCION'
        self.funcion = leerExpresion('f(x) = ', float)

    def leerUmbrales(self):
        print '\n\t\t\tUMBRALES'
        print 'Los umbrales se definen bajo la variable [s].'
        print 'Dicha regla aplica para <Condicion> y <Valor de retorno>.'
        print """\nEjemplo
================================
        Condicion: s < 1
        Valor de retorno: 0.0
        Condicion: s > 1
        Valor de retorno: s * s
================================"""
        print 'Ingrese [continuar] para establecer la conectividad\n'
        while(True):
            cond = leerExpresion('Condicion: ', bool)
            if cond == None: break
            retorno = leerExpresion('Valor de retorno: ', float) 
            if retorno == None: break
            self.umbrales[cond] = retorno

    def leerConexiones(self):
        print '\n\t\t\tCONEXIONES'
        i = 0
        while i < self.s:
            msg = 'La salida #{} se conecta con la neurona: '
            neurona = leerLetra(msg.format(i))
            self.conexiones[i] = neurona
            i += 1

    def agregarEntrada(self, old, new):
        try:
            i = self.x.index(old)
            self.x[i] = new
        except ValueError:
            print 'Excedente de entradas'