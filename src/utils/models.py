#!/usr/bin/python3


# Tablica z właściwymi danymi
# Nazwa pomiaru
# Miesiąc
# Rok
# Nazwy wielkości
class Record:
    '''Pomiar'''
    class Station:
        '''Stacja badawcza'''
        # name: nazwa stacji
        # city: nazwa miasta
        # quantity: mierzona wielkość fizyczna (temperatura)
        def __init__(self):
            pass
        def set_name(self, new_name):
            self.name = new_name
        def set_city(self, new_city):
            self.city = new_city
        def set_quantity(self, new_quantity):
            self.quantity = new_quantity
        def get_name(self):
            return self.name
        def get_city(self):
            return self.city
        def get_quantity(self):
            return self.quantity
    def __init__(self, data):
        self.data = data.copy()
        self.station = self.Station()
    def set_station_name(self, new_name):
        self.station.set_name(new_name)
    def set_station_city(self, new_city):
        self.station.set_city(new_city)
    def set_station_quantity(self, new_quantity):
        self.station.set_quantity(new_quantity)
    def get_station_name(self):
        return self.station.get_name() if hasattr(self.station, 'name') else None
    def get_station_city(self):
        return self.station.get_city() if hasattr(self.station, 'city') else None
    def get_station_quantity(self):
        return self.station.get_quantity() if hasattr(self.station, 'quantity') else None
    def set_data(self, new_data):
        self.data = new_data.copy()
    def get_data(self):
        return self.data.copy()

def main():
    data = [ 10, 20, 30 ]

    record = Record(data)

    record.set_station_name('Stacja 1')
    record.set_station_city('Kielce')
    record.set_station_quantity('Temperatura')

    print(record.get_station_name())

if __name__ == '__main__':
    main()

