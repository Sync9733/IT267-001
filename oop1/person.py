class Person:
    def __init__(self,name,gender,proffession,study) -> None:
        self.name = name
        self.gender = gender
        self.profession = proffession
        self.study2 = study

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

person2_obj = Person('John','Male','Professional',15)
person2_obj.work()
person2_obj.study()
person2_obj.show()

person3_obj = Person('Lisa','Female','Korean Singer',15)
person3_obj.work()