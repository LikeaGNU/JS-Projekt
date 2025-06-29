# Projekt z przedmiotu Języki Skryptowe
## Temat nr 25: Analizator danych meteorologicznych

### Wykonali
- Wojciech Lis
- Tomasz Kundera

### Zależności
- `console-menu`
- `matplotlib`
- `memory_profiler`
- `numpy`


### Krótka instrukcja użytkowania
```
usage: Meteolizer [options]

Analizator danych meteorologicznych

options:
  -h, --help         show this help message and exit
  -n N               Liczba pomiarów
  --tmin TMIN        Minimalna wartość temperatury (w stopniach Celsjusza)
  --tmax TMAX        Maksymalna wartość temperatury (w stopniach Celsjusza)
  --hmin HMIN        Minimalna wartość wilgotności (w procentach)
  --hmax HMAX        Maksymalna wartość wilgotności (w procentach)
  --wmin WMIN        Minimalna prędkość wiatru (m/s)
  --wmax WMAX        Maksymalna prędkość wiatru (m/s)
  --csvfile CSVFILE  Nazwa pliku do eksportu danych CSV
  --csvdir CSVDIR    Ścieżka pliku do eksportu danych CSV

Wykonany przez: Wojciech Lis, Tomasz Kundera

```

### Struktura projektu
```
.
├── CHANGELOG.md
├── misc
│   ├── input_data.csv
│   ├── output_graph.png
│   └── output_graph_sorted.png
├── README.md
├── setup.cfg
└── src
    ├── dane.csv
    ├── meteolizer.py
    ├── test.csv
    ├── tests
    │   ├── test_analysis.py
    │   ├── test_data_generator.py
    │   └── test_models.py
    └── utils
        ├── analysis.py
        ├── data_generator.py
        ├── __init__.py
        └── models.py
```

