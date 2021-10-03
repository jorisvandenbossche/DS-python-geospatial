# Apply function to a single file 
resample_raster_file("./data/gent/raster/2020-09-17_Sentinel_2_L1C_B04.tiff", 
                     "b4_out.tiff", Resampling.bilinear, scaling_factor=2)