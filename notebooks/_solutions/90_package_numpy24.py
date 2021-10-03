# Rescale the data to 0-1
b48_min = b48_bands.min(axis=(1, 2), keepdims=True)
b48_max = b48_bands.max(axis=(1, 2), keepdims=True)
b48_bands = ((b48_bands - b48_min)/(b48_max - b48_min))