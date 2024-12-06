urban_green_fraction = urban_green_area / districts_area * 100
# some district are missing from urban_green_area (no urban green in that district)
# this gives NaNs in the result, which we fill with 0
urban_green_fraction = urban_green_fraction.fillna(0)