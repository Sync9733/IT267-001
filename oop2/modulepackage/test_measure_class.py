from re import M
from measure import Measure

"""if __name__ == '__main__':
    m1 = Measure(12.5)
    m2 = Measure(100)
    m3i = Measure(56)
    m4i = Measure(78)
    m5c = Measure(14)
    m6c = Measure(250)
    print(m1.inch_cm())
    print(m2.cm_inch())
    print(m3i.inch_cm())
    print(m4i.inch_cm())
    print(m5c.cm_inch())
    print(m6c.cm_inch())"""

"""inch_list = [52,18,20,40]
for i in inch_list:
        m = Measure(i)
        print(m.inch_cm())"""

num = float(input('Enter number : '))
ch = input('Choose I(inch->cm)or C(cm->inch): ').upper()
m = Measure(num)
if ch == 'I':
    print(m.inch_cm())
elif ch == 'C':
    print(m.cm_inch())
else:
    print('Wrong Character')
