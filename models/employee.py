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
        if len(self.projects) >= 5:
            raise ProjectAllocationError("Từ chối phân công: Nhân viên đã có đủ 5 dự án.") # [cite: 37]
        self.projects.append(project_name)