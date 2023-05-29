"""
 -Idea is a class should have only one reason to change
"""

class Employee:
    def __init__(self, _id):
        self._employeeId = _id

    @property
    def employeeId(self):
        return self._employeeId

    def employeeSalary(self):
        salary = None
        # salary calculation logic
        print("Calculating salary...")
        return salary

    def employeeBioData(self):
        data = None
        print("Fetching Employee Bio Data...")
        # fetch bio_data and update it in data variable
        return data

    def employeePerformance(self):
        performance_report = None
        print("Creating performance report")
        # the logic behind a performance report goes here
        return performance_report


# A simple employee class might look like this, we can make it an abstract class for implement these method basis
# different employee types
"""
 -Problem with this class or the class implementing this class if we make it abstract is, it has multiple reason to change
 -If salary calculation logic changes this class has to suffer
 -If there is some change in response format of employeeBioData this class has to suffer
 -If there is any change in response format or performance matrix calculation this class has to suffer
"""
# we can see that this class has multiple reason to change

" => According to SRP a class should have only one reason to changes "

# what we can do is create a separate class for each responsibility
"""
 -Now we have separated each responsibility in separate class, for changes in particular responsibility, that class wil
 suffer only
"""