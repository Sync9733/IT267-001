from animal import Animal

class Dog(Animal):
    def info(self):
         #super().info()
        Animal.info(self) #-------- Animal information --------
        print('I am a dog.')
        print(f'My name is {self.name}')
        print(f'I am {self.age} years old')
    
    def make_soud(self):
        Animal.make_sound(self) #======== Animal Sound ========
        print(f'Hey! I make Woof!! Woof!! sound.')

class Cat(Animal):
    def info(self):
         #super().info()
        Animal.info(self) #-------- Animal information --------
        print('I am a Cat.')
        print(f'My name is {self.name}')
        print(f'I am {self.age} years old')
    
    def make_soud(self):
        Animal.make_sound(self) #======== Animal Sound ========
        print(f'Hey! I make Meow!! Meow!! sound.')

class Cow(Animal):
    def info(self):
         #super().info()
        Animal.info(self) #-------- Animal information --------
        print('I am a Cow.')
        print(f'My name is {self.name}')
        print(f'I am {self.age} years old')
    
    def make_soud(self):
        Animal.make_sound(self) #======== Animal Sound ========
        print(f'Hey! I make Moo!! Moo!! sound.')