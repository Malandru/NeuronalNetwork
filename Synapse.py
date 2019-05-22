from stdio import readExpression

class Synapse():
    def __init__(self, lock):
        self.lock = lock
        self.netInputs = 0
        self.userInputs = None

    def setTotalInputs(self, totalInputs):
        self.userInputs = totalInputs - self.netInputs
        self.inputs = [None for i in range(totalInputs)]
        self.weights = [1.0 for i in range(totalInputs)]

    def readUserInputs(self):
        nInput = 0
        while nInput < self.userInputs:
            msg = 'Valor de entrada [{}]: '.format(nInput + 1)
            value = float(input(msg))
            self.addInputValue(value)
            nInput += 1

    def addNetworkInput(self):
        if self.userInputs != None:
            self.userInputs -= 1
        self.netInputs += 1

    def addInputValue(self, value): # void
        self.lock.acquire()
        try:
            i = self.inputs.index(None)
            self.inputs[i] = value
        except ValueError:
            print 'Entradas mal configurdas, no espere el resultado deseado'
        self.lock.release()

    def allInputsReady(self): # boolean
        return (None not in self.inputs)

    def getInputs(self): # list
        return self.inputs

    def resetInputs(self):
        index, lim = 0, len(self.inputs)
        while index < lim:
            self.inputs[index] = None
            index += 1

    def getWeights(self): # list
        return self.weights