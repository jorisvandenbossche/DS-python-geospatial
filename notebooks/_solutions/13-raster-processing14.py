img = dem_gent.plot.imshow(
    cmap="terrain", figsize=(10, 10), interpolation='antialiased', vmin=0, vmax=30)
img.axes.set_aspect("equal")