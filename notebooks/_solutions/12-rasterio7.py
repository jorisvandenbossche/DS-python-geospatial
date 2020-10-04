# Create a custom function
def resample_raster_file(input_file, output_file, resampling_method, scaling_factor=2):
    """Resample a raster file with a given scaling factor using rasterio
    
    Parameters
    ----------
    input_file : str | Path
        Input raster file to resample
    output_file : str | Path
        Output raster file
    resampling_method : rasterio.Resampling
        Method available in the Resampling module of rasterio, e.g. Resampling.bilinear
    scaling_factor : float, default 2
        Scaling factor to use for resampling the data
    
    Examples
    --------
    >>> resample_raster_file("./input_file.tiff", "output_file.tiff", 
    ...                      Resampling.bilinear, scaling_factor=3)
    """
    with rasterio.open(input_file) as src:  
        
        # resample data to target shape
        new_width = int(src.width / scaling_factor)
        new_height = int(src.height / scaling_factor)
        out_image = src.read(
            out_shape=(src.count, new_height, new_width),
            resampling=resampling_method  #Resampling.bilinear
        )

        # scale image transform and update metadata  # 3
        data_profile = src.profile
        out_transform = src.transform * src.transform.scale(scaling_factor)
        data_profile.update({"height": new_height,
                             "width": new_width,
                             "transform": out_transform})      

        # save the output to disk # 4
        with rasterio.open(output_file, "w", **data_profile) as dst:
            dst.write(out_image)    