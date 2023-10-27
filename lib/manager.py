from lib.employee import Employee

class Manager:
    all = []
    all_departments = []

    def __init__(self, name, department, age):
        self.name = name
        self.department = department
        self.age = age
        Manager.all.append(self)
        Manager.all_departments.append(self.department)

    @property
    def employees(self):
        employee_list = [employee for employee in Employee.all if employee.manager_name == self]
        return employee_list

    def hire_employee(self, emp_name, salary):
        if isinstance(emp_name, str) and isinstance(salary, int):
            new_employee = Employee(emp_name, salary, self)
        else:
            print("Invalid input for new employee")

    @classmethod
    def average_age(cls):
        ages = [manager.age for manager in cls.all]
        average_age = sum(ages) / len(ages)
        return average_age
