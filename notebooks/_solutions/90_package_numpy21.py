# Create an image plot
fig, ax = plt.subplots(figsize=(10, 4))
img = ax.imshow(b4_data_classified, extent=b4_data_extent)
fig.colorbar(img, values=[10, 20, 30], ticks=[10, 20, 30])
ax.set_aspect("equal")