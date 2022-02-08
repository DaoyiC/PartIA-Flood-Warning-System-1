from floodsystem.geo import *
from floodsystem.stationdata import build_station_list

def run():
    """prints how many rivers have at least one monitoring station and first 10 in alphabetical order"""
    stations = build_station_list()
    rs = rivers_with_station(stations)
    print(f'{len(rs)} stations. First 10 - {sorted(rs)[0:10]}')

    sbr = stations_by_river(stations)
    print(f'River Aire stations: {sbr["River Aire"]}')

    print(f'River Cam stations: {sbr["River Cam"]}')

    print(f'River Thames stations: {sbr["River Thames"]}')

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()