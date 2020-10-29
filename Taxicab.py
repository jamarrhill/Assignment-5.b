# Name: Jamar Hill
# Date: 10/28/20
# Description: Assignment 5.b

class Taxicab():
    def __init__(self,x,y):
        """I have set two parameters to initialize coordinates"""
        self.x_coordinate = x
        self.y_coordinate = y
        """Odometer is set to zero"""
        self.odometer = 0

    """(get_) estabilishes current coordinate and odometer positions"""
    def get_x_coord(self):
        return self.x_coordinate

    def get_y_coord(self):
        return self.y_coordinate

    def get_odometer(self):
        return self.odometer
    """ (move_) established how the cab will moved to new coordinates"""
    def move_x(self, distance):
        self.x_coordinate += distance
        self.odometer += abs(distance)

    def move_y(self, distance):
        self.y_coordinate += distance
        self.odometer += abs(distance)

cab = Taxicab(5,-8)
cab.move_x(3)
cab.move_y(-4)
cab.move_x(-1)
print(cab.get_odometer())