import random
class Customber:
    def __init__(self,cust_id,name,phno):
        self.cust_id=cust_id
        self.name=name
        self.phno=phno
    def gen_rand_id(self):
        c_id=ramdom.randint(1000,9999)
        return f"TICK{c_id}"
    def verify_customber_id(cust_id):
        cust_id=input()
        cus_len=len(cust_id)
        if cus_len==8:
            if cust_id[0]=="T" and cust_id[1]=="I" and cust_id[2]=="C" and cust_id[3]=="K":
                if cust_id[4] and cust_id[5] and cust_id[6] and cust_id[7].isdigit()  ==True:
                    print("Valid")
                else:
                    print("last 4 cases not valid")
            else:
                print("first 4 cases not valid")
        else:
            print("length not valid")
class TicketBooking:
    def __init__(self):
        self.events={"Concert":{"price":100,"seats":100},"Movie":{"price":200,"seats":100},"Drama":{"price":300,"seats":100},}
        self.booked_tickets=[] 
    def view_event():
        for events,details in self.events.items():
            print(f"{events}:{details['price']}per ticket{details['seats']}seats are available")
        
        

    def book_tickets(self,even_name,quantity,customber):
        if event_name is self.events:
            event=self.event[event_name]
            if event['seats']>=quantity:
                totalprice=event['price']*quantity
                event['seats']-=quantity
                self.booked_tickets.append({"customber id":customber.cust_id,"event":event_name,"Quantity":quantity,"Total price":totalprice,})
            else:
                print("Seas not available!!!")
        else:
             print("Event name is not availabe!!!!")
        
    def view_tickets(self,customber):
        print("****************Ticket Information*************")
        cus_ticket=[t for t in self.booked_tickets if t["customber_id"]==customber.cust_id]
        if not cus_tickets:
            print("No tickets booked")
        else:
            for tick in cus_ticket:
                print(f"Event:{tick['event']},Quantity: ticket['quantity'],Total cost:{tick['totalprice'],}")
if __name__=="_main_":
    book=Ticketbooking()    
print("************Welcome to TICKET Bokking application*************")
cust_id=input("Enter the costomber ID:")
if Customber.verify_customber_id(cust_id):
    name=input("Enter your name:")
    phno=int(input("Enter your phone number:"))
    customber=Customber(cust_id,name,phno)
    print("****Valid!!! View the booking details*********")
else:
    print("Invalid!!! Please reegister")
    name=input("Enter your name:")
    phno=int(input("Enter your phno:"))
    cust_id=Customber.gen_rand_id()
    customber=Coustomber(cust_id,name,phno)
    print("Your customber id is:",cust_id)

while True:
    print("***Booking Info****")
    print("\n1.View Events")
    print("\n2.Book tickets")
    print("\n3.View my tickets")
    print("\n4.Exit")
    choice=int(input("Enter any options to continue booking"))
    if choice==1:
        book.view_events()
    elif choice==2:
        event_name=input("Enter any event:")
        quantity=int(input("enter the number of tickets:"))
        book.book_tickets(event_name,quantity,customber)
    if choice==3:
        book.view_tickets(customber)
    if choice==4:
        break
        

                     







    
    

