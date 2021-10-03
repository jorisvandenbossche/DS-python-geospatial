argo_pressure = argo.assign_coords(pressure=argo["pressure"]).sel(date='2012-12')

fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(12, 6))
argo_pressure["salinity"].plot.line(y="pressure", yincrease=False, ax=ax0, hue='date');
argo_pressure["temperature"].plot.line(y="pressure", yincrease=False, ax=ax1, hue='date');