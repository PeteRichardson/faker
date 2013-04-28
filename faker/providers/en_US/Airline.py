
import csv
import os
from ..Airline import Provider as AirlineProvider


class Provider(AirlineProvider):
    def __init__(self, generator):
        """ Load the airplines list from airlines.dat """
        self.__class__.airlines[:] = []    # clear the list
        fieldnames = ["id", "name", "alias", "iata", "icao", "callsign", "country", "active"]
        dir = os.path.dirname(__file__)
        with open(os.path.join(dir, 'airlines.dat')) as airlineData:
            self.__class__.airlines = [row for row in csv.DictReader(airlineData, delimiter=",", fieldnames=fieldnames)]
