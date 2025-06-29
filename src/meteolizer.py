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

def main():
    def argparser():
        parser = argparse.ArgumentParser(
                prog='Meteolizer',
                description='Analizator danych meteorologicznych',
                epilog='Wykonany przez: Wojciech Lis, Tomasz Kundera',
                usage='%(prog)s [options]')

        parser.add_argument('-n', type=int, help='Liczba pomiarów', default=30)
        parser.add_argument('--tmin', type=int, help='Minimalna wartość temperatury (w stopniach Celsjusza)', default=-40)
        parser.add_argument('--tmax', type=int, help='Maksymalna wartość temperatury (w stopniach Celsjusza)', default=50)
        parser.add_argument('--hmin', type=int, help='Minimalna wartość wilgotności (w procentach)', default=0)
        parser.add_argument('--hmax', type=int, help='Maksymalna wartość wilgotności (w procentach)', default=100)
        parser.add_argument('--wmin', type=int, help='Minimalna prędkość wiatru (m/s)', default=30)
        parser.add_argument('--wmax', type=int, help='Maksymalna prędkość wiatru (m/s)', default=300)
        parser.add_argument('--csvfile', type=str, help='Nazwa pliku do eksportu danych CSV', default='dane.csv')
        parser.add_argument('--csvdir', type=str, help='Ścieżka pliku do eksportu danych CSV', default=os.path.dirname(__file__))
        args = parser.parse_args()

        return args

    def console_menu(scr, args):
        def print_params(scr, args):
            scr.println('Parametry programu:')
            scr.println(f'Ilość pomiarów: {args.n}')
            scr.println(f'Minimalna temperatura: {args.tmin}')
            scr.println(f'Maksymalna temperatura: {args.tmax}')
            scr.println(f'Minimalna wilgotność: {args.hmin}')
            scr.println(f'Maksymalna wilgotność: {args.hmax}')
            scr.println(f'Maksymalna prędkość wiatru: {args.wmin}')
            scr.println(f'Maksymalna prędkość wiatru: {args.wmax}')
            scr.println(f'Domyślna ścieżka katalogu eksportu: {args.csvdir}')
            scr.println(f'Domyślna nazwa pliku eksportu: {args.csvfile}')
        def show_params_scr(scr, args):
            print_params(scr, args)
            scr.input('Kliknij Enter, aby wyjść')
        def import_data_scr(scr, args):
            global record

            try:
                data = datagen.data_reader(args.csvfile)

            except FileNotFoundError:
                scr.println(f'Nie znaleziono pliku {args.csvfile} w katalogu {args.csvdir}!')
                scr.input()
            except (TypeError, OSError, ValueError):
                scr.println(f'Błąd odczytu pliku {args.csvfile} w katalogu {args.csvdir}!')
            else:
                record.set_data(data)

                scr.println(f'Udało się zaimportować dane z pliku {args.csvfile}!')
                scr.input()
        def gen_data_scr(scr, args):
            data = datagen.file_data_generator(args.n,
                                               (args.tmin, args.tmax),
                                               (args.hmin, args.hmax),
                                               (args.wmin, args.wmax))

            try:
                datagen.data_writer(args.csvdir + '/' + args.csvfile, data) 
            except OSError:
                scr.println(f'Wystąpił problem z zapisaniem danych do pliku {args.csvfile}')
            except:
                scr.println(f'Wystąpił wyjątek')
            else:
                scr.println(f'Udało się zapisać dane do pliku {args.csvfile} w katalogu {args.csvdir}!')
                scr.input()

        def draw_graph_scr(scr, args):
            global record

            try:
                data = record.get_data()

                if not data:
                    scr.println('Nie zaimportowano danych!')
                    scr.input()
                    
                    raise ValueError('Nie zaimportowano danych!')
            except ValueError as e:
                print(e)
            else:
                num = [ nm['pomiar'] for nm in data ]
                temp = [ tp['temperatura'] for tp in data ]
                hum = [ hm['wilgotnosc'] for hm in data ]
                wind = [ wn['predkosc_wiatru'] for wn in data ]

                plt.plot(num, temp, color='r', label='Temperatura [°C]')
                plt.plot(num, hum, color='g', label='Wilgotność [%]')
                plt.plot(num, wind, color='b', label='Prędkość wiatru [m/s]')
                plt.legend()
                plt.xlabel('Numer pomiaru')
                plt.ylabel('Wielkości')
                plt.title('Wykres danych meteorologicznych')
    
                plt.show()

        def modify_data_scr(scr, args):
            global record

            def insert_num(scr, args):
                global record

                data = record.get_data()

                vmax = len(data)

                try:
                    user_value = int(scr.input('Podaj numer pomiaru, który chcesz zmodyfikować (od 1 do {vmax+1}): '))

                    if user_value-1 < 0 or user_value-1 > vmax:
                        scr.println('Niepoprawny numer pomiaru')
                        raise ValueError(f'Niepoprawny number pomiaru! {user_value}')
                except TypeError:
                    print(e)
                else:
                    return user_value
            def insert_param(scr, args):
                global record
                chosen_key = ''

                try:
                    data = record.get_data()
                    
                    if not data:
                        raise ValueError('Brak danych!')
                except:
                    scr.println('Wystąpił wyjątek!')
                else:
                    scr.println('Możliwe klucze:')

                    i = 1
                    
                    available_keys = {}

                    for key in data[0].keys():
                        available_keys[str(i)] = key
                        scr.println(f'{i}. {key}')
                        i += 1

                    try:
                        user_value = int(input('Podaj numer klucza: '))
                        
                        if user_value not in range(1, i):
                            scr.println(f'Podano niepoprawny numer klucza! {user_value}')
                            raise ValueError(f'Podano niepoprawny numer klucza! {user_value}')
                    except (TypeError, ValueError) as e:
                        scr.println(f'Wykryto wyjątek: {e}')
                    else:
                        chosen_key = available_keys[str(user_value)]
                        scr.println(f'Wybrano klucz {user_value} - {chosen_key}')
                        input()
                        return chosen_key

            data = record.get_data()

            try:
                #idx = 1
                idx = insert_num(scr, args)
                key = insert_param(scr, args)
            except (ValueError, TypeError) as e:
                scr.println(f'Wystąpił wyjątek! {e}')
            else:
                old_value = data[idx][key]

                old_val_type = type(old_value)

                try:
                    scr.println(f'Wybrana wartość: {old_value}, Typ: {old_val_type.__name__}')
                    new_value = old_val_type(scr.input('Podaj nową wartość: '))

                    if key == 'pomiar' or key == 'predkosc_wiatru':
                        if new_value < 0:
                            raise ValueError(f'Niepoprawna wartość: {new_value})')
                            scr.input()
                    if key == 'wilgotnosc':
                        if new_value < 0 or new_value > 100:
                            scr.println(f'Niepoprawna wartość: {new_value})')
                            scr.input()
                            raise ValueError(f'Niepoprawna wartość: {new_value})')
                    
                except (TypeError, ValueError) as e:
                    scr.println(f'Wykryto wyjątek: {e}')
                    scr.input() 
                else:
                    data[idx][key] = new_value
                    scr.println('Nadpisano dane!')
                    scr.input()


        def modify_params_scr(scr, args):
            def modify_n(scr, args):
                try:
                    new_n = int(scr.input('Podaj nową wartość liczby pomiarów: '))

                    if new_n <= 0:
                        raise ValueError(f'Zbyt mała liczba pomiarów: {new_n}')
                except (TypeError, ValueError) as e:
                    print(e)
                else:
                    args.n = new_n
                    scr.println(f'Nadpisano wartość liczby pomiarów: {args.n}')
                    scr.input('Kliknij Enter, aby wyjść')

            def modify_tmin(scr, args):
                try:
                    new_tmin = int(scr.input('Podaj nową wartość najmniejszej temperatury (w stopniach Celsjusza): '))

                except (TypeError, ValueError) as e:
                    print(e)
                else:
                    args.tmin = new_tmin
                    scr.println(f'Nadpisano wartość liczby najmniejszej temperatury: {args.tmin}')
                    scr.input('Kliknij Enter, aby wyjść')
            def modify_tmax(scr, args):
                try:
                    new_tmax = int(scr.input('Podaj nową wartość największej temperatury (w stopniach Celsjusza): '))

                except (TypeError, ValueError) as e:
                    print(e)
                else:
                    args.tmax = new_tmax
                    scr.println(f'Nadpisano wartość liczby największej temperatury: {args.tmax}')
                    scr.input('Kliknij Enter, aby wyjść')
            def modify_hmin(scr, args):
                try:
                    new_hmin = int(scr.input('Podaj nową wartość najmniejszej wilgotności (w procentach): '))

                    if new_hmin < 0 and new_hmin > 100:
                        raise ValueError('Niepoprawa wartość wilgotności: {new_hmin}%')

                except (TypeError, ValueError) as e:
                    print(e)
                else:
                    args.hmin = new_hmin
                    scr.println(f'Nadpisano wartość najmniejszej wilgotności: {args.hmin}%')
                    scr.input('Kliknij Enter, aby wyjść')
            def modify_hmax(scr, args):
                try:
                    new_hmax = int(scr.input('Podaj nową wartość największej wilgotności (w procentach): '))

                    if new_hmax < 0 and new_hmax > 100:
                        raise ValueError('Niepoprawa wartość wilgotności: {new_hmax}%')

                except (TypeError, ValueError) as e:
                    print(e)
                else:
                    args.hmax = new_hmax
                    scr.println(f'Nadpisano wartość największej wilgotności: {args.hmax}%')
                    scr.input('Kliknij Enter, aby wyjść')
            def modify_wmin(scr, args):
                try:
                    new_wmin = int(scr.input('Podaj nową najmniejszą prędkość wiatru (w m/s): '))

                    if new_wmin < 0:
                        scr.println('Niepoprawna prędkość wiatru {new_wmin} m/s')
                        scr.input()
                        raise ValueError('Niepoprawa prędkość wiatru: {new_wmin} m/s')

                except (TypeError, ValueError) as e:
                    print(e)
                else:
                    args.wmin = new_wmin
                    scr.println(f'Nadpisano najmniejszą prędkość wiatru: {args.wmin} m/s')
                    scr.input('Kliknij Enter, aby wyjść')
            def modify_wmax(scr, args):
                try:
                    new_wmax = int(scr.input('Podaj nową największą prędkość wiatru (w m/s): '))

                    if new_wmax < 0:
                        raise ValueError('Niepoprawa prędkość wiatru: {new_wmax} m/s')

                except (TypeError, ValueError) as e:
                    print(e)
                else:
                    args.wmax = new_wmax
                    scr.println(f'Nadpisano największą prędkość wiatru: {args.wmax} m/s')
                    scr.input('Kliknij Enter, aby wyjść')
            def modify_csvdir(scr, args):
                try:
                    new_csvdir = scr.input(f"Podaj nazwę nowej ścieżki do katalogu eksportu (bez {os.getenv('HOME')}): ")

                    full_csvdir = os.getenv('HOME') + '/' + new_csvdir

                    if not os.path.exists(full_csvdir):
                        raise ValueError(f'Podana ścieżka do pliku nie istnieje: {full_csvdir}')
                except (OSError) as e:
                    print(e)
                else:
                    args.csvdir = full_csvdir
                    scr.println(f'Nadpisano domyślną ścieżkę do katalogu eksportu: {args.csvdir}')
                    scr.input('Kliknij Enter, aby wyjść')
            def modify_csvfile(scr, args):
                try:
                    new_csvfile = scr.input(f'Podaj nową nazwę pliku eksportu: ')

                except (OSError) as e:
                    print(e)
                else:
                    args.csvfile = new_csvfile
                    scr.println(f'Nadpisano nazwę pliku eksportu: {args.csvfile}')
                    scr.input('Kliknij Enter, aby wyjść')

            params_submenu = ConsoleMenu('Zmień ustawienia parametrów')

            params_n = FunctionItem('Zmień liczbę pomiarów', modify_n, [scr, args])
            params_tmin = FunctionItem('Zmień najmniejszą wartość temperatury', modify_tmin, [scr, args])
            params_tmax = FunctionItem('Zmień największą wartość temperatury', modify_tmax, [scr, args])
            params_hmin = FunctionItem('Zmień najmniejszą wartość wilgotności', modify_hmin, [scr, args])
            params_hmax = FunctionItem('Zmień największą wartość wilgotności', modify_hmax, [scr, args])
            params_wmin = FunctionItem('Zmień najmniejszą prędkość wiatru', modify_wmin, [scr, args])
            params_wmax = FunctionItem('Zmień największą prędkość wiatru', modify_wmax, [scr, args])
            params_csvfile = FunctionItem('Zmień domyślną nazwę pliku eksportu', modify_csvfile, [scr, args])
            params_csvdir = FunctionItem('Zmień domyślną ścieżkę katalogu eksportu', modify_csvdir, [scr, args])

            params_submenu.append_item(params_n)
            params_submenu.append_item(params_tmin)
            params_submenu.append_item(params_tmax)
            params_submenu.append_item(params_hmin)
            params_submenu.append_item(params_hmax)
            params_submenu.append_item(params_wmin)
            params_submenu.append_item(params_wmax)
            params_submenu.append_item(params_csvfile)
            params_submenu.append_item(params_csvdir)

            params_submenu.show()


        menu = ConsoleMenu('Meteolizer', 'Analizator danych meteorologicznych', screen=scr)

        show_params = FunctionItem("Pokaż parametry programu", show_params_scr, [scr, args])
        mod_params = FunctionItem('Nadpisz parametry programu', modify_params_scr, [scr, args])
        draw_graph = FunctionItem('Narysuj graf na podstawie zaimportowanych danych', draw_graph_scr, [scr, args])
        import_data = FunctionItem('Zaimportuj dane CSV z pliku', import_data_scr, [scr, args])
        gen_data = FunctionItem('Wygeneruj dane do pliku CSV', gen_data_scr, [scr, args])
        modify_data = FunctionItem('Nadpisz dane zaimportowane z pliku CSV', modify_data_scr, [scr, args])

        menu.append_item(show_params)
        menu.append_item(mod_params)
        menu.append_item(draw_graph)
        menu.append_item(import_data)
        menu.append_item(gen_data)
        menu.append_item(modify_data)

        menu.show()

    
    scr = Screen()
    args = argparser()
    console_menu(scr, args)


if __name__ == '__main__':
    main()
