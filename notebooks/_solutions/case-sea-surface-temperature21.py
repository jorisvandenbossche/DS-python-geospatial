# Merge the data with the `basin_s` data on the index:
basin_mean_df_merged = pd.merge(basin_mean_df, basin_s, left_index=True, right_index=True)