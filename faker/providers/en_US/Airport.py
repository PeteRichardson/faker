from ..Airport import Provider as AirportProvider
from json import load
import os


class Provider(AirportProvider):
    def __init__(self, generator):
        """ Load the airports list with some airports with English names """
        dir = os.path.dirname(__file__)
        with open(os.path.join(dir, 'airports.json')) as airportData:
            self.__class__.airports = load(airportData, object_hook=self.ascii_encode_dict)

    def ascii_encode_dict(self, data):
        '''http://stackoverflow.com/questions/9590382/forcing-python-json-module-to-work-with-ascii'''
        ascii_encode = lambda x: x.encode('ascii', 'ignore')
        return dict(map(ascii_encode, pair) for pair in data.items())
