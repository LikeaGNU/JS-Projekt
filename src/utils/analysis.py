import functools
import math
import random
import numpy as np
from functools import reduce

def get_arithmetic_average(data):
    """
    Oblicz średnią arytmetyczną
    """

    length = len(data)

    dat_sum = reduce(lambda x, y: x + y, [ x for x in data ])

    try:
        res = dat_sum / length
    except ZeroDivisionError:
        print(f'Wykryto dzielenie przez zero')
    else:
        return res

def test_get_arithmetic_average():
    random_data = []

    def gen_random_data():
        nonlocal random_data

        for i in range(10):
            random_data.append(random.randint(-100, 100))

    gen_random_data()
    tmp_data = random_data.copy()

    avg1 = get_arithmetic_average(random_data)
    avg2 = np.average(np.array(tmp_data))

    assert avg1 == avg2


# Algorytm quicksort do sortowania wyników
def partition(array, low, high):
    pivot = array[high].get('wartosc')

    i = low - 1

    j = low
    while j < high:
        if array[j].get('wartosc') <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
        j += 1

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)

def test_quick_sort():
    data = []

    def gen_random_data():
        nonlocal data

        for i in range(10):
            data.append( { 'pomiar': i, 'wartosc': random.randint(-100, 100) } )

    gen_random_data()

    tmp = data.copy()

    quick_sort(data, 0, len(data)-1)

    tmp_sorted = sorted(tmp, key=lambda x: x['wartosc'])

    assert all(x == y for x, y in zip(data, tmp_sorted)) == True

def get_standard_deviation(data):
    """
    Oblicz odchylenie standardowe
    """

    deviation = 0
    res = 0
    length = len(data)

    avg = get_arithmetic_average(data)

    for i in range(length):
        deviation += ((i - avg) ** 2)

    try:
        deviation /= length-1
        res = math.sqrt(deviation)
    except ZeroDivisionError:
        print(f'Wykryto dzielenie przez zero')
    except:
        print(f'Wykryto wyjątek!')
    finally:
        return res

def get_celsius(fahrenheit):
    assert isinstance(fahrenheit, float), 'Typ podanej wartości się nie zgadza!'
    return fahrenheit * 33.8

def test_get_celsius():
    assert get_celsius(1.0) == 33.8

def get_fahrenheit(celsius):
    assert isinstance(celsius, float), 'Typ podanej wartości się nie zgadza!'
    return celsius * -17.222222

def test_get_fahrenheit():
    assert int(get_fahrenheit(1.0)) == -17

def main():
    data = [
            { 'pomiar': 0, 'wartosc': -20.0 },
            { 'pomiar': 1, 'wartosc': -10.0 },
            { 'pomiar': 2, 'wartosc': -81.0 },
            { 'pomiar': 3, 'wartosc': 24.0 },
            { 'pomiar': 4, 'wartosc': 2.0 },
            { 'pomiar': 5, 'wartosc': 0.0 }
            ]

    print(data)
    quick_sort(data, 0, len(data)-1)
    print(data)

if __name__ == '__main__':
    main()
