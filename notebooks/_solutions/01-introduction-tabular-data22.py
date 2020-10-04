fig, ax = plt.subplots()
stations["bike_stands"].hist(ax=ax, alpha=.5, label="Total bike stands")
stations["available_bikes"].hist(ax=ax, alpha=.5, label="Available bikes")
ax.legend()