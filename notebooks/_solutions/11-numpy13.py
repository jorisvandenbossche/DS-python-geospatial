# Make a Grey scale plot
greyscale_data = herstappe_data.sum(axis=0)
fig, ax = plt.subplots(figsize=(12, 5))
plt.imshow(greyscale_data, extent=herstappe_extent, cmap="Greys");