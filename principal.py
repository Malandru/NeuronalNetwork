from Neurona import Neurona

red = [Neurona() for n in range(input('Total de neuronas: '))]
for n in red:
    n.conectar(red)

for n in red:
    n.leerEntradas()

for n in red:
    n.procesarEntradas()