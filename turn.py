class Airline:
    def __init__(self, name, l_planes, l_airports, l_routes):
        self.name = name
        self.planes = l_planes
        self.airports = l_airports
        self.routes = l_routes

class AirplaneModel:
    def __init__(self, num_seats, miles_per_gallon, miles_range, cruising_altitude, speed):
        self.num_seats = num_seats
        self.mpg = miles_per_gallon
        self.range = miles_range
        self.altitude = cruising_altitude
        self.speed = speed

class Airplane:
    def __init__(self, model: AirplaneModel, l_classes):
        self.model: AirplaneModel = model
        self.l_classes = l_classes
    
class SeatClass:
    def __init__(self, num_seats, name, cost = 100):
        self.cost = cost
        self.total_seats = num_seats
        self.name = name

    def set_price(self, new_price):
        self.cost = new_price

class Airport:
    def __init__(self, name, code, num_gates, num_citizens, lat, long):
        self.name = name
        self.code = code
        self.num_gates = num_gates
        self.citizens = num_citizens
        self.lat = lat
        self.long = longatude

class Citizen:
    pass


