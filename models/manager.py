from .employee import Employee

class Manager(Employee):
    def __init__(self, emp_id, name, age, email, base_salary):
        super().__init__(emp_id, name, age, email, base_salary, "Manager")

    def calculate_salary(self):
        return self.base_salary + (self.performance_score * 200)