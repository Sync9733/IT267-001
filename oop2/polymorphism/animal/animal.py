class Animal:
    def __init__(self,name,age) -> None:
        self.__name = name
        self.__age = age
    
    @property #getter สำหรับเรียกค่า private (-) ของ name
    def name(self):
        return self.__name
    @name.setter #setter of name
    def name(self,value):
        self.__name = value

    @property #getter สำหรับเรียกค่า private (-) ของ age
    def age(self):
        return self.__age
    @name.setter #setter of age
    def age(self,value):
        self.__age = value

    def info(self):
        print('-------- Animal information --------')

    def make_sound(self):
        print('======== Animal Sound ========')