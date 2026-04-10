from abc import ABC, abstractmethod
from exceptions.employee_exceptions import ProjectAllocationError

class Employee(ABC):
    def __init__(self, emp_id, name, age, email, base_salary, emp_type):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.email = email
        self.base_salary = base_salary
        self.emp_type = emp_type
        self.projects = []
        self.performance_score = 0.0

    @abstractmethod
    def calculate_salary(self):
        pass

    def add_project(self, project_name):
        # Từ chối phân công dự án nếu đã có 5 dự án [cite: 37]
        if len(self.projects) >= 5:
            raise ProjectAllocationError("Nhân viên đã có đủ 5 dự án.")
        self.projects.append(project_name)

# models/manager.py
from models.employee import Employee
class Manager(Employee):
    def calculate_salary(self):
        return self.base_salary + (self.performance_score * 200)

# models/developer.py
from models.employee import Employee
class Developer(Employee):
    def __init__(self, emp_id, name, age, email, base_salary, prog_lang):
        super().__init__(emp_id, name, age, email, base_salary, "Developer")
        self.prog_lang = prog_lang

    def calculate_salary(self):
        return self.base_salary + (self.performance_score * 100)

# models/intern.py
from models.employee import Employee
class Intern(Employee):
    def calculate_salary(self):
        return self.base_salary * 0.8  # Intern thường nhận % lương cơ bản