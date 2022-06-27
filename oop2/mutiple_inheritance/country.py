from geographic import Geographic
from temperature import Temperature

class Country(Geographic,Temperature):
    def __init__(self,name:str,area:float,pop:float) -> None:
        self.name = name
        self.area = area
        self.population = pop

    def getpopulationdensity(self):
        return self.population/self.area

    def showdeatail(self):
        print(f'Country : {self.name}')
        #ชื่อประเทศ

        print(f'Location : {self.get_cordinate()}')
        #สถานที่ตั้ง lattitude and longtitude
        print(f'Population : {self.population:,d}')
        #แสดงจำนวนประชากร
        print(f'Area : {self.area:.2f}')   
        #แสดงขนาดพื้นที่ 
        print(f'Destiny : {self.getpopulationdensity()}')
        #ความหนาแน่นของประชากร

        print(f'Timezone : {self.get_timeZone()}')
        print(f'Climate : {self.get_climate()}')
        print(f'Temperature(C) : {self.get_celsius()}')
        print(f'Temperature(F) : {self.get_fahrenheit()}')
        print(f'Weather : {self.get_weather()}')

