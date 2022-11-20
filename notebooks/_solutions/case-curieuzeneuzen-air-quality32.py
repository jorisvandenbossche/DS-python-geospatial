import xarray

raster = xarray.open_dataarray("data/CLC2018_V2020_20u1_flanders.tif", engine="rasterio", mask_and_scale=False)
raster