seaons_temp = era5_renamed["temperature_k"].groupby("time.season").mean()
# See https://github.com/pydata/xarray/issues/757 for getting well-sorted groups for plotting
seaons_temp = seaons_temp.sortby(xr.DataArray(['DJF','MAM','JJA', 'SON'], dims=['season']))
seaons_temp.plot.imshow(col="season", cmap="Reds")