class Employee:
    def __init__(self, _id):
        print("Creating Employee object...")
        self._employeeId = _id

    @property
    def employee_id(self):
        return self._employeeId