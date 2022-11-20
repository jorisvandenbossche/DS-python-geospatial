fig, ax = plt.subplots(figsize=(12, 12))
ax = gdf_gent.to_crs(3857).plot(column="no2", ax=ax, scheme="NaturalBreaks", k=6, legend=True)
ax.set(xlim=(408_000, 420_000), ylim=(6_625_000, 6_638_000))
contextily.add_basemap(ax, source=contextily.providers.Stamen.TonerLite)
ax.set_axis_off()