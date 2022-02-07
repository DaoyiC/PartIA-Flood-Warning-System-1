# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine

def stations_by_distance(stations, p):
    """Given list of stations and a coordinate , returns list of stations
    with distance from coordinate sorted ascending by distance"""
    output = []
    for station in stations:
        coord = station.coord
        distance = haversine (coord, p)
        output.append((station.name,distance))
    output = sorted_by_key(output,1)
    return output

def stations_within_radius(stations, centre, r):
    """Returns all stations within radius of specified coordinate"""
    distances = stations_by_distance(stations,centre)
    output = []
    for distance in distances:
        if distance[1] < r:
            output.append(distance[0])
    output.sort()
    return output

def rivers_with_station(stations):
    """Returns list of all rivers with monitoring stations"""
    rivers = []
    for s in stations:
        if s.river and not s.river in rivers:
            rivers.append(s.river)

    return rivers

def stations_by_river(stations):
    """Returns dict of {river: [stations]}"""
    rivers = rivers_with_station(stations)
    d = {}
    for r in rivers:
        d[r] = [s for s in stations if s.river == r]
    return d

def rivers_by_station_number(stations, N):
    s = stations_by_river(stations)
    l = []
    items = list(s.items())

    def sortTuple(elem):
        return elem[1]

    ls = sorted([(t[0], len(t[1])) for t in items], key=sortTuple, reverse=True)
    l = ls[0:N]

    while l[len(l) - 1][1] == ls[N][1]:
        l.append(ls[N])
        N += 1
        if N >= len(ls):
            break

    return l

