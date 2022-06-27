from vehicle import Vehicle
class Bus(Vehicle):
    def __init__(self, name, wheels, maxspeed) -> None:
        super().__init__(name, wheels, maxspeed)
        self.color = None
        self.capacity = None

    def set_color(self,color):
        self.color = color

    def set_capacity(self,capacity):
        self.capacity = capacity

    def bus_detail(self):
        print(f'Color : {self.color}\nCapacity : {self.capacity}')