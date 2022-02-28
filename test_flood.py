"""Unit test for module flood"""

from floodsystem.geo import *
from floodsystem.stationdata import *
from floodsystem.station import *
from random import randint
from floodsystem.flood import *

def test_level_over_threshold():
    """Tests stations_level_over_threshold function"""
    test_station = [MonitoringStation(0, 0, 0, 0, [0,100], 0, 0)]
    stations = stations_level_over_threshold(test_station, 0.5)
    #Checks that if no latest level then nothing is returned
    assert len(stations) == 0
    test_station[0].latest_level = 50
    stations = stations_level_over_threshold(test_station, 0.5)
    #Checks that if on boundary nothing is returned
    assert len(stations) == 0
    test_station[0].latest_level = 51
    stations = stations_level_over_threshold(test_station, 0.5, update = False)
    #Checks that if just over  boundary something is returned
    assert len(stations) == 1

def test_highest_rel_level():
    stations = build_station_list()
    top = stations_highest_rel_level(stations, 3, current = False)
    #Checks that if all stations don't have latest level nothing is returned
    assert len(top) == 0
    top = stations_highest_rel_level(stations, 3)
    all = stations_level_over_threshold(stations,0)
    #Checks actually 3 stations returned
    assert len(top) == 3 
    for i in range(3):
        #checks 3 returned are actually the highest
        assert top[i] == all[i][0]