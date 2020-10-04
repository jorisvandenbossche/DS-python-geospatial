gent_file = "./data/gent/raster/2020-09-17_Sentinel_2_L1C_True_color.tiff"
with rasterio.open(gent_file) as gent_gif:
    gent = gent_gif.read([1]) # only read the first band/layer
    show(gent, transform=gent_gif.transform)