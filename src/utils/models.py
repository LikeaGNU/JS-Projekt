import unittest

class Record:
    def __init__(self, stat_id, date, temp, hum):
        self.station_id = stat_id
        self.date = date
        self.temperature = temp
        self.humidity = hum

    def __repr__(self):
        return (\
            f"""
Rekord:
    ID stacji: ${self.station_id},
    Data: ${self.date},
    Temperatura: ${self.temperature},
    Wilgotność: ${self.humidity}
            """)

class Station:
    def __init__(self, stat_id, name, lat, lon):
        self.station_id = stat_id
        self.name = name
        self.latitude = lat
        self.longitude = lon

    def __repr__(self):
        return (\
                f"""
Stacja:
    ID: ${self.station_id},
    Nazwa: ${self.name},
    Szer. geograficzna: ${self.longitude}
    Wys. geograficzna: ${self.latitude}
                """)

class TestRecord(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()

