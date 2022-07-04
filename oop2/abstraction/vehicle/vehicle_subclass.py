from vehicle_abstract import Vehicle
class Car(Vehicle):
    def __init__(self, brand, speed) -> None:
        #super().__init__(brand, speed)
        Vehicle.__init__(self,brand,speed)
        self.__year = 0
        self.__maintanance = 0
    @property #year
    def year(self):
        return self.__year
    @year.setter
    def year(self,value):
        self.__year = value
    
    @property #maintanance
    def maintanance(self):
        return self.__maintanance
    @maintanance.setter
    def maintanance(self,value):
        self.__maintanance = value
    
    #implement abstact method
    def show_detail(self):
        super().show_detail()
        print('=== Car Detail ===')
        print(f'{self.brand} with speed {self.speed} km/hr')
        print(f'manufactered in {self.year} has')
        print(f'{self.gear} gear and {self.seat} seats')

    #implement Car method
    def show_maintanance(self):
        print('-- Car Maintanance --')
        print(f'The lastest maintanace in {self.maintanance}')
        
class Truck(Vehicle):
    def __init__(self, brand, speed) -> None:
        super().__init__(brand, speed)
        self.__capacity = 0
        self.__wheel = 0
    @property
    def capacity(self):
        return self.__capacity
    @capacity.setter
    def capacity(self,value):
        self.__capacity = value
    
    @property
    def wheel(self):
        return self.__wheel
    @wheel.setter
    def wheel(self,value):
        self.__wheel = value
    def show_detail(self):
        super().show_detail()
        print('=== Truck Detail ===')
        print(f'{self.brand} with speed {self.speed} km/hr and {self.wheel} wheels can carry {self.capacity} ton')
    def show_price(self):
        print('=== Truck Price ===')
        if self.wheel == 4:
            price = 1000
        elif self.wheel == 6:
            price = 1500
        elif self.wheel ==8:
            price = 2000
        else :
            price = 3000
        print(f'{self.wheel} wheels truck is {price} baht/day.')
class Motocycle(Vehicle):
    def __init__(self, brand, speed) -> None:
        super().__init__(brand, speed)
        self.__cc = 150
        self.__model = None
    @property
    def cc(self):
        return self.__cc
    @cc.setter
    def cc(self,value):
        self.__cc = value
    
    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self,value):
        self.__model = value
    
    def show_detail(self):
        super().show_detail()
        print('=== Motorcycle Detail ===')
        print(f'{self.brand}--{self.model} with speed {self.speed} km/hr')
        print(f'cc {self.cc}')