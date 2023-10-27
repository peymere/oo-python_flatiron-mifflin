class Employee:
    all = []

    def __init__(self, name, salary, manager_name):
        self.name = name
        self.salary = salary
        self.manager_name = manager_name
        Employee.all.append(self)

    def tax_bracket(self):
        bracket_low = self.salary - 1000
        bracket_high = self.salary + 1000
        return [emp for emp in Employee.all if emp != self and bracket_low <= emp.salary <= bracket_high]

    @classmethod
    def paid_over(cls, number):
        return [employee for employee in cls.all if employee.salary > number]
    
    @classmethod
    def find_by_department(cls, dep_name):
        return [emp for emp in Employee.all if emp.manager_name.department == dep_name][0]

