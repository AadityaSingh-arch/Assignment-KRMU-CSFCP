# Create a Python program to perform the following file operations:
# Append new employee data (ID, Name, Salary) into employees.txt
# Display all employee records
# Search for a specific employee by name
class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary 
    def printdisplay(self):
        print(f"Employee Name: {self.name}, Salary: {self.salary}")
if __name__ == "__main__":
    emp1 = employee("Alice", 50000)
    emp1.printdisplay()
class manager(employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    def printdetails(self):
        super().printdisplay()
        print(f"Department: {self.department}")
if __name__ == "__main__":
    mgr1 = manager("Bob", 80000, "Sales")
    mgr1.printdetails()
    
