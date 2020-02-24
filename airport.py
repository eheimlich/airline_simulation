class Airport:

    def __init__ (self, name, code, slots, lat, long):
        self.name = name
        self.code = code
        self.slots = slots
        self.lat = lat
        self.long = long

    def distance(self, airport_1, airport_2):
        """
        Return the distance between two airports given the longitude and latitude of both airports.
        :param airport_1: Airport
        :param airport_2: Airport
        :return: float
        """
        
