from turtle import back
from floodsystem.stationdata import *
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from datetime import timedelta

if __name__ == "__main__":
    stations = build_station_list()
    highest = stations_highest_rel_level(stations, 5)
    backdate = timedelta(days=10)
    for station in highest:
        dates, levels = fetch_measure_levels(station.measure_id, backdate)
        plot_water_levels(station, dates, levels)
