#!/usr/bin/python3

from consolemenu import *
from consolemenu.items import *

import matplotlib.pyplot as plt
import argparse
import numpy as np
import os

import utils.data_generator as datagen
import utils.analysis as asys
import utils.models as models

record = models.Record(list())
def_path = os.getcwd()
def_gen_filename = 'dane.csv'

def generate_datafile(filepath):
    data = datagen.file_data_generator(30, (20,30), (30,90), (0,20))
    datagen.data_writer(filepath, data)

def datafile_generation_screen():
    global def_path

    datafile_screen = Screen()
    datafile_screen.clear()

    datafile_screen.println('Generowanie pliku z danymi\n\n')

    data_dir = datafile_screen.input('Podaj katalog pliku CSV: ')

    if not os.path.exists(data_dir):
        print(f'Ścieżka {data_dir} nie istnieje.')
        print(f'Wybieram domyślną ścieżkę {def_path}')

        data_dir = def_path

    filename = ''
    try:
        filename = input('Podaj nazwę pliku CSV: ')

        if not filename:
            filename = def_gen_filename
    except OSError as e:
        print(f'Nie można utworzyć pliku {filename}!')
        print(e)
    else:
        generate_datafile(data_dir + '/' + filename)


def datafile_import_screen():
    global record 

    datafile_screen = Screen()
    datafile_screen.clear()

    datafile_screen.println('Importowanie pliku z danymi\n\n')

    station_name = datafile_screen.input('Podaj nazwę stacji: ')
    datafile_screen.println(f'Nazwa stacji: {station_name}')

    station_city = datafile_screen.input('Podaj nazwę miasta: ')
    datafile_screen.println(f'Nazwa miasta: {station_city}')

    station_quantity = datafile_screen.input('Podaj nazwę wielkości, którą mierzy stacja: ')
    datafile_screen.println(f'Mierzona wielkość: {station_quantity}')

    filepath = datafile_screen.input('Podaj ścieżkę plik CSV: ')
    file_content = datagen.data_reader(filepath)

    datafile_screen.println(f'Nazwa stacji: {station_name}')
    datafile_screen.println(f'Nazwa miasta: {station_city}')
    datafile_screen.println(f'Mierzona wielkość: {station_quantity}')
    datafile_screen.println(f'Ścieżka do pliku: {filepath}')

    record.set_data(file_content)
    record.set_station_name(station_name)
    record.set_station_city(station_city)
    record.set_station_quantity(station_quantity)


def save_graph_screen():
    global record

    csv_station_name = record.get_station_name()
    csv_city_name = record.get_city_name()
    csv_data = record.get_data()

    save_screen = Screen()
    save_screen.clear()
    save_screen.println('Nazwij plik wykresu')

    xp = [ x['pomiar'] for x in csv_data ]
    yp = [ y['temperatura'] for y in csv_data ]
    wp = [ w['wilgotnosc'] for w in csv_data ]
    pwp = [ pw['predkosc_wiatru'] for pw in csv_data ]

    filepath = save_screen.input('Wprowadź ścieżkę pliku obrazu z wykresem: ')

    figure, axis = plt.subplots(2, 2)

    axis[0, 0].set_title("Temperatura")
    axis[0, 0].set_yticks(list(filter(lambda a: a % 3 == 0, [x for x in range(len(csv_data['temperatura']))])))
    axis[0, 0].plot(csv_data['pomiar'], csv_data['temperatura'])

    axis[0, 1].plot(xp, wp)
    axis[0, 1].set_title("Wilgotność")

    axis[1, 0].plot(xp, pwp)
    axis[1, 0].set_title("Prędkość wiatru")

    plt.title(f'{csv_station_name} | {csv_city_name}')
    plt.savefig(filepath)

    save_screen.input(f'Zapisano plik obrazu w {filepath}')

def plot_sorted_graph_screen():
    global record

    tmp_data = record.get_data()

    asys.quick_sort(tmp_data, 0, len(tmp_data)-1)

    plot_screen = Screen()
    plot_screen.clear()
    plot_screen.println('Wykreśl graf w oparciu o posortowane zaimportowane dane\n\n')

    xp = [ x['pomiar'] for x in tmp_data ]
    yp = [ y['temperatura'] for y in tmp_data ]
    wp = [ w['wilgotnosc'] for w in tmp_data ]
    pwp = [ pw['predkosc_wiatru'] for pw in tmp_data ]

    plot_screen.input('Naciśnij dowolny klawisz, by wykreślić wykres... ')

    plt.plot(xp, yp)
    plt.plot(xp, wp)
    plt.plot(xp, pwp)
    plt.grid(True)
    plt.tight_layout()
    plt.title(f'{csv_station_name} | {csv_city_name}')
    plt.show()
    plt.close()

