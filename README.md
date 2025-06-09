# Projekt z przedmiotu Języki Skryptowe
## Temat nr 25: Analizator danych meteorologicznych

### Wykonali
- Wojciech Lis
- Tomasz Kundera

### Zależności
- `console-menu`
- `matplotlib`

### Krótka instrukcja użytkowania
```
usage: meteolizer [options]

Analizator danych meteorologicznych

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Ścieżka pliku z danymi meteo w formacie CSV
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
    ├── meteolizer.py
    ├── test.csv
    ├── tests
    │   └── test_analysis.py
    └── utils
        ├── analysis.py
        ├── data_generator.py
        ├── __init__.py
        └── models.py

4 directories, 13 files
```
