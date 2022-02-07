"""Unit test for geo module"""

from floodsystem.geo import *
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from random import randint

def test_stations_by_distance():
    """Tests stations_by_distance function"""
    test_station = [MonitoringStation(0, 0, 0, (15,15), 0, 0, 0)]
    test_distance = stations_by_distance(test_station,(0,0))
    assert test_distance[0][0] == 0
    assert round(test_distance[0][1] ,2) == 2345.17 
    
    stations = build_station_list()
    stations_distances = stations_by_distance(stations,(0,0))
    assert len(stations) == len(stations_distances)
    
    distances = [station_distance[1] for station_distance in stations_distances]
    assert distances == sorted(distances)

def test_stations_within_radius():
    """Tests test_stations_within_radius function"""
    stations = build_station_list()
    null_station = stations_within_radius(stations,(0,0),0)
    assert len(null_station) == 0
    
    within_5 = stations_within_radius(stations,(52.2053, 0.1218),5)
    assert within_5 == sorted(within_5)

    stations_distances = stations_by_distance(stations,(0,0))
    for within_station in within_5:
        for station in stations:
            if station.name == within_station:
                distance = stations_by_distance([station],(52.2053, 0.1218))[0][1]
                assert distance < 5
                break


def test_rivers_with_stations():
    """Tests rivers_with_stations function"""
    test_rivers = [f'river_{x}' for x in range(10)]
    # make sure rivers will be in same order as out
    test_rivers = sorted(test_rivers)
    test_stations = [MonitoringStation(0, 0, 0, (15,15), 0, test_rivers[randint(0, 9)], 0) for n in range(100)]
    
    out_rivers = rivers_with_station(test_stations)
    out_rivers = sorted(out_rivers)
    assert out_rivers == test_rivers


def test_stations_by_river():
    """Tests stations_by_river function"""
    test_rivers = [f'river_{x}' for x in range(10)]
    test_stations = [MonitoringStation(0, 0, 0, (15,15), 0, test_rivers[n], 0) for n in range(10)]
    out = stations_by_river(test_stations)
    i = list(out.items())
    for n in range(10):
        assert i[n][0] == test_rivers[n]
        print(str(i[n][1]))
        print(str(test_stations[n]))
        assert str(i[n][1]) == str([test_stations[n]])

def test_rivers_by_station_number():
    """Tests rivers_by_station_number function"""
    test_rivers = [f'river_{x}' for x in range(10)]
    test_stations = [MonitoringStation(0, 0, 0, (15,15), 0, test_rivers[n % len(test_rivers)], 0) for n in range(14)]
    out_1 = rivers_by_station_number(test_stations, 4)  
    print(out_1)
    
    assert len(out_1) == 4 
    assert out_1[0] == ("river_0", 2)

    assert len(rivers_by_station_number(test_stations, 5)) == 10      