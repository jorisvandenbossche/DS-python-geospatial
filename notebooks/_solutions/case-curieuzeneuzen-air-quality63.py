def closest_road_type(point, streets):
    """Type to the nearest road (OpenStreetMap)"""
    dist = streets.distance(point)
    idx_closest = dist.idxmin()
    return streets.loc[idx_closest, "highway"]