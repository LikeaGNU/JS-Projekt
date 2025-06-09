#!/usr/bin/python3

# Import the necessary packages
from consolemenu import *
from consolemenu.items import *
import matplotlib.pyplot as plt
import argparse
import numpy as np

import utils.data_generator as datagen
import utils.analysis as asys
import utils.models as models

record = models.Record(list())

def get_stats_from_file():
    pass

def generate_datafile(filepath):
    data = datagen.file_data_generator(31, (20, 30))
    datagen.data_writer(filepath, data)

def datafile_generation_screen():
    datafile_screen = Screen()
    datafile_screen.clear()

    datafile_screen.println('Generowanie pliku z danymi\n\n')
    filepath = datafile_screen.input('Podaj ścieżkę plik CSV: ')
    generate_datafile(filepath)

    datafile_screen.println(f'Wygenerowano plik CSV i zapisano w {filepath}')

def datafile_import_screen():
    global record 

    datafile_screen = Screen()
    datafile_screen.clear()

    datafile_screen.println('Importowanie pliku z danymi\n\n')
    filepath = datafile_screen.input('Podaj ścieżkę plik CSV: ')

    file_content = datagen.data_reader(filepath)
    #csv_data = file_content.copy()
    record.set_data(file_content)


def save_graph_screen():
    global record

    save_screen = Screen()
    save_screen.clear()
    save_screen.println('Nazwij plik wykresu')

    csv_data = record.get_data()

    xp = [ x['pomiar'] for x in csv_data ]
    yp = [ y['wartosc'] for y in csv_data ]

    filepath = save_screen.input('Wprowadź ścieżkę pliku obrazu z wykresem: ')

    plt.plot(xp, yp)
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
    yp = [ y['wartosc'] for y in tmp_data ]

    plot_screen.input('Naciśnij dowolny klawisz, by wykreślić wykres... ')

    plt.plot(xp, yp)
    plt.show()
    plt.close()

def data_plot_screen():
    global record

    csv_data = record.get_data()

    plot_screen = Screen()
    plot_screen.clear()
    plot_screen.println('Wykreśl graf w oparciu o zaimportowane dane\n\n')

    xp = [ x['pomiar'] for x in csv_data ]
    yp = [ y['wartosc'] for y in csv_data ]

    plot_screen.input('Naciśnij dowolny klawisz, by wykreślić wykres... ')

    plt.plot(xp, yp)
    plt.show()
    plt.close()

def main():
    def argparser():
        parser = argparse.ArgumentParser(
                prog='meteolizer',
                description='Analizator danych meteorologicznych',
                epilog='Wykonany przez: Wojciech Lis, Tomasz Kundera',
                usage='%(prog)s [options]')

        parser.add_argument('-f', '--file', help='Ścieżka pliku z danymi meteo w formacie CSV', type=str)
        args = parser.parse_args()

    def console_menu():
        menu = ConsoleMenu('Meteolizer', 'Analizator danych meteorologicznych')

        import_file = FunctionItem('Importuj plik CSV z danymi', datafile_import_screen)
        gen_file = FunctionItem('Wygeneruj plik CSV z danymi', datafile_generation_screen)
        stats_data = FunctionItem('Wylicz i wyświetl dane statystyczne importowanego pliku', get_stats_from_file)
        plot_graph = FunctionItem('Wykreśl graf na podstawie danych z importowanego pliku', data_plot_screen)
        plot_sorted_graph = FunctionItem('Wykreśl graf na podstawie posortowanych danych z importowanego pliku', plot_sorted_graph_screen)
        save_graph = FunctionItem('Zapisz graf wykreślony na podstawie pliku CSV', save_graph_screen)

        menu.append_item(import_file)
        menu.append_item(gen_file)
        menu.append_item(stats_data)
        menu.append_item(plot_graph)
        menu.append_item(plot_sorted_graph)
        menu.append_item(save_graph)

        menu.show()

    # Wykonywanie
    argparser()
    console_menu()

if __name__ == '__main__':
    main()
