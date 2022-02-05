from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    """Prints all "stations within 10km
    of Cambridge city centre"""
    coords = (52.2053, 0.1218)
    stations = build_station_list()
    stations = stations_within_radius(stations,coords,10)
    print(stations)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
