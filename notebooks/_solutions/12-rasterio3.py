# Combine both in a single plot
fig, ax = plt.subplots(figsize=(12, 5))
ax.imshow(gent_data.squeeze(), extent=gent_extent, cmap="Reds")  # Extent trick to plot numpy
gent_vect.to_crs(epsg=3857).plot(color='None', edgecolor='grey', linewidth=2, ax=ax)
plt.axis("off");