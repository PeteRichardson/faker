from ..Airport import Provider as AirportProvider
import os
import csv


class Provider(AirportProvider):
    def __init__(self, generator):
        """ Load the airplines list from airlines.dat """
        self.__class__.airports[:] = []    # clear the list
        fieldnames = ["id", "name", "city", "country", "iata", "icao", "latitude", "longitude", "altitude", "timezone", "DST"]
        dir = os.path.dirname(__file__)
        with open(os.path.join(dir, 'airports.dat')) as airportData:
            self.__class__.airports = [row for row in csv.DictReader(airportData, delimiter=",", fieldnames=fieldnames)]

