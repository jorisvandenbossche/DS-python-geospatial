# Overlay both datasets based on the intersection
combined = geopandas.overlay(land_use, districts, how='intersection', keep_geom_type=True)