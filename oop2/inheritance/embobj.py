from empit import EmpIT
from empMKT import EmpMKT

#create object employee IT
mike = EmpIT('001','Mike',60000)
mike.add_skill('Python, Javascript')
mike.add_experience(5)
mike.emp_detail()
mike.it_salary()

#create object employee MKT
anna = EmpMKT('002','Anna',35000)
anna.emp_detail()
anna.mkt_salary()
#พนักงานแผนการตลาดชื่อ Paul มีเงินเดือน 45,000 ได้รับ commision 35% โดยทำงานอยุ่ในจ.เชียงใหม่

paul = EmpMKT('003','Paul',45000)
paul.add_commision(35)
paul.add_location('Chiang mai')
paul.emp_detail()
paul.mkt_salary()