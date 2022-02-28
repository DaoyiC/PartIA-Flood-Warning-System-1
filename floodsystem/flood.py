from floodsystem.datafetcher import *
from floodsystem.stationdata import update_water_levels


def stations_level_over_threshold(stations, tol, update = True):
    """returns all stations that have a relative water level above 'tol'"""
    final = []
    if update:
        update_water_levels(stations) 
    for station in stations:
        relative = station.relative_water_level()
        if relative:
            if relative > tol and station.name != "Letcombe Bassett":
                final.append((station,relative))
    
    final.sort(key = lambda x: x[1],reverse = True)
    return final

def stations_highest_rel_level(stations, N, current = True):
    """returns 'N' stations with the highest relative water level"""
    stations = stations_level_over_threshold(stations,0, update=current)
    try:
        stations = [stations[i][0] for i in range(N)]
        
    except:
        stations = [station[0] for station in stations]
        
    
    return stations