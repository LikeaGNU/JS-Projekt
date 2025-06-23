#! /usr/bin/python3

import csv
import random
import datetime

def row_generator(n, minimum, maximum):
    """
    Wygeneruj pojedynczy wiersz danych meteorologicznych
    """

    # row = ( day, temp/hum)
    # row = ( x, y )

    value = random.randint(minimum, maximum)
    row = []

    row.append(n+1)
    row.append(value)

    return tuple(row)

def file_data_generator(n, values):
    """
    Utwórz zawartość pliku z danymi meteorologicznymi
    """

    data = []

    for i in range(n):
        data_set = row_generator(i, values[0], values[1])
        data.append(data_set)
    return data

def data_writer(filepath, data):
    """
    Utwórz plik CSV i wpisz do niego dane meteorologiczne
    """

    with open(filepath, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['pomiar','wartosc'])
        writer.writerows(data)

def data_reader(filepath):
    """
    Odczytaj plik CSV i zwróć jego zawartość w liście
    """

    file_content = []

    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)

        for line in reader:
            file_content.append(line)

    return file_content


def main():
    data = file_data_generator(10, (20, 30))
    data_writer('dane.csv', data)

if __name__ == '__main__':
    main()
