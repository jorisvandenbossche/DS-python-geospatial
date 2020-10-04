with rasterio.open("./data/herstappe/raster/2020-09-17_Sentinel_2_L1C_True_color.tiff") as src:
    herstappe_data = src.read()
    herstappe_extent = plotting_extent(src)