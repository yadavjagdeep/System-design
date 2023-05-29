from employee import Employee

class VolunteerEmployee(Employee):

    def __init__(self, _id):
        super().__init__(_id)

    def calculate_salary(self):
        print(f"ERROR => Calculating salary for emp_type = {self.__class__.__name__} and employee_id = {self.employeeId}")
        # Logic to calculate salary goes here
        raise Exception("Employee type Volunteer are unpaid !!!")

