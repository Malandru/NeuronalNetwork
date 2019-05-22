from math import asin, atan
from threading import Thread
from Synapse import Synapse
import numpy as np

class Neuron(Thread):
    def __init__(self, name, lock):
        Thread.__init__(self, args=(lock))
        self.name = name
        self.synapse = Synapse(lock) # Se va a encargar de recoger las entradas y los pesos
        self.inputs = []
        self.weights = []
        self.bias = {} # {"cond": "return value"}
        self.output = float('nan')
        self.function = 'x' # f(x) = x
        self.branches = [] # Synapses listening

    def setFunction(self, function):
        self.function = function

    def readUserInputs(self):
        if self.synapse.userInputs > 0:
            print '\t\t\tENTRADAS DE NEURONA', self.name
            self.synapse.readUserInputs()

    def run(self):
        while not self.synapse.allInputsReady(): pass
        self.inputs = self.synapse.getInputs()
        self.weights = self.synapse.getWeights()
        self.processInputs()


    def processInputs(self):
        s = np.dot(self.inputs, self.weights)
        x = float('nan')
        for cond in self.bias:
            if eval(cond):
                x = eval(self.bias[cond])
                break
        else: x = s
        self.output = eval(self.function)
        if self.branches == []: print self.output
        else: self.sendOutput()

    def sendOutput(self):
        index, lim = 0, len(self.branches)
        while index < lim:
            self.branches[index].addInputValue(self.output)
            index += 1