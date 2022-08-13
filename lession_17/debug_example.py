import datetime
from this import d

# 1. Create a new Class with some properties and methods
class Vehicle:
    def __init__(self, name, max_speed=100, color='red', year=1990):
        self.name = name # public property (default)
        self._max_speed = max_speed # protected property with single underscore
        self.__color = color # private property with double underscore
        self.__year = year # private property with double underscore

    def get_name(self):
        return self.name
    
    def get_max_speed(self):
        return self._max_speed
    
    def get_color(self):
        return self.__color

    # define private methods with double underscore
    def __calculate_year_old(self):
        year_old = datetime.datetime.now().year - self.__year
        return year_old
    
    def get_year_old(self):
        return self.__calculate_year_old()
    
    def set_color(self, color):
        self.color = color

    def set_max_speed(self, max_speed):
        self.max_speed = max_speed

# 2. Create a Child class for the vehicle
class Motor(Vehicle):
    def __init__(self, name, color, max_speed, year, engine):
        self.engine = engine
        # Vehicle.__init__(self, name, max_speed, color, year)
        super().__init__(name, max_speed, color, year)
    
    # can't access private properties from parrent class
    # def get_color(self):
    #     return self.__color

def main():
    # create a new object for the Motor class
    motor_x = Motor('Air Blade', 'black', 200, 2017, 150)

    print(f'Vehicle information of X - Name: {motor_x.name}, Color: {motor_x.get_color()}, \
        Year Old: {motor_x.get_year_old()}, Engine: {motor_x.engine}, Max Speed: {motor_x._max_speed}')

    # create some objects of Vehicle class
    # veh_x = Vehicle('Toyota Fortuner')
    # veh_y = Vehicle('Huyndai Santafe', 200, 'black', 2016)

    # print(f'Vehicle information of X - Name: {veh_x.name}, Max Speed: {veh_x.get_color()}, Year Old: {veh_x.get_year_old()}')

    # print(f'Vehicle information of X - Name: {veh_x.get_name()}, Max Speed: {veh_x.get_max_speed()}')
    # print(f'Vehicle information of Y - Name: {veh_y.get_name()}, Max Speed: {veh_y.get_max_speed()}, - Year Old: {veh_y.get_year_old()}')


if __name__ == '__main__':
    main()
