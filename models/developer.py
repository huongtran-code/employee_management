from .employee import Employee

class Developer(Employee):
    def __init__(self, emp_id, name, age, email, base_salary, prog_lang):
        super().__init__(emp_id, name, age, email, base_salary, "Developer")
        self.prog_lang = prog_lang

    def calculate_salary(self):
        return self.base_salary + (self.performance_score * 100)