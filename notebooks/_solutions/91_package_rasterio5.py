# Stack both data sets and convert to uint32 data (#2)
b48_bands = np.vstack((b4_data, b8_data))  # 0 is b4 and 1 is b8  
b48_bands = b48_bands.astype("uint32")
b48_bands.shape