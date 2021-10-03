with rasterio.open("./data/gent/raster/2020-09-17_Sentinel_2_L1C_B04.tiff") as src:
    b4_data = src.read()