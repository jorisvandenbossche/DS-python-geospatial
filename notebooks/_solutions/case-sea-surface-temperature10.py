ds_mm = sst.groupby(sst.time.dt.month).mean(dim='time')