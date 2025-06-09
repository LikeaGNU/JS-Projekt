import functools
import math
import random
import numpy as np
from functools import reduce
from memory_profiler import profile
import timeit

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

def get_fahrenheit(celsius):
    assert isinstance(celsius, float), 'Typ podanej wartości się nie zgadza!'
    return celsius * -17.222222

def main():
  pass

if __name__ == '__main__':
    main()
