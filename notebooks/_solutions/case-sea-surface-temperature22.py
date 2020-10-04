# Create a bar chart of the SST per basin data:
basin_mean_df_merged.sort_values(by="sst").plot.barh(x="basin");