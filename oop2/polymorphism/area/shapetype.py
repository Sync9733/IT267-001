from shape import Shape
from math import pi

class Square(Shape):
    def __init__(self, length = 0) -> None:
        super().__init__('Square')
        self.__length = length

    @property
    def length(self):
        return self.__length
    @length.setter
    def length(self,value):
        self.__length = value
    
    #overiding
    def computer_area(self):
        super().computer_area()
        self.area = self.length ** 2
        #area มาจาก superclass Shape

    #newmethod
    def print_sqaure(self):
        self.computer_area()
        print(f'{self.shape} area = {self.area:,.2f}')
        #shape มาจาก superclass Shape
class Circle(Shape):
    def __init__(self, radius = 0) -> None:
        super().__init__('Circle')
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self,value):
        self.__radius = value
    
    #overiding
    def computer_area(self):
        super().computer_area()
        self.area = pi * (self.radius ** 2)
        #area มาจาก superclass Shape

    #newmethod
    def print_circle(self):
        self.computer_area()
        print(f'{self.shape} area = {self.area:,.2f}')
        #shape มาจาก superclass Shape

class Triangle(Shape):
    def __init__(self,base = 0 ,height =0) -> None:
        super().__init__('Square')
        self.__base = base
        self.__height = height

    @property
    def base(self):
        return self.__base
    @base.setter
    def base(self,value):
        self.__base = value
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self,value):
        self.__height = value
    #overiding
    def computer_area(self):
        super().computer_area()
        self.area = 0.5*self.base*self.height
        #area มาจาก superclass Shape

    #newmethod
    def print_triangle(self):
        self.computer_area()
        print(f'{self.shape} area = {self.area:,.2f}')
        #shape มาจาก superclass Shape

