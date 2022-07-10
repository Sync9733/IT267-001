from mule import Mule

mule1 = Mule('Mumu','Blue-eyed cream',3,200)
print(f'**** {mule1.name} info ****')
mule1.show_name()
mule1.show_info()

mule2 = Mule('Meme','Palomino',1,120.7)
print(f'**** {mule2.name} info ****')
mule2.sound()
mule2.show_name()
mule2.show_info()