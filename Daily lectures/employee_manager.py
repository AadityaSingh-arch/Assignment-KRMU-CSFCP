class EmployeeManager:
    def __init__(self, filename="employees.txt"):
        self.filename = filename
    
    def add_employee(self, emp_id, name, salary):
        """Append new employee data to the file"""
        try:
            with open(self.filename, "a") as file:
                file.write(f"{emp_id},{name},{salary}\n")
            print(f"Employee {name} added successfully!")
        except Exception as e:
            print(f"Error adding employee: {e}")
    
    def display_all_employees(self):
        """Display all employee records"""
        try:
            with open(self.filename, "r") as file:
                records = file.readlines()
            
            if not records:
                print("No employee records found.")
                return
            
            print("\n" + "="*50)
            print("EMPLOYEE RECORDS")
            print("="*50)
            print(f"{'ID':<10} {'Name':<20} {'Salary':<15}")
            print("-"*50)
            
            for record in records:
                emp_id, name, salary = record.strip().split(",")
                print(f"{emp_id:<10} {name:<20} ${salary:<14}")
            
            print("="*50 + "\n")
        except FileNotFoundError:
            print("No employee file found. Please add an employee first.")
        except Exception as e:
            print(f"Error displaying employees: {e}")
    
    def search_employee(self, name):
        """Search for a specific employee by name"""
        try:
            with open(self.filename, "r") as file:
                records = file.readlines()
            
            found = False
            print("\n" + "="*50)
            print(f"SEARCH RESULTS FOR: {name}")
            print("="*50)
            
            for record in records:
                emp_id, emp_name, salary = record.strip().split(",")
                if emp_name.lower() == name.lower():
                    print(f"ID: {emp_id}")
                    print(f"Name: {emp_name}")
                    print(f"Salary: ${salary}")
                    found = True
            
            if not found:
                print(f"Employee '{name}' not found.")
            
            print("="*50 + "\n")
        except FileNotFoundError:
            print("No employee file found.")
        except Exception as e:
            print(f"Error searching employee: {e}")


def main():
    manager = EmployeeManager("employees.txt")
    
    while True:
        print("\n--- EMPLOYEE MANAGEMENT SYSTEM ---")
        print("1. Add new employee")
        print("2. Display all employees")
        print("3. Search employee by name")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            emp_id = input("Enter Employee ID: ").strip()
            name = input("Enter Employee Name: ").strip()
            salary = input("Enter Salary: ").strip()
            manager.add_employee(emp_id, name, salary)
        
        elif choice == "2":
            manager.display_all_employees()
        
        elif choice == "3":
            search_name = input("Enter employee name to search: ").strip()
            manager.search_employee(search_name)
        
        elif choice == "4":
            print("Thank you! Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
