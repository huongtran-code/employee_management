from exceptions.employee_exceptions import InvalidAgeError, InvalidSalaryError

def validate_age(age):
    if not (18 <= age <= 65):
        raise InvalidAgeError("Tuổi phải từ 18 đến 65.") # [cite: 37]
    return age

def validate_salary(salary):
    if salary <= 0:
        raise InvalidSalaryError("Lương phải lớn hơn 0.") # [cite: 37]
    return salary

def validate_email(email):
    if "@" not in email:
        raise ValueError("Email sai định dạng (thiếu @).") # [cite: 37]
    return email

def validate_performance(score):
    if not (0 <= score <= 10):
        raise ValueError("Điểm hiệu suất phải từ 0 đến 10.") # [cite: 38]
    return score