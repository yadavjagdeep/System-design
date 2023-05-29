from full_time_employee import FullTimeEmployee
from part_time_employee import PartTimeEmployee
from volunteer_employee import VolunteerEmployee
from trigger_salary import TriggerSalary


if __name__ == "__main__":
    emp_list = [FullTimeEmployee("FTE001"), PartTimeEmployee("PTE001"), FullTimeEmployee("FTE001"), VolunteerEmployee("VTE001"),
                FullTimeEmployee("FTE001"), PartTimeEmployee("PTE002")]

    TriggerSalary().trigger_salary(emp_list)