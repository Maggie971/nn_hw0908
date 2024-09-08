def mcCulloch_pitts(inputs, weights, threshold):
    total_input = sum(i * w for i, w in zip(inputs, weights))
    if total_input >= threshold:
        return 1
    else:
        return 0

inputs = [1, 0, 1]  # Binary inputs
weights = [0.5, 0.5, 0.5]  # Weights for each input
threshold = 0.8  # Threshold value
output = mcCulloch_pitts(inputs, weights, threshold)
print(f"Neuron output: {output}")
