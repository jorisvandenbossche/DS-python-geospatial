# A Sequential colormap `YlGn` with a normalization on the color limits
import matplotlib.colors as mcolors
div_norm = mcolors.Normalize(0.1, 0.8)
fig, ax = plt.subplots(figsize=(14, 5))
ll = ax.imshow(ndvi, cmap="YlGn", extent=b4_extent, norm=div_norm)
fig.colorbar(ll);