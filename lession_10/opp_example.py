from datetime import datetime
from turtle import st


class Vehicle:
    def __init__(self, name, max_speed = 100, color = 'red', year = 1990):
        self.name = name
        self._max_speed = max_speed
        self.__color = color
        self.__year = year

    def get_name(self):
        return self.name

    def get_max_speed(self):
        return self._max_speed
    
    def get_color(self):
        return self.__color

    def max_speed(self):
        return self.max_speed

    # define private methods with double underscore
    def __calculate_year_old(self):
        year_old = datetime.now().year - self.__year
        return year_old
    
    def get_year_old(self):
        return self.__calculate_year_old()
    
    def set_color(self, color):
        self.color = color

    def set_max_speed(self, max_speed):
        self.max_speed = max_speed

veh_x = Vehicle('Toyota')
veh_y = Vehicle('Honda')

# create some objects of Vehicle class
veh_x = Vehicle('Toyota Fortuner')
veh_y = Vehicle('Huyndai Santafe', 200, 'black', 2016)

print(f'Vehicle information of X - Name: {veh_x.name}, Max Speed: {veh_x.get_color()}, Year Old: {veh_x.get_year_old()}')

print(f'Vehicle information of X - Name: {veh_x.get_name()}, Max Speed: {veh_x.get_max_speed()}')
print(f'Vehicle information of Y - Name: {veh_y.get_name()}, Max Speed: {veh_y.get_max_speed()}, - Year Old: {veh_y.get_year_old()}')

# 2. Create a Child class for the vehicle
class Motor(Vehicle):
    def __init__(self, name, color, max_speed, year, engine):
        self.engine = engine
        # Vehicle.__init__(self, name, max_speed, color, year)
        super().__init__(name, max_speed, color, year)
    
    # can't access private properties from parrent class
    # def get_color(self):
    #     return self.__color


# create a new object for the Motor class
motor_x = Motor('Air Blade', 'black', 200, 2017, 150)

print(f'Vehicle information of X - Name: {motor_x.name}, Color: {motor_x._max_speed()}, \
    Year Old: {motor_x.get_year_old()}, Engine: {motor_x.engine}, Max Speed: {motor_x._max_speed}')