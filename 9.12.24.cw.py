Date:09.12.2024
'''HYBRID INHERITANCE-->COMBINATION OF DIFFERENT INHERITANCE'''
class person:
    def _init_(self,name,age):
        self.name=name
        self.age=age
    def person_info(self):
        print(f"Name of the person: {self.name}\nAge of the person: {self.age}")
class student(person):
    def _init_(self,stu_id):
        self.stu_id=stu_id
    def student_info(self):
        print(f"Student Id: {self.stu_id}")
class Employee(person):
    def _init_(self,emp_id):
        self.emp_id=emp_id
    def Employee_info(self):
        print(f"Employee Id: {self.emp_id}")
class display_details(student,Employee,person):
    def _init_(self,name,age,stu_id,emp_id):
        person._init_(self,name,age)
        student._init_(self,stu_id)
        Employee._init_(self,emp_id)
    def display_all(self):
        self.person_info()
        self.student_info()
        self.Employee_info()
m=display_details("Anika",18,"E24AI003",207645)
m.display_all()

'''Test'''
class Management:
    def getmarks(self):
        self.name=input("Enter the student Name:")
        self.mark1=int(input("Enter the Mark1:"))
        self.mark2=int(input("Enter the Mark2:"))
        self.mark3=int(input("Enter the Mark3:"))
    def show(self):
        print(self.name,self.mark1,self.mark2,self.mark3)
    def percen(self):
        total=self.mark1+self.mark2+self.mark3
        self.percentage=(total/300)*100
    def display(self):
        print(self.percentage)
 class Details(Management):
    def detailsinfo(self):
        self.getmarks()
        self.percen()
    def markdetails(self):
        self.show()
        self.display()
stu=Details()
stu.detailsinfo()
stu.markdetails()
Date:10.12.2024
