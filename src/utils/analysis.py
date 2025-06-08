import functools
import math

def get_arithmetic_average(data):
    length = len(stations)

    dat_sum = reduce(lambda x, y: x + y, [ x for x in data ])

    try:
        res = dat_sum / length
    except ZeroDivisionError:
        print(f'Wykryto dzielenie przez zero')
    else:
        return res

def get_standard_deviation(data):
    deviation = 0
    res = 0
    length = len(data)

    avg = get_arithmetic_average(data)

    for i in range(length):
        deviation += (avg - i) ** 2

    try:
        deviation /= length
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

