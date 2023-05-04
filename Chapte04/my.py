towns = {
    'ottawa': {'monreal': 199, 'kingstown': 196, 'toronto': 450, 'sadbery': 484},
    'monreal': {'ottawa': 199, 'kingstown': 287, 'toronto': 542, 'sadbery': 680},
    'kingstown': {'ottawa': 196, 'monreal': 287, 'toronto': 263, 'sadbery': 634},
    'toronto': {'ottawa': 450, 'monreal': 542, 'kingstown': 263, 'sadbery': 400},
    'sadbery': {'ottawa': 484, 'monreal': 680, 'kingstown': 634, 'toronto': 400},
}
towns2 = {
    'ottawa': {'monreal': 19, 'kingstown': 160, 'toronto': 50, 'sadbery': 48},
    'monreal': {'ottawa': 99, 'kingstown': 87, 'toronto': 52, 'sadbery': 68},
    'kingstown': {'ottawa': 196, 'monreal': 287, 'toronto': 23, 'sadbery': 64},
    'toronto': {'ottawa': 40, 'monreal': 54, 'kingstown': 26, 'sadbery': 40},
    'sadbery': {'ottawa': 4, 'monreal': 60, 'kingstown': 63, 'toronto': 40},
}


def get_route(towns_=None,
              start_town_=None,
              route_=None):
    for town, path in towns_.items():
        if town == start_town_:
            next_cities = dict(sorted(path.items(), key=lambda x: x[1]))
            for city_, _ in next_cities.items():
                if city_ in route_:
                    continue
                else:
                    route_.append(city_)
                    get_route(towns, city_, route_)

            return route


def get_length(route, towns_):
    length = 0
    for idx in range(len(route) - 1):
        length += towns_[route[idx]][route[idx + 1]]
    return length

start_town = 'ottawa'
route = [start_town]

route = get_route(towns, start_town, route)
route.append(route[0])
length_way = get_length(route, towns)
print(route)
print(length_way)


print('~' * 50)
start_town = 'ottawa'
route = [start_town]

route = get_route(towns2, start_town, route)
route.append(route[0])
length_way = get_length(route, towns2)
print(route)
print(length_way)