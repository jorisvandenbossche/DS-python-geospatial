map_proj = ccrs.Orthographic(-20, 5)

fig, ax = plt.subplots(figsize = (12, 6), subplot_kw={"projection": map_proj})

ax.gridlines()
ax.coastlines()
ds_anom.sel(time='2018-01-01').plot(ax=ax, vmin=-1.5, vmax=1.5,
                                   cmap='coolwarm', transform = ccrs.PlateCarree(),
                                   cbar_kwargs={'shrink':0.5, 'label': 'anomaly'})