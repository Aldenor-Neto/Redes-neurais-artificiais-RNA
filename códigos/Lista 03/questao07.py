import numpy as np

class MLP:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        self.weights_input_hidden = np.random.randn(self.input_size, self.hidden_size)
        self.weights_hidden_output = np.random.randn(self.hidden_size, self.output_size)
        
        self.bias_input_hidden = -1
        self.bias_hidden_output = -1
        
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def forward(self, inputs):
        hidden_sum = np.dot(inputs, self.weights_input_hidden) + self.bias_input_hidden
        hidden_output = self.sigmoid(hidden_sum)
        
        output_sum = np.dot(hidden_output, self.weights_hidden_output) + self.bias_hidden_output
        output = self.sigmoid(output_sum)
        
        return output
    
mlp = MLP(input_size=2, hidden_size=2, output_size=1)

input_examples = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
for example in input_examples:
    output = mlp.forward(example)
    print(f"Entrada: {example}, Saída: {output}")
