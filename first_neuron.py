#firt neuron network with 3 inputs

x = [1,2,3]
weights = [0.1,0.3,-0.5]
bias = 2

outputs = (x[0]*weights[0] + x[1]*weights[1] + x[2]*weights[2] + bias)
# print(outputs)

#firt neuron network with 4 inputs

x = [1.0,2.0,3.0,4.0]
weights = [0.1,0.3,-0.5,1.0]
bias = 2

outputs = (x[0]*weights[0] + 
           x[1]*weights[1] + 
           x[2]*weights[2] + 
           x[3]*weights[3] +
           bias)
# print(outputs)


#layers of neurons

input = [1, 2, 3, 2.5]

weights = [[0.2, 0.8, -0.5, 1],
 [0.5, -0.91, 0.26, -0.5],
 [-0.26, -0.27, 0.17, 0.87]]

weight0 = weights[0]
weight1 = weights[1]
weight2 = weights[2]
bias = [2, 3, 0.5]
 


outputs =[
        input[0]*weight0[0]+
        input[1]*weight0[1]+
        input[2]*weight0[2] +
        input[3]*weight0[3] + bias[0],
        input[0]*weight1[0] + 
        input[1]*weight1[1] + 
        input[2]*weight1[2] + 
        input[3]*weight1[3] + bias[1] ,
        input[0]*weight2[0] + 
        input[1]*weight2[1] + 
        input[2]*weight2[2] +
        input[3]*weight2[3] + bias[2]
] 
# print(outputs)


#using for loops
input = [1, 2, 3, 2.5]

weights = [[0.2, 0.8, -0.5, 1],
 [0.5, -0.91, 0.26, -0.5],
 [-0.26, -0.27, 0.17, 0.87]]

bias = [2, 3, 0.5]
layer_outputs = []
for neuron_weights , neuron_bias in zip(weights,bias):
    neuron_output =0 
    for n_input , n_weight in zip(input,neuron_weights):
        neuron_output += n_input * n_weight
    neuron_output+= neuron_bias
    layer_outputs.append(neuron_output)

print("FINAL OUTPUT :",layer_outputs)

   

