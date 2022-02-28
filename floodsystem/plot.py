from matplotlib import pyplot as plt
from matplotlib.dates import date2num
from .analysis import polyfit
import numpy as np

def plot_water_levels(station, dates, levels):
    """plots river level by date with typical range for a station"""
    low = [station.typical_range[0] for x in dates]
    high = [station.typical_range[1] for x in dates]
    name = station.name

    plt.scatter(date2num(dates), levels)
    plt.plot(dates, low, label="typical low")
    plt.plot(dates, high, label="typical high")
    plt.xlabel("date")
    plt.ylabel("river level")
    plt.title(name)
    plt.show()    

def plot_water_level_with_fit(station, dates, levels, p):
    """plots river level along with curve of best fit against date"""
    dates = date2num(dates)
    poly, offset = polyfit(dates, levels, p)
    x = np.arange(dates[-1] - offset)
    y = poly(x)
    x = x + offset

    plt.plot(x, y, label="best fit")

    low = [station.typical_range[0] for x in dates]
    high = [station.typical_range[1] for x in dates]
    name = station.name

    plt.scatter(date2num(dates), levels)
    plt.plot(dates, low, label="typical low")
    plt.plot(dates, high, label="typical high")
    plt.xlabel("date")
    plt.ylabel("river level")
    plt.title(name)
    plt.show() 