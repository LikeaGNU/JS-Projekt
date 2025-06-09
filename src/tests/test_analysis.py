#!/usr/bin/python3

from memory_profiler import profile
import timeit
import sys
import random
import numpy as np
sys.path.insert(0, '..')

import utils.analysis as asys


def quick_sort_perf_test():
    start = timeit.default_timer()
    for _ in range(10):
        data = [{ 'pomiar': 0, 'wartosc': -20.0 },{ 'pomiar': 1, 'wartosc': -10.0 },
                { 'pomiar': 2, 'wartosc': -81.0 },{ 'pomiar': 3, 'wartosc': 24.0 },
                { 'pomiar': 4, 'wartosc': 2.0 },{ 'pomiar': 5, 'wartosc': 0.0 }]
        asys.quick_sort(data, 0, len(data)-1)
    stop = timeit.default_timer()
    print(asys.quick_sort.__name__ + ': Czas wykonania: ', stop - start)

@profile
def get_arthm_average_perf_test():
    start = timeit.default_timer()
    for _ in range(10):
        asys.get_arithmetic_average([ 10, 20, 30, 40, 50, 60, 70, 80, 90 ])
    stop = timeit.default_timer()
    print(asys.get_arithmetic_average.__name__ + ': Czas wykonania: ', stop - start)

@profile
def get_std_deviation_perf_test():
    start = timeit.default_timer()
    for _ in range(10):
        asys.get_standard_deviation([ 10, 20, 30, 40, 50, 60, 70, 80, 90 ])
    stop = timeit.default_timer()
    print(asys.get_standard_deviation.__name__ + ': Czas wykonania: ', stop - start)

def test_get_arithmetic_average():
    random_data = []

    def gen_random_data():
        nonlocal random_data

        for i in range(10):
            random_data.append(random.randint(-100, 100))

    gen_random_data()
    tmp_data = random_data.copy()

    avg1 = asys.get_arithmetic_average(random_data)
    avg2 = np.average(np.array(tmp_data))

    assert avg1 == avg2

def test_quick_sort():
    data = []

    def gen_random_data():
        nonlocal data

        for i in range(10):
            data.append( { 'pomiar': i, 'wartosc': random.randint(-100, 100) } )

    gen_random_data()

    tmp = data.copy()

    asys.quick_sort(data, 0, len(data)-1)

    tmp_sorted = sorted(tmp, key=lambda x: x['wartosc'])

    assert all(x == y for x, y in zip(data, tmp_sorted)) == True

@profile
def test_get_celsius():
    assert asys.get_celsius(1.0) == 33.8

@profile
def test_get_fahrenheit():
    assert int(asys.get_fahrenheit(1.0)) == -17


def main():
    quick_sort_perf_test()
    get_arthm_average_perf_test()
    get_std_deviation_perf_test()

if __name__ == '__main__':
    main()
