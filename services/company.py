import random
from exceptions.employee_exceptions import DuplicateEmployeeError, EmployeeNotFoundError

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        for e in self.employees:
            if e.emp_id == employee.emp_id:
                # Tự động sinh ID mới nếu trùng mã nhân viên [cite: 37]
                new_id = f"{employee.emp_id}_{random.randint(100,999)}"
                employee.emp_id = new_id
                raise DuplicateEmployeeError(f"Trùng ID. Đã tự động đổi ID thành: {new_id}")
        self.employees.append(employee)

    def get_employee(self, emp_id):
        for e in self.employees:
            if e.emp_id == emp_id:
                return e
        # Bắn lỗi nếu tìm hoặc xóa nhân viên không tồn tại 
        raise EmployeeNotFoundError(emp_id)

    def get_all_employees(self):
        if not self.employees:
            # Truy cập danh sách rỗng sẽ báo lỗi [cite: 38]
            raise IndexError("Chưa có dữ liệu")
        return self.employees

# services/payroll.py
def calculate_company_payroll(company):
    try:
        employees = company.get_all_employees()
        return sum(emp.calculate_salary() for emp in employees)
    except IndexError as e:
        print(f"Lỗi: {e}")
        return 0