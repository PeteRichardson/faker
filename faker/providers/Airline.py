from . import BaseProvider


class Provider(BaseProvider):

    formats = ['{{airline}}', ]

    airlines = ['Qantas', 'Aeroflot', ]

    def airline(self):
        """
        :example 'Nevada Jets'
        """
        format = self.randomElement(self.formats)
        return self.generator.parse(format)
