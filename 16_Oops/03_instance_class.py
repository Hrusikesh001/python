class Employee:
    company = "Asus"
    
    def __init__(self, salary, name, bond, company):
        self.salary = salary  # Create an instance attribute of name salary and assign it with salary
        self.name = name 
        self.bond = bond
        self.company = company

    def get_salary(self): # self is important here beacause self is a  way to reference the object of the class which is being created
        return self.salary
    
    def get_info(self):
        print(f"The name of the employee is {self.name}.Salary is {self.salary}. The bond is for {self.bond} years")

    
e1 = Employee(34000,"John",4, "Tesla")
print(e1.company)  # will always print instance attribute whenever present
print(Employee.company)  # This will always print the class attribute

# Object interospection
print(dir(e1))
