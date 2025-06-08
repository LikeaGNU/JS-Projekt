#!/usr/bin/python3

# Import the necessary packages
from consolemenu import *
from consolemenu.items import *
import matplotlib.pyplot as plt
import argparse
import numpy as np

def get_stats_from_file():
    pass


def get_graph_from_file():
    xp = np.array( [ 0, 6 ] )
    yp = np.array( [ 0, 250 ] )

    plt.plot(xp, yp)
    plt.show()


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

        import_file = FunctionItem('Importuj plik CSV z danymi', input, [ 'Podaj ścieżkę pliku z danymi >  ' ])
        gen_file = FunctionItem('Wygeneruj plik CSV z danymi', input, [ 'aaaa' ] )
        stats_data = FunctionItem('Wylicz i wyświetl dane statystyczne importowanego pliku', get_stats_from_file)
        plot_graph = FunctionItem('Wykreśl graf na podstawie danych z importowanego pliku', get_graph_from_file)

        menu.append_item(import_file)
        menu.append_item(gen_file)
        menu.append_item(stats_data)
        menu.append_item(plot_graph)

        menu.show()

    # Wykonywanie
    argparser()
    console_menu()

if __name__ == '__main__':
    main()
