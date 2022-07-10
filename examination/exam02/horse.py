class Horse:
    max_height = float(200)
    def __init__(self,name:str,color:str) -> None:
        self.name = name
        self.color = color

    def run(self):
        print(f'{self.name} is running')

    def show_name(self):
        print(f'Name : {self.name}')

    def show_info(self):
        print(f'Color : {self.color}\nMax Height : {self.max_height} cm')