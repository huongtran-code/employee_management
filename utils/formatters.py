# utils/formatters.py

def format_currency(amount):
    """Định dạng số tiền thành chuỗi có dấu phẩy và ký hiệu $"""
    return f"${amount:,.2f}"

def print_emp(emp):
    """In thông tin nhân viên, bao gồm cả các dự án đang tham gia"""
    # Xử lý chuỗi dự án: Nếu có dự án thì nối lại bằng dấu phẩy, nếu danh sách rỗng thì hiện "Chưa có"
    projects_str = ", ".join(emp.projects) if emp.projects else "Chưa có"
    
    # In ra màn hình với cột Dự án được thêm vào phía cuối
    print(f"ID: {emp.emp_id:5} | Tên: {emp.name:15} | Chức vụ: {emp.emp_type:10} | Lương: {format_currency(emp.calculate_salary()):10} | Dự án: {projects_str}")