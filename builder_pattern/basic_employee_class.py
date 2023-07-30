class Employee:

    def __init__(self, name: str, employee_id: str, phone_numer: str, age=None, sex=None, address=None):
        self.name = name
        self.emp_id = employee_id
        self.age = age
        self.sex = sex
        self.phone_numer = phone_numer
        self.address = address

    def get_employee_bio_data(self, employee_id):
        pass


"""
Let's look at the problems here:

1. when a client is creating an instance of the class, he/she needs to understand what all fields are mandatory and 
optional, even he does not needs to use some fields.

2. The initializer has too much fields to accept which is not good.

=> One way to solve this problem is buy using method overloading, but python does not support method overloading directly,
anyway method overloading is not a good solution as it will create another problem of combinatorial explosion.

=> Another good way is to create a separate class and load input to that and pass object of that class to init of 
Employee class, but defining a class outside is not a good approach

"""
