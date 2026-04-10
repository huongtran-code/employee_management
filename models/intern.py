from .employee import Employee

class Intern(Employee):
    def __init__(self, emp_id, name, age, email, base_salary):
        super().__init__(emp_id, name, age, email, base_salary, "Intern")

    def calculate_salary(self):
        return self.base_salary * 0.8