# Convert to float
gent_f = gent.astype(float)
gent_f = gent_f.where(gent_f != 65535)