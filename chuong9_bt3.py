class Employee:
    def __init__(self, employee_id, name, salary=0):
        self.employee_id = employee_id
        self.name = name
        self.__salary = salary  # Private property
    
    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Salary must be a positive value!")
    
    def get_salary(self):
        return self.__salary

# Tạo hai nhân viên
employee1 = Employee(101, "Alice")
employee2 = Employee(102, "Bob")

# Thiết lập lương cho nhân viên
employee1.set_salary(5000)
employee2.set_salary(6000)

# In thông tin nhân viên
print("employee1")
print("Id : ",employee1.employee_id)
print("Name : ",employee1.name)
print("Salary : ",employee1.get_salary())
print("----------------------")
print("employee2")
print("Id : ",employee2.employee_id)
print("Name : ",employee2.name)
print("Salary : ",employee2.get_salary())