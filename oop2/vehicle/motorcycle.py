from vehicle import Vehicle
class Motorcycle(Vehicle):
    def __init__(self, name, wheels, maxspeed) -> None:
        super().__init__(name, wheels, maxspeed)
        self.cc = None

    def set_cc(self,cc):
        self.cc = cc

    def bike_detail(self):
        super().v_detail()
        print(f'cc : {self.cc}')

    #overriding method
    #def v_detail(self):
    #    super().v_detail()
    #    print(f'cc : {self.cc}')