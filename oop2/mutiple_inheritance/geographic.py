class Geographic:
    def set_cordinate(self,lat:float,long:float):
        self.lattitude = lat
        self.longtitude = long
    
    def get_cordinate(self):
        return f'lattitude : {self.lattitude}, longtitude {self.longtitude}'

    def get_timeZone(self):
        timezone = round((self.longtitude/12)-1)
        if timezone > 0:
            return f'+{timezone}'
        else:
            return f'{timezone}'

    def get_climate(self):
        if self.lattitude <= 66.5 or self.lattitude >= 66.5:
            return f'Polar Zone'
        elif self.lattitude <= -23.5 or self.lattitude >= 23.5:
            return f'Temerate Zone'
        else:
            return f'Tropical Zone'