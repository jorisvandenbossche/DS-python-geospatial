# Read the tiff raster data
with rasterio.open("./data/gent/raster/2020-09-17_Sentinel_2_L1C_B04.tiff") as src:
    gent_data = src.read(out_dtype=float, masked=False)
    gent_extent = plotting_extent(src)