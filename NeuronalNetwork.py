from string import uppercase
from Synapse import Synapse
from Neuron import Neuron
from threading import Lock
import threading
import stdio
import copy

class NeuronalNetwork():
    def __init__(self):
        self.lock = Lock()
        self.items = stdio.readInt('Total de neuronas: ', 'x >= 1')
        self.neurons = {} #[Neuron(letter) for letter in uppercase]
        for letter in uppercase[:self.items]:
            self.neurons[letter] = Neuron(letter, self.lock)

    def run(self):
        for key in self.neurons.keys():
            self.neurons[key].readUserInputs()
            self.neurons[key].start()
        for key in self.neurons.keys():
            self.neurons[key].join()

    def initNeurons(self):
        print '\n========================'
        for key in uppercase[:self.items]:
            print '\t\t\tCONFIGURANDO NEURONA', key
            neuron = self.neurons[key]
            self.readSynapse(neuron)
            self.readConfiguration(neuron)
            self.readConnections(neuron)
        print '========================\n\n'

    def readSynapse(self, neuron):
        totalInputs = stdio.readInt('Total de entradas: ', 'x >= 1')
        neuron.synapse.setTotalInputs(totalInputs)

    def readConfiguration(self, neuron):
        print '--> Umbrales <--'
        while(True):
            condition = stdio.readExpression('Condicion: ', bool)
            if condition == None: break
            returnValue = stdio.readExpression('Valor de retorno: ', float) 
            if returnValue == None: break
            neuron.bias[condition] = returnValue
        print '--> Funcion de activacion <--'
        neuron.function = stdio.readExpression('f(x) = ', float)

    def readConnections(self, neuron):
        print '--> Conexiones <--'
        string = raw_input('Neuronas: ')
        connetions = string.split()
        totalConnections = 0
        for conn in connetions:
            if totalConnections > 4: break
            try:
                branch = self.neurons[conn].synapse
                branch.addNetworkInput() # Se le dice a la neurona que quite una entrada de usuario
                neuron.branches.append(branch)
                totalConnections += 1
                print 'Conexion [{}] agregada'.format(conn)
            except KeyError:
                print 'Conexion [{}] inexistente'.format(conn)
        if totalConnections == 0:
            print 'Sin conexiones'