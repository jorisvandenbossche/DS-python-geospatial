# Create the histogram plots
fig, (ax0, ax1) = plt.subplots(1, 2, sharey=True)
ax0.hist(b4_data.flatten(), bins=30, log=True);
ax1.hist(b4_data_f.flatten(), bins=30, log=True);