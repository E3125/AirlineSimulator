import classes.py

name = input("Enter airline name:")

dash8 = AirplaneModel(40, 1125.0/835, 1125, 25000, 333)
dc3 = AirplaneModel(32, 1500.0/822, 1500, 23200, 207)

coach_class = SeatClass(dc3.num_seats, "coach")

plane1 = Airplane(dc3, [coach_class])
plane2 = Airplane(dash8, [coach_class])
player_planes = [plane1, plane2]

CHO_loc = Location(38.1395, 78.4516)
CHO = Airport("charlottesville/albemarle", "CHO", 3, 40000, CHO_loc)
DCA_loc = Loacation(38.8512, 77.0402)
DCA = Airport("ronald reagan washington national airport", 12, 1000000,)
# finish airports cap later 

player_airline = Airline(name, player_planes, )

