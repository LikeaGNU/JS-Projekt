#! /usr/bin/python3

import csv
import random
import datetime

def row_generator(n, temp_range, humidity_range, wind_range):
    """
    Wygeneruj pojedynczy wiersz danych meteorologicznych
    """
    temperature = random.randint(temp_range[0], temp_range[1])
    humidity = generate_humidity(humidity_range[0], humidity_range[1])
    wind_speed = generate_wind_speed(wind_range[0], wind_range[1])

    row = []

    row.append(n+1)  # pomiar
    row.append(temperature)
    row.append(humidity)
    row.append(wind_speed)

    return tuple(row)

def generate_humidity(minimum, maximum):
    """
    Generuj losową wilgotność procentową
    """
    return random.randint(minimum, maximum)

def generate_wind_speed(minimum, maximum):
    """
    Generuj siłę wiatru w m/s
    """
    return random.randint(minimum, maximum)

def file_data_generator(n, temp_range, humidity_range, wind_range):
    """
    Utwórz zawartość pliku z danymi meteorologicznymi
    """
    data = []

    for i in range(n):
        data_set = row_generator(i, temp_range, humidity_range, wind_range)
        data.append(data_set)
    return data

def data_writer(filepath, data):
    """
    Utwórz plik CSV i wpisz do niego dane meteorologiczne
    """
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['pomiar', 'temperatura', 'wilgotnosc', 'predkosc_wiatru'])
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
    # Definiujemy zakresy dla temperatury, wilgotności i wiatru
    temp_range = (20, 30)
    humidity_range = (30, 90)   # wilgotność od 30% do 90%
    wind_range = (0, 20)        # siła wiatru od 0 do 20 m/s

    data = file_data_generator(10, temp_range, humidity_range, wind_range)
    data_writer('dane.csv', data)

if __name__ == '__main__':
    main()

