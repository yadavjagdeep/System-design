"""
 => LSP (Liskov Substitution Principle)
 - Inheritance should not be used for code re-usability
 - We should use Inheritance only where is there is a 'strict' 'is-a' relation-ship b/w parent and child
 => In more generic terms we should use inheritance only is subclass can we substituted in parent class
"""

class Employee:

    def __init__(self, _id):
        self._employeeId = _id

    @property
    def employeeId(self):
        return self._employeeId

    def calculate_salary(self):
        salary = None
        # logic to calculate salary goes here, and update salary variable
        return salary



"""
 - Consider a case if this class is to be used for an NGO
 - An NGO can have different types of employees like, full-time, part-time, adhoc, volunteer
 - If we create instance of all the employee by inheriting the above 'Employee' class, then it may not be correct for 'volunteer',
    as it does not any salary, in that case we may raise an exception, but this problem will not be eliminated.
 - If we pass instances of objects of all the employee in the organization to trigger salary we have to add handling of 'volunteer' there as well.
 - check TriggerSalary class
"""