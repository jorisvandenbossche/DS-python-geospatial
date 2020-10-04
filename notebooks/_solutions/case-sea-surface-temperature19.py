# In such a situation, the ELLIPSIS can be used to aggregate over all dimensions
basin_mean_sst = sst.groupby(basin_surface_interp).mean(dim=...) # ellipsis is shortcut for all dimensions
basin_mean_sst