"""Unit test for geo module"""

from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation

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
    
    


     