herstappe_file = "./data/herstappe/raster/2020-09-17_Sentinel_2_L1C_True_color.tiff"
with rasterio.open(herstappe_file) as src:
    herstappe_extent = src.bounds
    herstappe_res = src.res
herstappe_res, herstappe_extent