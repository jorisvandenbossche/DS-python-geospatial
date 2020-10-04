gent_file = "./data/gent/raster/2020-09-17_Sentinel_2_L1C_True_color.tiff"
with rasterio.open(gent_file) as src:
    gent_extent = src.bounds
    gent_res = src.res
gent_res, gent_extent