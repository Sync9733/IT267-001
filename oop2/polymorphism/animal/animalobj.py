#from animalsubclass import Dog,Cat,Cow
from animalsubclass import * # เครื่องหมาย * สำหรับเรียกใช้ทุก class

dogobj = Dog('Fluffy',4)
catobj = Cat('Milo',2.5)
cowobj = Cow('Phil',5)

"""dogobj.info()
dogobj.make_soud()
catobj.info()
catobj.make_soud()
cowobj.info()
cowobj.make_soud()"""

for animal in (dogobj,catobj,cowobj):
    print('#######################')
    animal.info()
    animal.make_soud()