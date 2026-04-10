# services/payroll.py

def calculate_total_payroll(company):
    try:
        employees = company.get_all_employees()
        return sum(emp.calculate_salary() for emp in employees)
    except IndexError:
        return 0

# THÊM CÁC HÀM DƯỚI ĐÂY:

def count_employees_by_type(company):
    """Đếm số lượng nhân viên theo từng loại"""
    counts = {"Manager": 0, "Developer": 0, "Intern": 0}
    try:
        for emp in company.get_all_employees():
            if emp.emp_type in counts:
                counts[emp.emp_type] += 1
            else:
                counts[emp.emp_type] = 1
    except IndexError:
        pass
    return counts

def calculate_total_salary_by_type(company):
    """Tính tổng lương theo từng loại (đại diện cho phòng ban)"""
    salaries = {"Manager": 0.0, "Developer": 0.0, "Intern": 0.0}
    try:
        for emp in company.get_all_employees():
            if emp.emp_type in salaries:
                salaries[emp.emp_type] += emp.calculate_salary()
            else:
                salaries[emp.emp_type] = emp.calculate_salary()
    except IndexError:
        pass
    return salaries

def calculate_avg_projects(company):
    """Tính số dự án trung bình trên mỗi nhân viên"""
    try:
        employees = company.get_all_employees()
        total_projects = sum(len(emp.projects) for emp in employees)
        return total_projects / len(employees)
    except IndexError:
        return 0.0