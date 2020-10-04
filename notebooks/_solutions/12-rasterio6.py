# Update profile metadata (#3) and save to a new tiff file (#4)
data_profile.update({"count": 2, 
                     "dtype": "uint32"})  #3

with rasterio.open("./B0408.tiff", "w", **data_profile) as dst: #4
    dst.write(b48_bands)