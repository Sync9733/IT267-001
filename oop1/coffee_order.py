class CoffeeOrder:
    menu_type = 'Coffee'
    total = 0
    def __init__(self,customer_name:str,menu:str,price:float,size:str = 'R',num:int = 1) -> None:
        self.customer = customer_name
        self.menu = menu
        self.num = num
        self.size = size
        self.price = price

    def check_menu(self):
        pass

    def compute_price(self):
        if self.size == 'L':
            self.price = self.price +1
        elif self.size == 'XL':
            self.price = self.price +1.5
        else:
            self.price
        CoffeeOrder.total = self.num * self.price

    def display_detail(self):
        print('---- Coffee Order ----')
        print(f'Name  : {self.customer}')
        print(f'Menu  : {self.menu}')
        print(f'Size  : {self.size}')
        print(f'Num   : {self.num}')
        print(f'Price : {self.price}')
        print(f'Total : {self.total}')

if __name__ == '__main__' :
    John = CoffeeOrder('John','Espresso')
    John.display_detail()