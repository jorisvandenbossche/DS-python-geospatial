# Make a plot
fig, ax = plt.subplots(figsize=(12, 5))
ax.imshow(herstappe_rescaled.transpose(1, 2, 0), extent=herstappe_extent);