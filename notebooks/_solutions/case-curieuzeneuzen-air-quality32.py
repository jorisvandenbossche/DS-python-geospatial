import rasterio
import rasterio.plot

with rasterio.open("data/CLC2018_V2020_20u1_flanders.tif") as src:
    print(src.meta)
    rasterio.plot.show(src)