from . import BaseProvider


class Airport:
    def __init__(self, code, name, location):
        self.code = code
        self.name = name
        self.location = location

    def __str__(self):
        return "{0} ({1})".format(self.name, self.code)


class Provider(BaseProvider):

    airports = [{'name': 'San Francisco International Airport', 'code': 'SFO', 'location': 'San Francisco, CA'},
                {'name': 'Seattle Tacoma International Airport', 'code': 'SEA', 'location': 'Seattle, WA'},
                {'name': 'McCarran International Airport', 'code': 'LAS', 'location': 'Las Vegas, NV'}]

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

        I think this model would be useful for other faker providers.
        For example  faker.family() could return a list of people objects each
        of which has a name, a gender, a role (Father, Mother, Son, Aunt), etc.
        It remains to be seen if this is stretching the faker interface too far.
        """
        return Airport(**cls.randomElement(cls.airports))

    @classmethod
    def airportCode(cls):
        """
        :example 'SFO'
        """
        return cls.airportObject().code

    @classmethod
    def airportName(cls):
        """
        :example 'McCarran International Airport'
        """
        return cls.airportObject().name

    @classmethod
    def airportLocation(cls):
        """
        :example 'Las Vegas, NV'
        """
        return cls.airportObject().location
