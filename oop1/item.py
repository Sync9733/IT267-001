class Item:
    def __init__(self,name:str,price:float,quanity:int) -> None:
        assert price >= 1 , f"Price should more than 0"
        assert quanity >= 1 , f'Quanity should more than 0'
        
        #รู้ชื่อสินค้า ราคาสินค้า จำนวนสินค้า
        self.name = name
        self.price = price
        self.quanity = quanity

    def calculate_total_price(self):
        #ราคาสุทธิ = ราคาสินค้า * จำนวนสินค้า
        return self.price * self.quanity

    def __del__(self):
        print(f'Object Destroyed')

if __name__ == '__main__':
    #create item
    item1 = Item('Cup',25,2)#50
    item2 = Item('Cone',10,3)#30
    print(f'****Total Price****')
    print(f'{item1.name} : {item1.calculate_total_price()}')
    print(f'{item2.name} : {item2.calculate_total_price()}')