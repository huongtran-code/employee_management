from services.company import Company
from models.developer import Developer
from utils.validators import validate_age, validate_salary, validate_email
from exceptions.employee_exceptions import InvalidAgeError, InvalidSalaryError, DuplicateEmployeeError, EmployeeNotFoundError

def display_menu():
    print("\n" + "="*30)
    print("HỆ THỐNG QUẢN LÝ NHÂN VIÊN CÔNG TY ABC") # [cite: 13]
    print("="*30)
    print("1. Thêm nhân viên mới") # [cite: 13]
    print("2. Hiển thị danh sách nhân viên") # [cite: 13]
    print("3. Tìm kiếm nhân viên") # [cite: 13]
    print("4. Quản lý lương") # [cite: 13]
    print("5. Quản lý dự án") # [cite: 13]
    print("6. Đánh giá hiệu suất") # [cite: 13]
    print("7. Quản lý nhân sự") # [cite: 13]
    print("8. Thống kê báo cáo") # [cite: 13]
    print("9. Thoát") # [cite: 13]
    print("="*30)

def main():
    company = Company()
    
    while True:
        display_menu()
        try:
            choice = int(input("Chọn chức năng (1-9): ")) # [cite: 14]
        except ValueError:
            print("Lỗi: Vui lòng nhập số hợp lệ!") # Nhập số khi menu yêu cầu [cite: 38]
            continue
            
        if choice == 1:
            try:
                emp_id = input("Nhập ID: ")
                name = input("Nhập tên: ")
                age = validate_age(int(input("Nhập tuổi: ")))
                email = validate_email(input("Nhập email: "))
                salary = validate_salary(float(input("Nhập lương cơ bản: ")))
                lang = input("Nhập ngôn ngữ lập trình (cho Developer): ")
                
                dev = Developer(emp_id, name, age, email, salary, lang)
                company.add_employee(dev)
                print("Thêm thành công!")
                
            except (InvalidAgeError, InvalidSalaryError, ValueError) as e:
                print(f"Lỗi đầu vào: {e} - Vui lòng thử lại.")
            except DuplicateEmployeeError as e:
                print(f"Cảnh báo: {e}")
                
        elif choice == 2:
            try:
                emps = company.get_all_employees()
                for e in emps:
                    print(f"ID: {e.emp_id} | Tên: {e.name} | Loại: {e.emp_type}")
            except IndexError as e:
                print(e)
                
        elif choice == 3:
            emp_id = input("Nhập ID cần tìm: ")
            try:
                emp = company.get_employee(emp_id)
                print(f"Đã tìm thấy: {emp.name} ({emp.email})")
            except EmployeeNotFoundError as e:
                print(e)
                
        elif choice == 9:
            print("Đã thoát chương trình.")
            break
        else:
            print("Tính năng đang được phát triển. Vui lòng chọn lại!")

if __name__ == "__main__":
    main()