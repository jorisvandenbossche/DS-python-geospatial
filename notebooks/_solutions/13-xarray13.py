fig, (ax0, ax1) = plt.subplots(1, 2)
subset_mean["salinity"].plot.line(y="level", yincrease=False, ax=ax0)
subset_mean["temperature"].plot.line(y="level", yincrease=False, ax=ax1)
plt.tight_layout()