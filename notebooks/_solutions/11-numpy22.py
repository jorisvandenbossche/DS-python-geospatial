with rasterio.open("./data/gent/raster/2020-09-17_Sentinel_2_L1C_B04.tiff") as src:
    b4_data = src.read()
    b4_extent = plotting_extent(src)
with rasterio.open("./data/gent/raster/2020-09-17_Sentinel_2_L1C_B08.tiff") as src:
    b8_data = src.read() 