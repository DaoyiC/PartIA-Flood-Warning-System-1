from matplotlib import pyplot as plt
from matplotlib.dates import date2num, num2date
from .analysis import polyfit
import numpy as np

def plot_water_levels(station, dates, levels):
    """plots river level by date with typical range for a station"""
    low = [station.typical_range[0] for x in dates]
    high = [station.typical_range[1] for x in dates]
    name = station.name

    ymin = 0
    if low[0] < ymin:
        ymin = 2 * low[0]

    plt.scatter(date2num(dates), levels, marker=".")
    plt.plot(dates, low, label="typical low")
    plt.plot(dates, high, label="typical high")
    plt.ylim(ymin, high[0] * 5)
    plt.xlabel("date")
    plt.ylabel("river level")
    plt.title(name)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend()
    plt.show()    

def plot_water_level_with_fit(station, dates, levels, p):
    """plots river level along with curve of best fit against date"""
    poly, offset = polyfit(date2num(dates), levels, p)
    x = np.arange(date2num(dates[0]) - offset, step=0.01)
    y = poly(x)
    x = x + offset

    plt.plot(x, y, label="best fit", linestyle="dashed")

    low = [station.typical_range[0] for x in dates]
    high = [station.typical_range[1] for x in dates]
    name = station.name

    ymin = 0
    if low[0] < ymin:
        ymin = 2 * low[0]
    for v in y:
        if v < ymin and v > -100:
            ymin = v * 1.25

    plt.scatter(date2num(dates), levels, marker=".")
    plt.plot(dates, low, label="typical low")
    plt.plot(dates, high, label="typical high")
    plt.ylim(ymin, high[0] * 5)
    plt.xlabel("date")
    plt.ylabel("river level")
    plt.title(name)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend()
    plt.show() 