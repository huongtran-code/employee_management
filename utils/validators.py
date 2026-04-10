from exceptions.employee_exceptions import InvalidAgeError, InvalidSalaryError

def validate_age(age):
    if not (18 <= age <= 65):
        # Thông báo lỗi tuổi không hợp lệ [cite: 37]
        raise InvalidAgeError("Tuổi phải từ 18 đến 65.")
    return age

def validate_salary(salary):
    if salary <= 0:
        # Thông báo lỗi lương không hợp lệ [cite: 37]
        raise InvalidSalaryError("Lương phải lớn hơn 0.")
    return salary

def validate_email(email):
    if "@" not in email:
        # Lỗi ValueError nếu thiếu @ [cite: 37]
        raise ValueError("Email sai định dạng (thiếu @).")
    return email

def validate_performance(score):
    if not (0 <= score <= 10):
        # Cập nhật điểm không trong khoảng 0-10 ném ValueError [cite: 38]
        raise ValueError("Điểm hiệu suất phải từ 0 đến 10.")
    return score