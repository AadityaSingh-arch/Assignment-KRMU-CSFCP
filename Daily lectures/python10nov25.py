# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)


# class Student(Person):
#     def __init__(self, fname, lname, marks):
#         super().__init__(fname, lname)
#         self.graduationyear = 2019
#         self.marks = marks

#     def show(self):
#         print(self.marks)


# if __name__ == "__main__":
#     x = Student("riyansh", "yadav", 67)
#     print(x.graduationyear)
#     x.printname()
#     x.show()

#     class employee(Person):
#         def __init__(self, name, id):
#             self.name = name
#             self.id = id

# class employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary 
#     def printdisplay(self):
#         print(f"Employee Name: {self.name}, Salary: {self.salary}")
# if __name__ == "__main__":
#     emp1 = employee("Alice", 50000)
#     emp1.printdisplay()
# class manager(employee):
#     def __init__(self, name, salary, department):
#         super().__init__(name, salary)
#         self.department = department
#     def printdetails(self):
#         super().printdetails()
#         print(f"Department: {self.department}")
# if __name__ == "__main__":
#     mgr1 = manager("Bob", 80000, "Sales")
#     mgr1.printdisplay()



    # //decorators//
def simple_decorator(func):
    def wrapper():
        print(">>> starting the function.")
        func()
        print(">>> finished calling the function.")
    return wrapper
@simple_decorator
def greet():
    print("Hello!")
    greet()