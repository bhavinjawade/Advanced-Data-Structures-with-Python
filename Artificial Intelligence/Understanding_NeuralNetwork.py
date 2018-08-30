from numpy import exp, array, random, dot

class NeuralNetwork:
    
    def __init__(self):
        self.weights = 2 * random.random((3, 1)) - 1
    
    def sigmoid(self,x):
        return 1 / (1 + exp(-x))
    
    def sigmoidgradientcurve(self,x):
        return x * (1-x)

    
    def think(self, inputs):
        return self.sigmoid(dot(inputs, self.weights))

    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        for iteration in range(number_of_training_iterations):
            output = self.think(training_set_inputs)
            error = training_set_outputs - output
            adjustment = dot(training_set_inputs.T, error * self.sigmoidgradientcurve(output))
            self.weights += adjustment
    
iterations = 100000
neural_network = NeuralNetwork()
print("Inital weights: (Random)")
print(neural_network.weights)
training_set_inputs = array([[0, 0, 1], [1, 1, 0], [1, 0, 1], [1, 0, 1]])
training_set_outputs = array([[0, 1, 1, 0]]).T
neural_network.train(training_set_inputs, training_set_outputs, iterations)
print("Weights after %d interations", (iterations))
print(neural_network.weights)
print("Considering new situation [1, 0, 0] -> ?: ")
print(neural_network.think(array([1, 0, 0])))