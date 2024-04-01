import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

weights = {
    'h1': {'bias': -1, 'x1': 0.2, 'x2': -0.1, 'x3': 0.4},
    'h2': {'bias': -1, 'x1': 0.7, 'x2': -1.2, 'x3': 1.2},
    'o1': {'bias': -1, 'h1': 1.1, 'h2': 0.1},
    'o2': {'bias': -1, 'h1': 3.1, 'h2': 1.17}
}

def mlp(input_vector):
    h1_sum = weights['h1']['bias'] + sum(weights['h1'][f'x{i+1}'] * input_vector[i] for i in range(len(input_vector)))
    h1_output = sigmoid(h1_sum)

    h2_sum = weights['h2']['bias'] + sum(weights['h2'][f'x{i+1}'] * input_vector[i] for i in range(len(input_vector)))
    h2_output = sigmoid(h2_sum)

    o1_sum = weights['o1']['bias'] + weights['o1']['h1'] * h1_output + weights['o1']['h2'] * h2_output
    o1_output = sigmoid(o1_sum)

    o2_sum = weights['o2']['bias'] + weights['o2']['h1'] * h1_output + weights['o2']['h2'] * h2_output
    o2_output = sigmoid(o2_sum)

    if o1_output >= o2_output:
        return 1
    else:
        return 2

inputs = [[10, 12, -9], [-2, 3, 30]]

for example in inputs:
    predicted_class = mlp(example)
    print(f"A classe estimada para o exemplo {example} é: {predicted_class}")
