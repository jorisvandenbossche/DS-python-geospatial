fig, ax = plt.subplots()
# using predefined bins
df['no2'].hist(ax=ax, bins=np.arange(0, 80, 5))
# adding x/y axis labels, and setting the range for the x axis
ax.set(xlabel="NO2 concentration (µg/m³)",
       ylabel="Number of measurements", xlim=(0,80))
# adding a line with the mean
ax.axvline(x=df['no2'].mean(), color='C2', linewidth=3)
# adding a line with the EU yearly limit value of 40 µg/m³
ax.axvline(x=40, color='C3', linewidth=3)