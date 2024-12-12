'''#Public
class Student:
    ID=int(input())
    def __init__(self,name):
        self.__name=name
    def display(self):
        print("NAME=",self.__name)

s=Student(input())
s.display()
print(s.ID)
'''
##NAME HANDLING
class Employee:
    def __init__(self):
        self.name=input("Enter your name:")#public
        self.__salary=input("Enter your salary")#private
class Manager(Employee):
    def __init__(self):
        Employee.__init__(self)
        self.M_name=input("Enter manager name:")
        self.__cost=input("Enter manager salary:")
        
emp=Manager()
print("NAME:",emp.name)
print("Salary:",emp._Employee__salary)
print("Manager_name:",emp.M_name)
print("Manager_salary:",emp._Manager__cost)
