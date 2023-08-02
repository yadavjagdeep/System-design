from collections import defaultdict

""" We are needed to make this class thread safe"""


class EmployeeIdStore:
    __INSTANCE = None

    def __init__(self):
        self.employees = defaultdict()
        # read data from db
        self.employees["101"] = "Jagdeep"
        self.employees["102"] = "Ankit"
        self.employees["103"] = "Vibhor"

    def __new__(cls, *args, **kwargs):
        if not cls.__INSTANCE:
            cls.__INSTANCE = super().__new__(cls)
        return cls.__INSTANCE

    def get_employee(self, employee_id: str):
        if not employee_id:
            raise RuntimeError("employee_id cannot be none !!!")
        if self.employees.get(employee_id, None):
            self.employees.get(employee_id)
        else:
            print(f"No employee exists for employee_id = {employee_id}")
        return None
