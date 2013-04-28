from . import BaseProvider


class Airport:
    """Airport object definition derived from data available at
       http://www.openflights.org/data

        Airport ID  Unique OpenFlights identifier for this airport.
        Name        Name of airport. May or may not contain the City name.
        City        Main city served by airport. May be spelled differently from Name.
        Country     Country or territory where airport is located.
        IATA/FAA    3-letter FAA code, for airports located in Country "United States of America".
                    3-letter IATA code, for all other airports.
                    Blank if not assigned.
        ICAO        4-letter ICAO code.
                    Blank if not assigned.
        Latitude    Decimal degrees, usually to six significant digits. Negative is South, positive is North.
        Longitude   Decimal degrees, usually to six significant digits. Negative is West, positive is East.
        Altitude    In feet.
        Timezone    Hours offset from UTC. Fractional hours are expressed as decimals, eg. India is 5.5.
        DST         Daylight savings time. One of E (Europe), A (US/Canada), S (South America), O (Australia), Z (New Zealand), N (None) or U (Unknown).
       """
    def __init__(self, id, name, city, country, iata, icao, latitude, longitude, altitude, timezone, DST):
        self.id = int(id)
        self.name = name
        self.city = city
        self.country = country
        self.iata = iata
        self.icao = '' if icao == "\\N" else icao
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.altitude = int(altitude)
        self.timezone = timezone
        self.DST = DST

    def __str__(self):
        if not self.icao:
            return self.name
        else:
            return "{0} ({1})".format(self.name, self.icao)


class Provider(BaseProvider):
    airports = [{"id": "3", "name": "Mount Hagen", "city": "Mount Hagen", "country": "Papua New Guinea", "iata": "HGU", "icao": "AYMH", "latitude": "-5.826789", "longitude": "144.295861", "altitude": "5388", "timezone": "10", "DST": "U"}, ]

    @classmethod
    def airport(cls):
        """
        :example 'McCarran International Airport (LAS)'
        """
        return str(cls.airportObject())

    @classmethod
    def airportObject(cls):
        """
        returns a rich Airport object constructed from the airport data in the
        list above. Most faker functions return a string, but I didn't want to
        lose all the rich airport info (e.g. code, location) or encode it in a
        string then have to parse it out again.
        """
        return Airport(**cls.randomElement(cls.airports))

    @classmethod
    def airportCode(cls):
        """
        :example 'SFO'
        """
        return cls.airportObject().iata

    @classmethod
    def airportName(cls):
        """
        :example 'McCarran International Airport'
        """
        return cls.airportObject().name

    @classmethod
    def airportLocation(cls):
        """
        :example 'San Francisco, United States'
        """
        airport = cls.airportObject()
        return "{0}, {1}".format(airport.city, airport.country)
