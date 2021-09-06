b4_data = xr.open_rasterio("./data/gent/raster/2020-09-17_Sentinel_2_L1C_B04.tiff").sel(band=1)
b8_data = xr.open_rasterio("./data/gent/raster/2020-09-17_Sentinel_2_L1C_B08.tiff").sel(band=1)