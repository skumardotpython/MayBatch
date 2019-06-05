

class Employee:
    'Employee Class Info'
    empCount = 0
    _privateVariable = "private Value"

    def __init__(self, empId = 0, empName = "DummyName"):
        self.empId = empId #Attrbibutes
        self.empName = empName
        self.salary = 10000


    def DisplayEmployee(self):
        Employee.empCount += 1
        print("Employee Id : ", self.empId)
        print("Employee Name : ", self.empName)
        print("Employee Count : ", Employee.empCount)

    def _PrivateMethod(self):
        print("Private method invoked")

emp1 = Employee(3199, "pragimTech");
emp1.DisplayEmployee();
emp1.DisplayEmployee()
emp1.DisplayEmployee()

emp2 = Employee(3200, "Chadru");
emp2.DisplayEmployee();
emp2.DisplayEmployee()
emp2.DisplayEmployee()

print('-' * 100)

emp3 = Employee()
emp3.empName = "Ravi"
emp3.empId = 4000
emp3.DisplayEmployee()

print('-' * 100)

print(hasattr(emp1, 'empName')) # Returns true if 'empName' attribute exists
print(getattr(emp1, 'empName')) # Returns value of 'empName' attribute
setattr(emp1, 'empName', 'Pragim New Value') # Set empName 'Ravi' at 8
print(getattr(emp1, 'empName')) # Returns value of 'empName' attribute
#delattr(emp1, 'empName') # Delete attribute 'empName'
print(getattr(emp1, 'empName')) # Returns value of 'empName' attribute


print('-' * 100)

print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__ )

# del emp1
# emp1.DisplayEmployee();

print(id(emp1))
print(id(emp2))
print(id(emp3))

emp4 = emp3
print(id(emp4))