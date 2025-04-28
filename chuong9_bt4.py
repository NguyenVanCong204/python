class Person:
    def __init__(self, employee_id, name, age=20):
        self.employee_id = employee_id
        self.name = name
        self.__age = age  # Private property
    
    def set_age(self, age):
            self.__age = age
    def get_age(self):
        return self.__age
    
david = Person(101, "Alice")

print("Tuổi của David : ",david.get_age())

david.set_age(99)

print("Tuổi của David : ",david.get_age())