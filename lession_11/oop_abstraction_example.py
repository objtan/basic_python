from abc import ABC, abstractmethod
'''
class abstractClassName(ABC):
    [list of attributes]
    [list of method]
    @abstractmethod
    def methodName(self):
        pass
'''

class Polygon(ABC):
    @abstractmethod
    def draw(self):
        pass

    def get_area(self):
        pass

    def get_perimeter(self):
        pass


class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        print('Draw rectangle')

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_area(self):
        return self.width*self.height

    def get_perimeter(self):
        return 2*(self.width*self.height)


class Square(Polygon):
    def __init__(self,width):
        self.width = width

    def draw(self):
        print('Draw Square')

    def get_area(self):
        return self.width * 2

    def get_perimeter(self):
        return 2 * (self.width*self.width)

obj_rectangle = Rectangle(5,8)
obj_rectangle.draw()
print(f'Area of Rectangle: {obj_rectangle.get_area()}')
print(f'Perimeter of Rectangle: {obj_rectangle.get_perimeter()}')
print()

obj_square = Square(5)
obj_square.draw()
print(f'Area of Square: {obj_square.get_area()}')
print(f'Perimeter of Square: {obj_square.get_perimeter()}')
print()

