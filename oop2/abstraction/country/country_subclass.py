from country import Country
class Europe(Country):
    def __init__(self, name, population) -> None:
        super().__init__(name, population)
        self.__location = None
        self.__capital = None
    
    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self,value):
        self.__location = value
    @property
    def capital(self):
        return self.__capital
    @capital.setter
    def capital(self,value):
        self.__capital = value
    
    def show_detail(self):
        print(f'==== Europe ====')
        print(f'Country: {self.name}\nCapital: {self.capital}\npopulation: {self.population:,}\nlocation: {self.location}')

class Asian(Country):
    def __init__(self, name, population) -> None:
        super().__init__(name, population)
        self.__gdp = 0
    
    @property
    def gdp(self):
        return self.__gdp
    @gdp.setter
    def gdp(self,value):
        self.__gdp = value
    
    def show_detail(self):
        print(f'==== Asia ====')
        print(f'Country: {self.name}\nPopulation {self.population:,}\ngdp: {self.gdp:,} billion USD')