def data_view_screen():
    global record

    tmp_data = record.get_data()

    view_screen = Screen()
    view_screen.clear()
    view_screen.println('Pokaż importowany plik\n\n')

    menu = ConsoleMenu('Co chcesz zmodyfikować? ', screen=view_screen)


    def print_list():
        nonlocal view_screen

        for i in tmp_data:
            view_screen.println(i)
    def list_it():
        nonlocal view_screen

        print_list()
        view_screen.input()

    def modify_list():
        nonlocal view_screen
        nonlocal tmp_data

        print_list()

        submenu = ConsoleMenu('Podaj parametr do modyfikacji: ', screen=view_screen)

        option_a = int(view_screen.input('Podaj wiersz: '))


        def mod_humidity():
            nonlocal option_a
            nonlocal view_screen
            nonlocal tmp_data

            try:
                hum = float(view_screen.input('Podaj wartość wilgotności: '))

                if hum < 0.0 or hum > 100.0:
                    raise Exception('Należy podać wartość od 0% do 100%')
            except TypeError as e:
                print(e)
            else:
                tmp_data[option_a]['wilgotnosc'] = hum
                view_screen.println(f'Zmodyfikowano wilgotność w pomiarze nr {option_a}: {hum} %')
            finally:
                view_screen.input()

        humidity = FunctionItem('Wilgotność', mod_humidity)

        submenu.append(humidity)
        submenu.show()
    
    list_items = FunctionItem('Pokaż dane', list_it)
    modify_item = FunctionItem('Zmodyfikuj dane', modify_list)

    menu.append_item(list_items)
    menu.append_item(modify_item)

    menu.show()

def data_plot_screen():
    global record

    csv_station_name = record.get_station_name()
    csv_city_name = record.get_station_city()
    csv_data = record.get_data()

    plot_screen = Screen()
    plot_screen.clear()
    plot_screen.println('Wykreśl graf w oparciu o zaimportowane dane\n\n')

    xp = [ x['pomiar'] for x in csv_data ]
    yp = [ y['temperatura'] for y in csv_data ]
    wp = [ w['wilgotnosc'] for w in csv_data ]
    pwp = [ pw['predkosc_wiatru'] for pw in csv_data ]

    plot_screen.input('Naciśnij dowolny klawisz, by wykreślić wykres... ')

    figure, axis = plt.subplots(2,2)

    plt.xlabel('Dzień miesiąca')

    axis[0, 0].plot(xp, yp, label='Temperatura')
    axis[0, 0].set_title("Temperatura")
    axis[0, 0].set_xlabel('aaa')

    axis[0, 1].plot(xp, wp, label='Wilgotność')
    axis[0, 1].set_title("Wilgotność")

    axis[1, 0].plot(xp, pwp, label='Prędkość wiatru')
    axis[1, 0].set_title("Prędkość wiatru")

    plt.show()
    plt.close()


def main():
    def argparser():
        parser = argparse.ArgumentParser(
                prog='METEOLIZER',
                description='Analizator danych meteorologicznych',
                epilog='Wykonany przez: Wojciech Lis, Tomasz Kundera',
                usage='%(prog)s [options]')

        args = parser.parse_args()

    def console_menu():
        menu = ConsoleMenu('Meteolizer', 'Analizator danych meteorologicznych')

        import_file = FunctionItem('Importuj plik CSV z danymi', datafile_import_screen)
        gen_file = FunctionItem('Wygeneruj plik CSV z danymi', datafile_generation_screen)
        plot_graph = FunctionItem('Wykreśl graf na podstawie danych z importowanego pliku', data_plot_screen)
        plot_sorted_graph = FunctionItem('Wykreśl graf na podstawie posortowanych danych z importowanego pliku', plot_sorted_graph_screen)
        save_graph = FunctionItem('Zapisz graf wykreślony na podstawie pliku CSV', save_graph_screen)
        view_file = FunctionItem('Pokaż zaimportowany plik', data_view_screen)

        menu.append_item(import_file)
        menu.append_item(view_file)
        menu.append_item(gen_file)
        menu.append_item(plot_graph)
        menu.append_item(plot_sorted_graph)
        menu.append_item(save_graph)

        menu.show()

    # Wykonywanie
    argparser()
    console_menu()

if __name__ == '__main__':
    main()
