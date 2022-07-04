from shapetype import *

#Menu
print('==== Compute Area ====')
print('1) Square')
print('2) Circle')
print('3) Triangle')
choice = int(input('Enter choice (1-3): '))
print('------------------------')

#check choice
if choice == 1:
    s = Square()
    s.length = float(input('Enter Length : '))
    s.print_sqaure()

elif choice ==2:
    c = Circle()
    c.radius = float(input('Enter Radius : '))
    c.print_circle()

elif choice ==3:
    t = Triangle()
    t.base = float(input('Enter Base : '))
    t.height = float(input('Enter Height : '))
    t.print_triangle()

else :
    print('Wrong choice !!!!')