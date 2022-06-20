#global variable
bird_type = 'parrot'

class Bird:
    #class variable
    bird_name = 'Peter'

    def __init__(self,color) -> None:
        #instance variable
        self.color = color

        #local variable
        country = 'Thailand'
        print(country)


    def show(self):
        return f'{Bird.bird_name} has {self.color}'

if __name__ == '__main__':
    print(f'***** {bird_type} ******') #เรียกใช้ Global variable
    my_bird = Bird('Red,Yellow')
    print(my_bird.show())

    #เรียก class variable (ผิด)
    #print(bird_name) #error    

    #เรียก class variable (ที่ถูกต้อง) ชื่อคลาส.class_variable
    print(Bird.bird_name)

    #เรียก instance variable
    print(my_bird.bird_name)

    #เรียก instnace variable
    #print(Bird.color) #error
    
    #ชื่อวัตถุ instance variable
    print(my_bird.color)