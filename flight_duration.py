import csv
import textwrap
from datetime import datetime


class Airport:
    """ Airport as represented in airports.dat """
    # CSV columns will become Airport property names in __init__
    prop_names = (
        'id', 'name', 'city', 'country', 'iata', 'icao', 'lat', 'long', 'alt', 'utc_offset', 'dst_rule', 'type', 'tz',
        'source')

    def __init__(self, csv_entry):
        assert len(csv_entry) == len(Airport.prop_names)
        self.__dict__.update(dict(zip(Airport.prop_names, csv_entry)))

    def __str__(self):
        return "{0.iata} ({0.name})".format(self)


def load_airports(csv_file_name):
    """ Load airports into a dictionary where keys are IATA codes"""
    airports = {}
    with open(csv_file_name, newline='') as data_file:
        for entry in csv.reader(data_file):
            a = Airport(csv_entry=entry)
            airports[a.iata] = a
    return airports


class Flight:
    def __init__(self, flight_id, origin, destination, departure, arrival):
        self.id = flight_id
        self.origin = origin
        self.destination = destination

        self.departure = departure
        self.arrival = arrival

    def __str__(self):
        return textwrap.dedent('''\
        Flight {0.id}:
            from        : {0.origin}
            to          : {0.destination}
            departure   : {0.departure}
            arrival     : {0.arrival}
        '''.format(self))


airports = load_airports('airports.dat')

flights = [
    Flight(flight_id='AA123',
           origin=airports['ATL'],
           destination=airports['SVO'],
           departure=datetime(2018, 1, 1, 10, 10, 0),
           arrival=datetime(2018, 1, 2, 7, 12, 0))
]

for f in flights:
    print(f)