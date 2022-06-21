from employee import Employee


class EmpIT(Employee):
    def __init__(self, id, name, salary) -> None:
        super().__init__(id, name, salary)
        self.skill = None
        self.experience = None
        self.department = 'IT'
    
    def add_skill(self,skill:str):
        self.skill = skill

    def add_experience(self,experience:int):
        self.experience = experience

    def emp_detail(self):
        print('===== Employee IT Detail ====')
        super().emp_detail() #เรียกใช้ method emp_detail ของคลาส Employee #super คือ ดึงข้อมูลใน method มาจาก class แม่
        print(f'Skill : {self.skill}')
        print(f'experience : {self.experience} Years')

    def it_salary(self):
        self._emp_salary()

    