from . import BaseProvider


class Provider(BaseProvider):

    formats = ['{{realAirline}}', ]

    realAirlines = ['Qantas', 'Aeroflot', ]

    def airline(self):
        """
        :example 'Nevada Jets'
        """
        format = self.randomElement(self.formats)
        return self.generator.parse(format)

    @classmethod
    def realAirline(cls):
        """
        :example 'United Airlines'
        """
        return cls.randomElement(cls.realAirlines)
