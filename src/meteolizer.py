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

    plt.plot(xp, yp)
    plt.plot(xp, wp)
    plt.plot(xp, pwp)
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
    plt.title(f'{csv_station_name} | {csv_city_name}')
    plt.show()
    plt.close()


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

    plt.title(f'{csv_station_name} | {csv_city_name}')
    plt.plot(xp, yp, label='temperatura')
    plt.plot(wp, label='wilgotnosc')
    plt.plot(pwp, label='predkosc wiatru')

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

        menu.append_item(import_file)
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
