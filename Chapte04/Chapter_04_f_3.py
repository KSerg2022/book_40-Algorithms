import random


def greedy_algorithm(cities, start=None):
    C = start or first(cities)
    tour = [C]
    unvisited = set(cities - {C})
    while unvisited:
        C = nearest_neighbor(C, unvisited)
        tour.append(C)
        unvisited.remove(C)
    return tour


def first(collection):
    return next(iter(collection))


def nearest_neighbor(A, cities):
    return min(cities, key=lambda C: distance_points(C, A))


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
    q = frozenset(a_city(random.randint(1, width), random.randint(1, height)) \
                     for c in range(number_of_cities))
    # return frozenset(a_city(random.randint(1, width), random.randint(1, height)) \
    #                  for c in range(number_of_cities))
    return q


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
    # print("{}: {} cities - tour length {:.0f} {in {:.3f} sec}".format(
    #     name(algorithm), len(tour), distance_tour(tour), t1 - t0
    # ))
    print(f'{name(algorithm)}: {len(tour)} cities - tour length {distance_tour(tour):.0f} in {t1 - t0:.3f} sec')


def name(algorithm):
    return algorithm.__name__.replace('_tsp', '')


tsp(greedy_algorithm, generate_cities(2000))
