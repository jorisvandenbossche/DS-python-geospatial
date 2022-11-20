xr_b4_data = xr.open_dataarray("./data/gent/raster/2020-09-17_Sentinel_2_L1C_B04.tiff", 
                               engine="rasterio", mask_and_scale=False)
b4_data = xr_b4_data.data
xr_b8_data = xr.open_dataarray("./data/gent/raster/2020-09-17_Sentinel_2_L1C_B08.tiff", 
                               engine="rasterio", mask_and_scale=False)
b8_data = xr_b8_data.data

# Get extent
(left, bottom, right, top) = xr_b4_data.rio.bounds()
b4_data_extent = (left, right, bottom, top)