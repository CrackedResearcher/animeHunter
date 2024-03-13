
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


