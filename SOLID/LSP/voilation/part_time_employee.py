from employee import Employee

class PartTimeEmployee(Employee):

    def __init__(self, _id):
        super().__init__(_id)

    def calculate_salary(self):
        print(f"Calculating salary for emp_type = {self.__class__.__name__} and employee_id = {self.employeeId}")
        # Logic to calculate salary goes here
        return ""
