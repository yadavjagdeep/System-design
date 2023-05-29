from employee import Employee
from employee_bio_data import EmployeeBioData
from salary_calculator import SalaryCalculator


if __name__ == "__main__":
    Emp = Employee(_id="SSN001")
    EmployeeBioData().get_employee_bio_data(Emp)
    SalaryCalculator().calculate_salary(Emp)


