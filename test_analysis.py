from floodsystem.analysis import polyfit
from numpy import poly1d, arange
from math import isclose

def test_polyfit():
    poly = poly1d([1, 2, 3, 4])
    x = arange(1010, 999, -1)
    
    y = poly(x - 1000)

    p, offset = polyfit(x, y, 3)

    assert offset == 1000
    assert isclose(p[0], 4) and isclose(p[3], 1) 