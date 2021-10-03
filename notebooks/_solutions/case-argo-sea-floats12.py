salinity_20121031 = argo["salinity"].sel(date='2012-10-31')

fig, ax = plt.subplots(figsize=(6, 6))
salinity_20121031.plot.line(y="level", yincrease=False, color="grey");
salinity_20121031.rolling(level=10, center=True).median().plot.line(y="level", yincrease=False, linewidth=3, color="orange");