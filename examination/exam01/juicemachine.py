class Juiceorder:
    def __init__(self,menu:str,size:str,price:int = 0) -> None:
        self.menu = menu.upper()
        self.size = size.upper()
        self.price = price
    
    def check_menu(self):
        if self.menu == 'ORANGE JUICE':
           self.menu = 'OJ'
           self.price = 25

        elif self.menu == 'APPLE JUICE':
            self.menu = 'AJ'
            self.price = 25

        elif self.menu == 'WATERMELON JUICE':
            self.menu = 'WJ'
            self.price = 30

        elif self.menu == 'PINEAPPLE JUICE':
            self.menu = 'PJ'
            self.price = 30
        
    def compute_price(self):
        if self.size == 'L':
            self.price = self.price + 5
        else:
            self.price
    
    def display_order(self):
        self.check_menu()
        self.compute_price()
        print(f'{self.menu}({self.size}*{self.price})=>{self.price} baht')