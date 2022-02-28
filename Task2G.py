from floodsystem.stationdata import *
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
from matplotlib.dates import date2num
from datetime import timedelta

def calcRisk(station):
    backdate = timedelta(days=10)
    dates, levels = fetch_measure_levels(station.measure_id, backdate)
    poly, offset = polyfit(date2num(dates), levels, 4)
    current_rel = station.relative_water_level()
    pred = poly(date2num(dates[0]) + 1 - offset)
    pred_rel = (pred - station.typical_range[1]) / station.typical_range[1]
    risk = current_rel * pred_rel 
    return risk

RISK_THRESHOLD = 1.3

def riskFilter(t):
    return t[1] > RISK_THRESHOLD

if __name__ == "__main__":
    stations = build_station_list()
    highest = stations_highest_rel_level(stations, 25)
    risks = [(s, calcRisk(s)) for s in highest]
    at_risk = [s for s in filter(riskFilter, risks)]
    for station in at_risk:
        print(f'{station[0].name} at risk, risk level: {station[1]}')