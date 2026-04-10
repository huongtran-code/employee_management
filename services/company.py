import random
from exceptions.employee_exceptions import DuplicateEmployeeError, EmployeeNotFoundError

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        for e in self.employees:
            if e.emp_id == emp.emp_id:
                new_id = f"{emp.emp_id}_{random.randint(100,999)}"
                emp.emp_id = new_id
                self.employees.append(emp)
                raise DuplicateEmployeeError(f"Tự động sinh ID mới: {new_id} do ID cũ bị trùng.") # [cite: 37]
        self.employees.append(emp)

    def get_all_employees(self):
        if not self.employees:
            raise IndexError("Chưa có dữ liệu") # [cite: 38]
        return self.employees

    def get_employee(self, emp_id):
        for e in self.employees:
            if e.emp_id == emp_id:
                return e
        raise EmployeeNotFoundError(emp_id) # [cite: 37]

    def remove_employee(self, emp_id):
        emp = self.get_employee(emp_id) # Sẽ ném lỗi EmployeeNotFoundError nếu không thấy [cite: 38]
        self.employees.remove(emp)