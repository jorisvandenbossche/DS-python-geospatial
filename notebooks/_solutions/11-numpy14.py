# Calculate the min and max for each channel
h_min = herstappe_data.min(axis=(1, 2), keepdims=True)
h_max = herstappe_data.max(axis=(1, 2), keepdims=True)