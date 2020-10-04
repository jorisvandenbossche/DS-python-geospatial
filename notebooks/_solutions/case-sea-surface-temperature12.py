# alternative using transpose instead of defining the x and y in the plot function
ds_mm.mean(dim='lon').transpose().plot.imshow(vmin=-2, vmax=30, cmap="coolwarm")