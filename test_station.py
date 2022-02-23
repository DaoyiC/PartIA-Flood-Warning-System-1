# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_inconsistent_typical_range_stations():
    """Tests inconsistent_typical_range_stations function"""
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    test1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    assert len(inconsistent_typical_range_stations([test1])) == 0
    
    trange = (4,4)
    test2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    assert len(inconsistent_typical_range_stations([test2])) == 0

    trange = (4,3.9)
    test3 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    assert len(inconsistent_typical_range_stations([test3])) == 1

    test4 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    assert len(inconsistent_typical_range_stations([test4])) == 1

    assert len(inconsistent_typical_range_stations([test1,test2,test3,test4])) == 2

