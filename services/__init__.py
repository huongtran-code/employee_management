# services/__init__.py
from .company import Company
from .payroll import (
    calculate_total_payroll, 
    count_employees_by_type, 
    calculate_total_salary_by_type, 
    calculate_avg_projects
)