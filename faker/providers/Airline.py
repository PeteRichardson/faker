from . import BaseProvider

class Airline:
    """Airline object definition derived from data available at
       http://www.openflights.org/data

       id is the openflights.org id for the airline.
       \N in a field means no value.
       iata is the 2 char abbreviation (e.g.  United Airlines = UL)
       icao is the 3 char abbreviation (e.g.  United Airlines = UAL)
       active is a boolean indicating the airline is still running. This field
                  is not particularly trustworthy.
       """
    def __init__(self, id, name, alias, iata, icao, callsign, country, active):
        self.id = id
        self.name = name
        #self.alias = '' if alias == "\\N" else alias
        if alias == "\\N":
            self.alias = ""
        else:
            self.alias = alias
        self.iata = iata
        self.icao = icao
        self.callsign = callsign
        self.country = country
        self.active = active == "Y"

    def __str__(self):
        return "{0} ({1})".format(self.name, self.icao)


class Provider(BaseProvider):

    airlines = [{"id": 2935, "name": "Island Air Charters", "alias": "\N", "iata": "", "icao": "ILF", "callsign": "ISLAND FLIGHT", "country": "United States", "active": "N"},
                {"id": 8568, "name": "Trans Maldivian Airways", "alias": "", "iata": "M8", "icao": "TMW", "callsign": "", "country": "Maldives", "active": "N"},
                {"id": 17618, "name": "AirOne Polska", "alias": "AirOne Polska", "iata": "U1", "icao": "001", "callsign": "AOC", "country": "Poland", "active": "N"}, ]

    @classmethod
    def airline(cls):
        """
        returns a string constructed from the airline name and icao abbreviation
        :example 'Worldwide Jet Charter (WWI)'
        """
        return str(cls.airlineObject())

    @classmethod
    def airlineObject(cls):
        return Airline(**cls.randomElement(cls.airlines))
