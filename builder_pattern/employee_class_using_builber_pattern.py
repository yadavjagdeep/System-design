class Employee:

    def __init__(self, builder: object):
        # to fix warning change names of attributes in builder class
        self.employee_id = builder._employee_id
        self.name = builder._name
        self.phone_numer = builder._phone_numer
        self.age = builder._age
        self.address = builder._address
        self.sex = builder._sex

    def print_all_attributes(self):
        print(self.employee_id)
        print(self.name)
        print(self.phone_numer)
        print(self.age)
        print(self.address)
        print(self.sex)

    class Builder:
        def __init__(self, employee_id: str):
            self._employee_id = employee_id
            self._name = None
            self._phone_numer = None
            self._age = None
            self._address = None
            self._sex = None

        def name(self, name: str):
            self._name = name
            return self

        def phone_numer(self, phone_numer: str):
            self._phone_numer = phone_numer
            return self

        def age(self, age: str):
            self._age = age
            return self

        def address(self, address: str):
            self._address = address
            return self

        def sex(self, sex: str):
            self._sex = sex
            return self

        def build(self):
            return Employee(self)


"""
This approach is also called as chaining
"""
