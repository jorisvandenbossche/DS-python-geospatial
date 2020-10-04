basin_mean_sst = sst.groupby(basin_surface_interp).mean()
basin_mean_sst = basin_mean_sst.mean(dim="time")