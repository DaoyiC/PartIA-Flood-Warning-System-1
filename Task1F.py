from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    """Prints all stations which have inconsistent data
    (i.e no data or low is higher than high)"""
    stations = build_station_list()
    print(inconsistent_typical_range_stations(stations))

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
