class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def getAnnualSalary(self):
        return self.salary * 12

    def increaseSalary(self, percent):
        self.salary += self.salary * percent / 100


employee = Employee("Mike", "Data Analyst", 2000)

employee.increaseSalary(10)

print(employee.name)
print(employee.position)
print(employee.salary)
print(employee.getAnnualSalary())
