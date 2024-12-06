seaons_temp = era5_renamed["temperature_k"].groupby("time.season").mean()
# See https://github.com/pydata/xarray/issues/757 for getting well-sorted groups for plotting
seaons_temp = seaons_temp.reindex(season=['DJF','MAM','JJA', 'SON'])
seaons_temp.plot.imshow(col="season", cmap="Reds")