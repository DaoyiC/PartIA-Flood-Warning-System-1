from floodsystem.stationdata import *
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
from matplotlib.dates import date2num

def calcRisk(station):
    dates, levels = fetch_measure_levels(station.measure_id, 10)
    poly, offset = polyfit(dates, levels, 4)
    current_rel = station.relative_water_level()
    predicted = (poly(dates[-1] - offset + 1) - station.typical_range) / station.typical_range
    risk = current_rel * predicted 
    return risk

RISK_THRESHOLD = 1.3

def riskFilter(t):
    return t[1] > RISK_THRESHOLD

if __name__ == "__main__":
    stations = build_station_list()
    highest = stations_highest_rel_level(stations, 25)
    risks = [(s, calcRisk(s)) for s in highest]
    at_risk = [s for s in filter(riskFilter, risks)]
    
    msg = [f'{s[0]} at risk, risk level: {s[1]}' for s in at_risk]

    print("\r\n".join(msg))