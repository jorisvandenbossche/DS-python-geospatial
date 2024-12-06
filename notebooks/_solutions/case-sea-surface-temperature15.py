# compute the resampling and rolling
ds_anom_resample = ds_anom_loc.resample(time='5YE').median(dim='time')
ds_anom_rolling = ds_anom_loc.rolling(time=12, center=True).median()