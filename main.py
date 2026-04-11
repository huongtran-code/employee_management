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
    print("HỆ THỐNG QUẢN LÝ NHÂN SỰ") 
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
            print("\n--- QUẢN LÝ DỰ ÁN ---")
            print("a. Phân công nhân viên vào dự án")
            print("b. Xóa nhân viên khỏi dự án")
            print("c. Hiển thị dự án của 1 nhân viên")
            # --- Các chức năng mới thêm từ ảnh ---
            print("d. Top 10 nhân viên tham gia nhiều dự án nhất")
            print("e. Top 10 nhân viên tham gia ít dự án nhất")
            print("f. Danh sách thành viên tham gia 1 dự án và chức vụ")
            
            sub5 = input("Chọn chức năng (a-f): ").lower()
            
            if sub5 == 'a':
                emp_id = input("Nhập ID nhân viên để phân công: ")
                try:
                    e = company.get_employee(emp_id)
                    proj = input("Nhập tên dự án: ")
                    e.add_project(proj)
                    print("Phân công thành công!")
                except EmployeeNotFoundError as e:
                    print(e)
                except ProjectAllocationError as e:
                    print(e)
                    
            elif sub5 == 'b':
                emp_id = input("Nhập ID nhân viên: ")
                try:
                    e = company.get_employee(emp_id)
                    proj = input("Nhập tên dự án cần xóa: ")
                    if proj in e.projects:
                        e.projects.remove(proj)
                        print("Xóa dự án thành công!")
                    else:
                        print("Nhân viên không tham gia dự án này.")
                except EmployeeNotFoundError as e:
                    print(e)
                    
            elif sub5 == 'c':
                emp_id = input("Nhập ID nhân viên: ")
                try:
                    e = company.get_employee(emp_id)
                    print(f"Các dự án của {e.name}: {', '.join(e.projects) if e.projects else 'Chưa có'}")
                except EmployeeNotFoundError as e:
                    print(e)
                    
            elif sub5 == 'd':
                try:
                    emps = company.get_all_employees()
                    # Sắp xếp theo số lượng dự án giảm dần, lấy top 10
                    top_10 = sorted(emps, key=lambda x: len(x.projects), reverse=True)[:10]
                    print("\n--- TOP 10 NHÂN VIÊN NHIỀU DỰ ÁN NHẤT ---")
                    for e in top_10:
                        print(f"ID: {e.emp_id:5} | Tên: {e.name:15} | Số dự án: {len(e.projects)}")
                except IndexError as e:
                    print(f"Thông báo: {e}")
                    
            elif sub5 == 'e':
                try:
                    emps = company.get_all_employees()
                    # Sắp xếp theo số lượng dự án tăng dần, lấy top 10
                    bottom_10 = sorted(emps, key=lambda x: len(x.projects))[:10]
                    print("\n--- TOP 10 NHÂN VIÊN ÍT DỰ ÁN NHẤT ---")
                    for e in bottom_10:
                        print(f"ID: {e.emp_id:5} | Tên: {e.name:15} | Số dự án: {len(e.projects)}")
                except IndexError as e:
                    print(f"Thông báo: {e}")
                    
            elif sub5 == 'f':
                proj_name = input("Nhập tên dự án cần xem: ")
                try:
                    emps = company.get_all_employees()
                    participants = [e for e in emps if proj_name in e.projects]
                    if participants:
                        print(f"\n--- DANH SÁCH THÀNH VIÊN DỰ ÁN '{proj_name}' ---")
                        for e in participants:
                            print(f"ID: {e.emp_id:5} | Tên: {e.name:15} | Chức vụ: {e.emp_type}")
                    else:
                        print("Không có nhân viên nào tham gia dự án này.")
                except IndexError as e:
                    print(f"Thông báo: {e}")
            else:
                print("Lựa chọn không hợp lệ!")
                
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
            print("\n--- QUẢN LÝ NHÂN SỰ ---")
            print("a. Xóa 1 nhân viên (nghỉ việc)")
            print("b. Tăng lương cơ bản cho nhân viên")
            print("c. Thăng chức")
            # --- Chức năng mới thêm từ ảnh ---
            print("d. Cắt giảm nhân sự (Cho nghỉ việc nhiều nhân viên)")
            
            sub7 = input("Chọn chức năng (a-d): ").lower()
            
            if sub7 == 'a':
                emp_id = input("Nhập ID nhân viên cần xóa: ")
                try:
                    company.remove_employee(emp_id)
                    print("Xóa nhân viên thành công!")
                except EmployeeNotFoundError as e:
                    print(e)
                    
            elif sub7 == 'b':
                emp_id = input("Nhập ID nhân viên cần tăng lương: ")
                try:
                    e = company.get_employee(emp_id)
                    new_salary = input_with_retry("Nhập mức lương mới: ", float, validate_salary)
                    e.base_salary = new_salary
                    print("Cập nhật lương thành công!")
                except EmployeeNotFoundError as e:
                    print(e)
                    
            elif sub7 == 'c':
                print("\n--- THĂNG CHỨC NHÂN VIÊN ---")
                emp_id = input("Nhập ID nhân viên cần thăng chức: ")
                try:
                    # Tìm nhân viên hiện tại
                    emp_to_promote = company.get_employee(emp_id)
                    
                    if emp_to_promote.emp_type == "Intern":
                        print(f"Nhân viên {emp_to_promote.name} hiện là Intern. Thăng chức lên Developer.")
                        lang = input("Nhập ngôn ngữ lập trình cho vai trò Developer: ")
                        # Tạo object Developer mới
                        new_emp = Developer(
                            emp_to_promote.emp_id, 
                            emp_to_promote.name, 
                            emp_to_promote.age, 
                            emp_to_promote.email, 
                            emp_to_promote.base_salary, 
                            lang
                        )
                    elif emp_to_promote.emp_type == "Developer":
                        print(f"Nhân viên {emp_to_promote.name} hiện là Developer. Thăng chức lên Manager.")
                        # Tạo object Manager mới
                        new_emp = Manager(
                            emp_to_promote.emp_id, 
                            emp_to_promote.name, 
                            emp_to_promote.age, 
                            emp_to_promote.email, 
                            emp_to_promote.base_salary
                        )
                    elif emp_to_promote.emp_type == "Manager":
                        print(f"Nhân viên {emp_to_promote.name} đã là Manager (cấp bậc cao nhất). Không thể thăng chức thêm.")
                        continue # Bỏ qua phần cập nhật bên dưới
                        
                    # Giữ lại danh sách các dự án và điểm hiệu suất cũ của nhân viên
                    new_emp.projects = emp_to_promote.projects.copy()
                    new_emp.performance_score = emp_to_promote.performance_score
                    
                    # Tìm vị trí của nhân viên cũ trong danh sách và thay thế bằng nhân viên mới
                    index = company.employees.index(emp_to_promote)
                    company.employees[index] = new_emp
                    
                    print(f"[*] Thăng chức thành công! {new_emp.name} nay đã là {new_emp.emp_type}.")
                    
                except EmployeeNotFoundError as err: # Bắt lỗi nếu nhập sai ID
                    print(err)
                
            elif sub7 == 'd':
                print("\n--- CẮT GIẢM NHÂN SỰ ---")
                ids_input = input("Nhập danh sách ID các nhân viên cần cho nghỉ việc (cách nhau bằng dấu phẩy, VD: NV01, NV02): ")
                
                # Tách chuỗi thành danh sách ID và loại bỏ khoảng trắng dư thừa
                ids_to_remove = [i.strip() for i in ids_input.split(",") if i.strip()]
                
                success_count = 0
                for emp_id in ids_to_remove:
                    try:
                        company.remove_employee(emp_id)
                        print(f"[+] Đã cho nghỉ việc nhân viên ID: {emp_id}")
                        success_count += 1
                    except EmployeeNotFoundError:
                        print(f"[-] Không tìm thấy ID: {emp_id} để cắt giảm.")
                        
                print(f"=> Tổng kết: Đã cắt giảm thành công {success_count}/{len(ids_to_remove)} nhân sự được yêu cầu.")
            else:
                print("Lựa chọn không hợp lệ!")
                
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