muni_mean = gdf_combined.groupby("NAAM")["no2"].mean()
muni_mean.head()