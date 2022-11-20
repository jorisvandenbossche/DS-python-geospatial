# A Diverging colormap `RdYlGn` with a normalization on the color limits in two directions of the central point:
div_norm = mcolors.TwoSlopeNorm(vmin=-0.1, vcenter=0.4, vmax=0.8)
fig, ax = plt.subplots(figsize=(10, 4))
ll = ax.imshow(ndvi, cmap="RdYlGn", extent=b4_data_extent, norm=div_norm)
fig.colorbar(ll);
plt.axis('off');