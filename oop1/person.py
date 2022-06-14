class Person:
    country = 'Thailand' #Class variable
    def __init__(self,name,gender,proffession,study) -> None:
        self.name = name #instance variable
        self.gender = gender #instance variable
        self.profession = proffession #instance variable
        self.study2 = study #instance variable

    def work(self):
        print(f'{self.name} is working as a {self.profession}')

    def study(self):
        print(f'{self.name} studies for {self.study2} hour(s)')
    
    def show(self):
        print(f'Name : {self.name}  Gender : {self.gender}  Profession : {self.profession} Study : {self.study2} hour(s)')

person_obj = Person('Jessa','Male','Software Engineer',10)
person_obj.work()
person_obj.study()
person_obj.show()

John = Person('John','Male','Professional',15)
John.work()
John.study()
John.show()

Lisa = Person('Lisa','Female','Korean Singer',15)
Lisa.work()

print(f'Class Variable : {Person.country}')
print(f'Instance Variable : {Lisa.country}')

#assign value
Lisa.country = 'Korean'
print('-----------')
print(f'Class Variable : {Person.country}')
print(f'Instance Variable : {Lisa.country}')
print(f'Instance Variable : {John.country}')

#assign Class variable
Person.country = 'England'
print('-----------')
print(f'Class Variable : {Person.country}')
print(f'Instance Variable : {Lisa.country}')
print(f'Instance Variable : {John.country}')