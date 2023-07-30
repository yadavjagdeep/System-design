from builder_pattern.employee_class_using_builber_pattern import Employee

if __name__ == "__main__":
    obj = Employee.Builder("ID123").name("Amit").sex("male").age(23).build()
    print(obj.print_all_attributes())

