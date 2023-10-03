# Class DerivedClass(BaseClass):
#     {body}


class Person:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def display(self):
        print(self.name, self.id)


class Emp(Person):
    def __init__(self,name, id, department):
        self.dept = department
        Person.__init__(self,name,id)
    def employee(self):
        print(self.dept,"employee class called")


emp_details = Emp("mario",102, "it")
emp_details.display()
emp_details.employee()