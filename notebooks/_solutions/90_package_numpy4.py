xr_tc_data = xr.open_dataarray("./data/gent/raster/2020-09-17_Sentinel_2_L1C_True_color.tiff", 
                               engine="rasterio", mask_and_scale=False)
tc_data = xr_tc_data.data    