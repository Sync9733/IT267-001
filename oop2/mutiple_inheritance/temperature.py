class Temperature:
    def set_celsius(self,celsius:float):
        self.celcius = celsius

    def get_celsius(self):
        return self.celcius

    def get_fahrenheit(self):
        return (self.celcius*1.8)+32

    def get_weather(self):
        if self.celcius <= 0:
            return 'Freezing'
        elif self.celcius <= 18:
            return 'Cold'
        elif self.celcius <= 28:
            return 'Warm'
        else:
            return('Hot')  