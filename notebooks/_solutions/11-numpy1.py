with rasterio.open("./data/gent/raster/2020-09-17_Sentinel_2_L1C_True_color.tiff") as src:
    tc_data = src.read()