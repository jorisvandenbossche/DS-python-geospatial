xr_herstappe_data = xr.open_dataarray("./data/herstappe/raster/2020-09-17_Sentinel_2_L1C_True_color.tiff", 
                                      engine="rasterio", mask_and_scale=False)
herstappe_data = xr_herstappe_data.data

(left, bottom, right, top) = xr_herstappe_data.rio.bounds()
herstappe_extent = (left, right, bottom, top)