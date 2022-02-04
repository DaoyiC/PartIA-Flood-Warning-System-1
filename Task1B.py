from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    """Prints the furthest and closest 10 stations
    to Cambridge city centre (52.2053, 0.1218)"""
    coords = (52.2053, 0.1218)
    stations = build_station_list()
    distances = stations_by_distance(stations,coords)
    output = []
    for distance in distances:
        name = distance[0]
        town = ''
        for station in stations:
            if station.name == name:
                town = station.town
        output.append((name,town,distance[1]))
    print('cloest')
    print(output[:10])
    print('furthest')
    print(output[-10:])
