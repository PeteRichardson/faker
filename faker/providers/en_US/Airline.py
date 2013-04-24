

from ..Airline import  Provider as AirlineProvider

class Provider(AirlineProvider):

    formats = (
        '{{realAirline}}',
        '{{lastName}} {{airlineSuffix}}',
        '{{state}} {{airlineSuffix}}'
    )

    realAirlines = (
        'ABX Air', 'Air Choice One', 'Air Flamenco', 'Air Transport International', 'Air Wisconsin', 'AirNet Express', 'AirNow', 'AirTran Airways', 'Alaska Airlines', 'Allegiant Air', 'Aloha Air Cargo', 'American Airlines', 'American Eagle Airlines', 'Ameriflight', 'Amerijet International', 'Ameristar Air Cargo', 'Arctic Circle Air', 'Asia Pacific Airlines', 'Astar Air Cargo', 'Atlas Air',
        'Bering Air',
        'Cape Air', 'Capital Cargo International Airlines', 'Centurion Air Cargo', 'Chautauqua Airlines', 'CommutAir', 'Compass Airlines',
        'Delta Air Lines', 'Delta Private Jets',
        'Empire Airlines', 'Empire Airways', 'Era Alaska', 'Evergreen International Airlines', 'Everts Air', 'Executive Airlines', 'Express.Net Airlines', 'ExpressJet Airlines',
        'FedEx Express', 'Flight Alaska', 'Freight Runners Express', 'Frontier Airlines', 'Frontier Flying Service',
        'GeorgiaSkies', 'go!', 'GoJet Airlines', 'Grant Aviation', 'Great Lakes Airlines', 'Gryphon Airlines',
        'Hageland Aviation Services', 'Hawaiian Airlines', 'Horizon Air',
        'Island Air',
        'JetBlue Airways',
        'Kalitta Air', 'Kenmore Air',
        'L-3 Flight International Aviation',
        'Mesa Airlines', 'Miami Air International', 'Mokulele Airlines',
        'Nantucket Airlines', 'National Airlines', 'NetJets', 'North American Airlines', 'Northern Air Cargo',
        'Omni Air International',
        'Pacific Wings', 'PenAir', 'Piedmont Airlines', 'Pinnacle Airlines', 'Polar Air Cargo', 'PSA Airlines',
        'Republic Airlines', 'Ryan Air Services',
        'San Juan Airlines', 'SeaCoast Airlines', 'SeaPort Airlines', 'Servant Air', 'Shuttle America', 'Silver Airways', 'Sky King', 'SkyWest Airlines', 'Southern Air', 'Southwest Airlines', 'Spirit Airlines', 'Sun Air International', 'Sun Country Airlines', 'Swift Air',
        'Taquan Air', 'Tepper Aviation', 'Tradewinds Airlines', 'Trans Executive Airlines', 'Trans States Airlines',
        'Ultimate Air Shuttle', 'United Airlines', 'UPS Airlines', 'US Airways', 'USA Jet Airlines',
        'Vieques Air Link', 'Virgin America', 'Vision Airlines',
        'Warbelow''s Air Ventures', 'Wiggins Airways', 'Wings of Alaska', 'World Airways', 'Wright Air Service',
        'Xtra Airways',
    )

    airlineSuffixes = (
        'Air', 'Aviation', 'Airlines', 'Airways', 'Aviation Service',
        'Business Jets',
        'Cargo', 'Charter', 'Commuter Jet',
        'Express', 'Eagle',
        'International',
        'Jets',
        'Transport',
        'Wings'
    )

    @classmethod
    def realAirline(cls):
        return cls.randomElement(cls.realAirlines)

    @classmethod
    def airlineSuffix(cls):
        return cls.randomElement(cls.airlineSuffixes)
