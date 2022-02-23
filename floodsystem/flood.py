
def stations_level_over_threshold(stations, tol):
    """returns all stations that have a relative water level above 'tol'"""
    final = []
    for station in stations:
        relative = station.relative_water_level()
        if relative:
            if relative > tol and station.name != "Letcombe Bassett":
                final.append((station,relative))
    
    final.sort(key = lambda x: x[1],reverse = True)
    return final

def stations_highest_rel_level(stations, N):
    """returns 'N' stations with the highest relative water level"""
    stations = stations_level_over_threshold(stations,0)
    stations = stations[:N]
    return stations