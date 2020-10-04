gdf_lambert = gdf.to_crs("EPSG:31370")  # or .to_crs(muni.crs)
gdf_lambert.head()