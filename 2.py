'''class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displayPerson(self):
        print("Name=",self.name,"\nAge=",self.age)
class Employee(Person):
    def __init__(self,name,age,ID):
        super().__init__(name,age)
        self.ID=ID
    def displayEmployee(self):
        self.displayPerson()
        print("ID=",self.ID)
class Manager(Employee):
    def __init__(self,name,age,ID,salary):
        super(). __init__(name,age,ID)
        self.salary=salary
    def display(self):
        self.displayEmployee()
        print("Salary=",self.salary)
emp=Manager("Harini",19,100,10000000)
emp.display()
        
'''        
#HIERARCHICAL INHERITANCE
class Parent:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(f"Parent_Name:{self.name}")
class child1(Parent):
    def __init__(self,name,child1_name):
        Parent.__init__(self,name)
        self.child1_name=child1_name
    def display1(self):
        self.display()
        print(f"Child1_Name:{self.child1_name}")
class child2(Parent):
    def __init__(self,name,child2_name):
        Parent.__init__(self,name)
        self.child2_name=child2_name
    def display2(self):
        print(f"Child2_Name:{self.child2_name}")
a=child1("Rickshitha","harini")
a.display1()
b=child2("Rickshitha","Hafeesha")
b.display2()






        
      
        





                         ,
        
