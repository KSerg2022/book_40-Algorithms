import random
from itertools import permutations


all_tours = permutations


def distance_tour(a_tour):
    return sum(distance_points(a_tour[i - 1], a_tour[i]) for i in range(len(a_tour)))


a_city = complex


def distance_points(first, second):
    return abs(first - second)


def generate_cities(number_of_cities):
    seed = 111
    width = 500
    height = 300
    random.seed((number_of_cities, seed))
    return frozenset(a_city(random.randint(1, width), random.randint(1, height)) \
                     for c in range(number_of_cities))


def brute_force(cities):
    return shortest_tour(all_tours(cities))


def shortest_tour(tours):
    return min(tours, key=distance_tour)

# %matplotlib inline
import matplotlib.pyplot as plt


def visualize_tour(tour, style='bo-'):
    if len(tour) > 1000:
        plt.figure(figsize=(15, 10))
    start = tour[0:1]
    visualize_segment(tour + start, style)
    visualize_segment(start, 'rD')


def visualize_segment(segment, style='bo-'):
    plt.plot([X(c) for c in segment], [Y(c) for c in segment], style, clip_on=False)
    plt.axis('scaled')
    plt.axis('off')

    plt.show()


def X(city):
    "X axis"
    return city.real


def Y(city):
    "Y axis"
    return city.imag


from time import time
from collections import Counter

def tsp(algorithm, cities):
    t0 = time()
    tour = algorithm(cities)
    t1 = time()
    assert Counter(tour) == Counter(cities)
    visualize_tour(tour)
    print("{}: {} cities - tour length {:.0f} (in {:.3f} sec)".format(
        name(algorithm), len(tour), distance_tour(tour), t1 - t0
    ))


def name(algorithm):
    return algorithm.__name__.replace('_tsp', '')


tsp(brute_force, generate_cities(10))





towns = [
    {'ottawa': {'monreal': 199, 'kingstown': 196, 'toronto': 450, 'sadbery': 484}},
    {'monreal': {'ottawa': 199, 'kingstown': 287, 'toronto': 542, 'sadbery': 680}},
    {'kingstown': {'ottawa': 196, 'monreal': 287, 'toronto': 263, 'sadbery': 634}},
    {'toronto': {'ottawa': 450, 'monreal': 542, 'kingstown': 263, 'sadbery': 400}},
    {'sadbery': {'ottawa': 484, 'monreal': 680, 'kingstown': 634, 'toronto': 400}},
]

start = 'ottawa'
route = [start]
way = 0
# for town in towns:
#     if list(town.keys())[0] == start:
