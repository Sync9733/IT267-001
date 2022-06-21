from employee import Employee

class EmpMKT(Employee):
    def __init__(self, id, name, salary) -> None:
        super().__init__(id, name, salary)
        self.location = 'Bangkok'
        self.commision = 30
        self.department = 'Marketing'

    def add_location(self,location:str):
        self.location = location

    def add_commision(self,commission:int):
        self.commision = commission

    def emp_detail(self):
        print('===== Employee Marketing Detail ====')
        super().emp_detail()
        print(f'Location : {self.location}')
        print(f'Commission : {self.commision}')

    def mkt_salary(self):
        self._emp_salary()