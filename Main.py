from NeuronalNetwork import NeuronalNetwork
from os import system

def addNetwork(networks):
    system('clear')
    print '\t\t\tCREANDO UNA NUEVA RED'
    name = raw_input('Nombre de la red: ')
    networks[name] = NeuronalNetwork()
    networks[name].initNeurons()

def useNetwork(networks):
    system('clear')
    if networks.keys() == []:
        print 'No hay redes creadas'
        return
    print '== Redes disponibles ==\n'
    for key in networks.keys():
        print '->', key
    try:
        name = raw_input('Eliga una opcion [menu/nombre]: ')
        networks[name]
        system('clear')
        print 'Red en ejecucion: [{}]'.format(name)
        networks[name].run()
    except KeyError:
        system('clear')

def main():
    networks = {}
    while True:
        print '\n\t\t\tREDES NEURONALES'
        print '1. Crear una nueva red'
        print '2. Usar una red'
        print '3. Cualquier tecla para salir'
        option = input('Eliga una opcion: ')
        if 1 == option: addNetwork(networks)
        elif 2 == option: useNetwork(networks)
        else: break

main()