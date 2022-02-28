from numpy import poly1d
from numpy import polyfit as pf

def polyfit(dates,levels, p):
    """computes polynomial of best fit for data of degree p"""
    offset = dates[0]
    dates = dates - offset
    coefs = pf(dates, levels, p)
    poly = poly1d(coefs)
    return poly, offset