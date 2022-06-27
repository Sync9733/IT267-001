from documentary_private import Documentary

m = Documentary('Mulan',2020,'Action')
#m.__get_movie() #เรียก private method ไม่ได้
#print(m.__genre)
m.print_detail()
print(f'year : {m._Movie__year}')
#obj._Classname__privateattribute