import numpy as np

class MLP:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        self.weights_input_hidden = np.random.randn(self.input_size + 1, self.hidden_size)
        self.weights_hidden_output = np.random.randn(self.hidden_size + 1, self.output_size)
        
        self.bias_input_hidden = -1
        self.bias_hidden_output = -1
        
    def tanh(self, x):
        return np.tanh(x)
    
    def forward(self, inputs):
        inputs_with_bias = np.append(inputs, 1)
        
        hidden_sum = np.dot(inputs_with_bias, self.weights_input_hidden)
        hidden_output = self.tanh(hidden_sum)
        
        hidden_output_with_bias = np.append(hidden_output, self.bias_hidden_output)
        
        output_sum = np.dot(hidden_output_with_bias, self.weights_hidden_output)
        output = self.tanh(output_sum)
        
        return output
    
mlp = MLP(input_size=3, hidden_size=2, output_size=1)

input_examples = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], 
                            [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])
for example in input_examples:
    output = mlp.forward(example)
    print(f"Entrada: {example}, Saída: {output}")
