land_use = xr.open_dataarray("data/CLC2018_V2020_20u1_flanders.tif").sel(band=1)
land_use