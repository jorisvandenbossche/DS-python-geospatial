# Convert to float and make 65535 equal to Nan
gent_f = gent.astype(float)
gent_f = gent_f.where(gent != 65535)