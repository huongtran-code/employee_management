class EmployeeException(Exception):
    """Base exception cho hệ thống nhân viên""" # [cite: 19, 20]
    pass

class EmployeeNotFoundError(EmployeeException):
    """Lỗi không tìm thấy nhân viên""" # [cite: 21, 22]
    def __init__(self, employee_id): # [cite: 23]
        self.employee_id = employee_id # [cite: 24]
        super().__init__(f"Không tìm thấy nhân viên có ID: {employee_id}") # [cite: 26]

class InvalidSalaryError(EmployeeException):
    """Lỗi Lương không hợp lệ""" # [cite: 27, 28]
    pass

class InvalidAgeError(EmployeeException):
    """Lỗi tuổi không hợp Lệ (phải 18-65)""" # [cite: 29, 30]
    pass

class ProjectAllocationError(EmployeeException):
    """Lỗi phân công dự án""" # [cite: 31]
    pass

class DuplicateEmployeeError(EmployeeException):
    """Lỗi trùng mã nhân viên""" # [cite: 33, 34]
    pass