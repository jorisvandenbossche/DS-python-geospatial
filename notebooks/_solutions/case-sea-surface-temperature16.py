# make a combined plot
fig, ax = plt.subplots()
ds_anom_loc.plot.line(ax=ax, label="monthly anom")
ds_anom_resample.plot.line(marker='o', label="5 year resample")
ds_anom_rolling.plot.line(label='12 month rolling mean')
fig.legend(loc="upper center", ncol=3)
ax.set_title("");