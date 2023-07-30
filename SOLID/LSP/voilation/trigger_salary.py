from volunteer_employee import VolunteerEmployee

class TriggerSalary:

    def trigger_salary(self, employee: list):
        """
        :param employee: list of diff employee objects
        :return:
        """
        for emp in employee:
            if isinstance(emp, VolunteerEmployee):
                print("Skipping salary trigger for volunteer employee !!!")
                continue
            salary = emp.calculate_salary()
            # logic to trigger salary goes here

"""
 - Problems with this approach is above class 'Trigger' salary need to have 
"""