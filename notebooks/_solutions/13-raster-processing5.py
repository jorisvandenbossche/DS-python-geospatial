dem = xr.open_dataarray("zip://./data/gent/DHMVIIDTMRAS25m.zip", engine="rasterio", mask_and_scale=False).sel(band=1)
dem.rio.nodata