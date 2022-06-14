class Animal:
    #class variable
    animal = 'CAT'

    def new_animal(self,name:str,breed:str,color:str,age:int):
        #instance variable
        self.name = name
        self.breed = breed
        self.color = color
        self.age = age

    def print_detail(self):
        print('***********')
        print(f'Name: {self.name}')
        print(f'Animal: {self.animal}')
        print(f'Breed: {self.breed}')
        print(f'Color: {self.color}')
        print(f'Age: {self.age}')

#create object
if __name__ == "__main__":
    Animal.animal = 'Fish'
    ula = Animal()
    ula.new_animal('Ula','Scottish','White',1)
    ula.animal = 'Dog'
    ula.print_detail()

    drac = Animal()
    drac.new_animal('Ula','Scottish','White',1)
    drac.breed = 'Catfish'
    drac.print_detail()

    #เรียกดูข้อมูลของ object
    Animal.print_detail(ula) #ula.print_detail()
    Animal.print_detail(drac) #drac.print_detail()

    #เรียกดู class valuable ทั้งหมด
    print(f'{Animal.__dict__}')
    print('*****************')

    #เรียกดู instance valuable ทั้งหมด
    print(f'{ula.__dict__}')

    peter = Animal()
    peter.new_animal('Peter','Parrot','Green,Yellow,Red','2')
    # add new attribute to peter
    peter.legs = 2
    print(f'{peter.__dict__}')