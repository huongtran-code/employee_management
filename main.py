from models import Manager, Developer, Intern
from services import Company, calculate_total_payroll, count_employees_by_type, calculate_total_salary_by_type, calculate_avg_projects
from utils import validate_age, validate_salary, validate_email, validate_performance, print_emp, format_currency
from exceptions import InvalidAgeError, InvalidSalaryError, DuplicateEmployeeError, EmployeeNotFoundError, ProjectAllocationError

def input_with_retry(prompt, type_cast, validator=None):
    """Hàm hỗ trợ nhập dữ liệu và tự động yêu cầu nhập lại nếu có lỗi"""
    while True:
        try:
            val = type_cast(input(prompt))
            if validator:
                return validator(val)
            return val
        except ValueError as e:
            if "invalid literal" in str(e):
                print("Lỗi: Vui lòng nhập đúng định dạng số!") 
            else:
                print(f"Lỗi: {e} - Yêu cầu nhập lại.") 
        except (InvalidAgeError, InvalidSalaryError) as e:
            print(f"Lỗi: {e} - Yêu cầu nhập lại.") 

def display_menu():
    print("\n" + "="*40)
    print("HỆ THỐNG QUẢN LÝ NHÂN VIÊN CÔNG TY ABC") 
    print("="*40)
    print("1. Thêm nhân viên mới") 
    print("2. Hiển thị danh sách nhân viên") 
    print("3. Tìm kiếm nhân viên") 
    print("4. Quản lý lương") 
    print("5. Quản lý dự án") 
    print("6. Đánh giá hiệu suất") 
    print("7. Quản lý nhân sự") 
    print("8. Thống kê báo cáo") 
    print("9. Thoát") 
    print("="*40)

def main():
    company = Company()
    
    while True:
        display_menu()
        try:
            choice = int(input("Chọn chức năng (1-9): ")) 
        except ValueError:
            print("Lỗi: Bạn phải nhập một số. Yêu cầu nhập lại!") 
            continue
            
        if choice == 1:
            print("a. Thêm Manager | b. Thêm Developer | c. Thêm Intern") 
            emp_type = input("Chọn loại nhân viên (a/b/c): ").lower()
            
            emp_id = input("Nhập ID: ")
            name = input("Nhập tên: ")
            email = input_with_retry("Nhập email: ", str, validate_email)
            age = input_with_retry("Nhập tuổi (18-65): ", int, validate_age)
            salary = input_with_retry("Nhập lương cơ bản: ", float, validate_salary)
            
            try:
                if emp_type == 'a':
                    emp = Manager(emp_id, name, age, email, salary)
                elif emp_type == 'b':
                    lang = input("Nhập ngôn ngữ lập trình: ")
                    emp = Developer(emp_id, name, age, email, salary, lang)
                elif emp_type == 'c':
                    emp = Intern(emp_id, name, age, email, salary)
                else:
                    print("Lựa chọn không hợp lệ!")
                    continue
                
                company.add_employee(emp)
                print("Thêm nhân viên thành công!")
            except DuplicateEmployeeError as e:
                print(f"Cảnh báo: {e}") 
                
        elif choice == 2:
            try:
                employees = company.get_all_employees()
                print("\n--- HIỂN THỊ DANH SÁCH NHÂN VIÊN ---")
                print("a. Tất cả nhân viên")
                print("b. Theo loại (Manager/Developer/Intern)")
                print("c. Theo hiệu suất (từ cao đến thấp)")
                sub_choice = input("Chọn chế độ hiển thị (a/b/c): ").lower()

                if sub_choice == 'a':
                    for e in employees:
                        print_emp(e)
                        
                elif sub_choice == 'b':
                    emp_type = input("Nhập loại nhân viên cần xem (Manager/Developer/Intern): ").capitalize()
                    filtered_emps = [e for e in employees if e.emp_type == emp_type]
                    if filtered_emps:
                        for e in filtered_emps:
                            print_emp(e)
                    else:
                        print(f"Không có nhân viên nào thuộc loại {emp_type}.")
                        
                elif sub_choice == 'c':
                    # Sắp xếp nhân viên theo điểm hiệu suất giảm dần
                    sorted_emps = sorted(employees, key=lambda x: x.performance_score, reverse=True)
                    for e in sorted_emps:
                        # In thêm điểm hiệu suất ở đầu để dễ quan sát
                        print(f"[Điểm: {e.performance_score}/10] ", end="")
                        print_emp(e)
                else:
                    print("Lựa chọn không hợp lệ!")
                    
            except IndexError as e:
                print(f"Thông báo: {e} - Bạn cần thêm nhân viên (Chức năng 1) trước!")
                
        elif choice == 3:
            emp_id = input("Nhập ID cần tìm: ")
            try:
                e = company.get_employee(emp_id)
                print("Đã tìm thấy:")
                print_emp(e)
            except EmployeeNotFoundError as e:
                print(e) 
                
        elif choice == 4:
            total = calculate_total_payroll(company)
            print(f"Tổng lương công ty: {format_currency(total)}") 
            
        elif choice == 5:
            emp_id = input("Nhập ID nhân viên để phân công dự án: ")
            try:
                e = company.get_employee(emp_id)
                proj = input("Nhập tên dự án: ")
                e.add_project(proj)
                print("Phân công thành công!")
            except EmployeeNotFoundError as e:
                print(e)
            except ProjectAllocationError as e:
                print(e) # [cite: 37]
                
        elif choice == 6:
            emp_id = input("Nhập ID nhân viên cần đánh giá: ")
            try:
                e = company.get_employee(emp_id)
                score = input_with_retry("Nhập điểm hiệu suất (0-10): ", float, validate_performance)
                e.performance_score = score
                print("Cập nhật điểm thành công!")
            except EmployeeNotFoundError as e:
                print(e)

        elif choice == 7:
            emp_id = input("Nhập ID nhân viên cần xóa: ")
            try:
                company.remove_employee(emp_id)
                print("Xóa nhân viên thành công!")
            except EmployeeNotFoundError as e:
                print(e) 
                
        elif choice == 8:
            try:
                # Kiểm tra xem có nhân viên nào không, nếu không sẽ ném lỗi IndexError
                company.get_all_employees() 
                
                print("\n--- THỐNG KÊ BÁO CÁO ---")
                
                # a. Số lượng nhân viên theo loại
                print("a. Số lượng nhân viên theo loại:")
                counts = count_employees_by_type(company)
                for emp_type, count in counts.items():
                    print(f"   - {emp_type}: {count} nhân viên")
                
                # b. Tổng lương theo phòng ban (loại nhân viên)
                print("\nb. Tổng lương theo loại (phòng ban):")
                salaries = calculate_total_salary_by_type(company)
                for emp_type, total in salaries.items():
                    print(f"   - {emp_type}: {format_currency(total)}")
                
                # c. Số dự án trung bình
                print("\nc. Số dự án trung bình trên mỗi nhân viên:")
                avg_proj = calculate_avg_projects(company)
                print(f"   - {avg_proj:.2f} dự án/nhân viên")
                
            except IndexError as e:
                print(f"Thông báo: {e} - Không có dữ liệu để thống kê.")
                
        elif choice == 9:
            print("Đã thoát chương trình.") 
            break
        else:
            print("Vui lòng chọn từ 1 đến 9.")

if __name__ == "__main__":
    main()