class Employee:
    def __init__(self,name,ID,position):
        self.name=name
        self.ID=ID
        self.position=position
    def displayemployee(self):
        print(f"Name:{self.name}\nID:{self.ID}\nPosition:{self.position}")
class Address:
    def __init__(self,street,state,country):
        self.street=street
        self.state=state
        self.country=country
    def displayaddress(self):
        print(f"Street Name:{self.street}\nStateName:{self.state}\nCountry Name:{self.country}")
class EmployeeDetais(Employee,Address):
    def __init__(self,name,ID,position,street,state,country):
        super().__init__(name,ID,position)
        Address.__init__(self,street,state,country)
    def displayEmp(self):
        self.displayemployee()
        self.displayaddress()
ed=EmployeeDetais("HAFEESHA",10,"Manager","kambar street","Tamil nadu","INDIA")
ed.displayEmp()
    
        
