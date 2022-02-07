from floodsystem.geo import *
from floodsystem.stationdata import build_station_list

def run():
    """prints 9 rivers with greatest number of monitoring stations"""
    stations = build_station_list()
    out = rivers_by_station_number(stations, 9)

    print(out)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()