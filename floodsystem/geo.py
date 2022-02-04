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