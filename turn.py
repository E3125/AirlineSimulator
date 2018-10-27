class Airline:
    def __init__(self, name, l_planes, l_airports, l_routes):
        self.name = name
        self.planes = l_planes
        self.airports = l_airports
        self.routes = l_routes

class AirplaneType:
    def __init__(self, num_seats, miles_per_gallon, miles_range, cruising_altitude, speed):
        self.num_seats = num_seats
        self.mpg = miles_per_gallon
        self.range = miles_range
        self.altitude = cruising_altitude
        self.speed = speed

class Airplane:
    def __init__(self, type, l_classes):
        pass



