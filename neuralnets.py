


# inputs = [1, 2, 3, 4] # four inputs
# # weights is a 3x4 array -> 3 neurons, 4 weights associated to each connection
# weights = [[ 0.74864643, -1.00722027,  1.45983017,  1.34236011],
#            [-1.20116017, -0.08884298, -0.46555646,  0.02341039],
#            [-0.30973958,  0.89235565, -0.92841053,  0.12266543]]
# biases = [0, 0.3, -0.5] # each neuron has a bias


# layer_outputs = [] # we create the list that will contain the results of the processing of the neurons of the layer
# # for each neuron
# for neuron_weights, neuron_bias in zip(weights, biases):
#     # initialize output to 0
#     neuron_output = 0
#     # for each input and weight
#     for n_input, weight in zip(inputs, neuron_weights):
#         # multiply input and weight and add it to the output
#         neuron_output += n_input * weight
#     # add bias to the output
#     neuron_output += neuron_bias
#     # add the neuron result to the layer
#     layer_outputs.append(neuron_output)

# print(layer_outputs) 
# # print the result

inputs = [9,10,11,4]
weights = [[0.74864643, -1.00722027,  1.45983017,  1.34236011],[-1.20116017, -0.08884298, -0.46555646,  0.02341039],
           [-0.30973958,  0.89235565, -0.92841053,  0.12266543],[-0.30973989,  0.89239965, -0.92841953,  0.19966543]] #4x4 neural net
biases = [0, 0.1, -0.6, 0.3]

layer_gives_output = []


for nWeight, nBias in zip(weights, biases):

    output = 0

    for input, weightVal in zip(inputs, nWeight):
        output +=input * weightVal

    output+=nBias
    layer_gives_output.append(output)

print(layer_gives_output)



















# for nWeights, nBias in zip(weights, biases):

#     outputVar = 0

#     for input, weight in zip(inputs, nWeights):

#         outputVar+=input*weight

#     outputVar+=nBias

#     layer_gives_output.append(outputVar)

# print(layer_gives_output)


