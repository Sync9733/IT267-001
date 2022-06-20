"""import measure_convert as my

measure = float(input('กรอกหน่วย : '))
if __name__ == '__main__':
    print(f'{measure} เซนติเมตร = {my.cm_to_inch(measure):.2f} นิ้ว')
    print(f'{measure} นิ้ว = {my.inch_to_cm(measure):.2f} เซนติเมตร')"""

from measure_convert import inch_to_cm,cm_to_inch

if __name__ == '__main__':
    print(inch_to_cm(12.5))
    print(cm_to_inch(100))