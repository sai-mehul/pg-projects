import numpy as np 
import matplotlib.pyplot as plt 

class NN_V1:
    def __init__(self,layers,seed):
        np.random.seed(seed)
        self.layers = layers 
        self.weights = self.__init_weights()
        self.biases = self.__init_biases()
        
    def __init_weights(self):
        w = []
        for i in range(len(self.layers)-1):
            w.append(np.random.randn(self.layers[i+1],self.layers[i]))
        return w      
    
    def __init_biases(self):
        b = []
        for i in range(len(self.layers)-1):
            b.append(np.random.randn(self.layers[i+1],1))
        return b
    
    def activation_function(self,data):
        return 1/(1+np.exp(-data))
    
    def feed(self,data):
        I = []
        A = data 
        for i in range(len(self.weights)):
            A = (np.dot(self.weights[i],A)+self.biases[i])
            A = self.activation_function(A)
            I.append(A)
        return I


N = [2, 3, 3, 2, 1]
model = NN_V1(N,123)
data = np.array([0.6, 0.9])
layer_outputs = model.feed(data)


for i,out in enumerate(layer_outputs,1):
    print(f'Layer {i}:{out}\n')