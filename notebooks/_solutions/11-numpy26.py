# Calculate the ndvi using the stacked data
ndvi = (b48_bands[1] - b48_bands[0])/(b48_bands[0] + b48_bands[1])