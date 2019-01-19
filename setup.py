from classes import *

name = input("Enter airline name:")

dash8 = AirplaneModel(40, 1125.0/835, 1125, 25000, 333)
dc3 = AirplaneModel(32, 1500.0/822, 1500, 23200, 207)

coach_class = SeatClass(dc3.num_seats, "coach")

plane1 = Airplane(dc3, [coach_class])
plane2 = Airplane(dash8, [coach_class])
player_planes = [plane1, plane2]

CHO_loc = Location(38.1395, 78.4516)
CHO = Airport("charlottesville/albemarle", "CHO", 3, 40000, CHO_loc)
DCA_loc = Location(38.8512, 77.0402)
DCA = Airport("ronald reagan washington national airport", "DCA", 12, 1000000, DCA_loc)

DCA_CHO1 = Route(DCA, CHO, 1.00, 1.75)
DCA_CHO2 = Route(DCA, CHO, 3.00, 3.75)
DCA_CHO3 = Route(DCA, CHO, 5.00, 5.75)
DCA_CHO4 = Route(DCA, CHO, 7.00, 7.75)

CHO_DCA1 = Route(CHO, DCA, 2.00, 2.75)
CHO_DCA2 = Route(CHO, DCA, 4.00, 4.75)
CHO_DCA3 = Route(CHO, DCA, 6.00, 6.75)
CHO_DCA4 = Route(CHO, DCA, 8.00, 8.75)

player_routes = [DCA_CHO1, DCA_CHO2, DCA_CHO3, DCA_CHO4, CHO_DCA1, CHO_DCA2, CHO_DCA3, CHO_DCA4]
player_airline = Airline(name, player_planes, [CHO, DCA], player_routes)
