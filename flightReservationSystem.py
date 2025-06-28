class reservation:                    #Class for reservation
 def __init__(self):      #constructor to initialize the variables
  self.fname=None
  self.lname=None
  self.age=0
  self.gend=None
  self.contact=0
  self.email=None
  self.pnr=0
  self.deptime=None
  self.arrtime=None
  self.flight=None
  self.date=0
  self.next=None

class Seatreservation:                 #Class for seat reservation
 def __init__(self):       #constructor to initialize the head & data
  self.head=None
  self.fname=None
  self.lname=None
  self.age=0
  self.gend=None
  self.contact=0
  self.email=None
  self.pnr=0
  self.deptime=None
  self.arrtime=None
  self.flight=None
  self.cargo=None
  self.cargodes=None
  self.cargocharges=0
  self.date=0
  self.ctr=0
  self.cargo=None
  self.cargodes=None
  self.cargocharges=0

 def seatreser(self):     #seat reservation module
  temp=reservation()
  temp.fname=input("Enter First Name:")
  temp.lname=input("Enter Last Name:")
  temp.age=int(input("Enter your age:"))
  temp.gend=input("Enter your Gender(M/F):")
  temp.contact=int(input("Enter your Contact number:"))
  temp.email=input("Enter your Email ID:")
  temp.pnr=int(input("Enter PNR number:"))
  print("Flights Available")
  print("Flight 1 :AirIndia         Departure:09:00       Arrival:12:00")
  print("Flight 2 :IndiGo           Departure:14:00       Arrival:17:00")
  print("Flight 3 :Emirates         Departure:19:00       Arrival:22:00")
  choice=int(input("Enter your choice:"))
  if choice==1:
   temp.flight="AirIndia"
   temp.deptime="09:00"
   temp.arrtime="12:00"
  elif choice==2:
   temp.flight="IndiGo"
   temp.deptime="14:00"
   temp.arrtime="17:00"
  elif choice==3:
   temp.flight="Emirates"
   temp.deptime="19:00"
   temp.arrtime="22:00"
  else:
   print("Please Enter Correct Choice")
   return
  temp.date=input("Enter Date of journey(dd/mm/yyyy):")
  temp.next=None
  print("***Ticket booked successfully***")
  print("PNR:",temp.pnr)
  print("Name:",temp.fname,temp.lname)
  print("Age:",temp.age)
  print("Gender:",temp.gend)
  print("Contact:",temp.contact)
  print("Email:",temp.email)
  print("Flight:",temp.flight)
  print("Departure:",temp.deptime)
  print("Arrival:",temp.arrtime)
  print("Date:",temp.date)
  return temp

 def insert(self):   #insert function to insert reservation
  temp=self.seatreser()
  if self.head==None:
   self.head=temp
  else:
   p=self.head
   while p.next!=None:
    p=p.next
   p.next=temp

 def checkticket(self,n):  #check ticket module
  if self.head==None:
   print("No reservations have been made yet")
  else:
   p=self.head
   while p!=None:
    if p.pnr==n:
     print("***Ticket Details Found***")
     print("PNR:",p.pnr)
     print("Name:",p.fname,p.lname)
     print("Age:",p.age)
     print("Gender:",p.gend)
     print("Contact:",p.contact)
     print("Email:",p.email)
     print("Flight:",p.flight)
     print("Departure:",p.deptime)
     print("Arrival:",p.arrtime)
     print("Date:",p.date)
     return
    p=p.next
   print("***No ticket found with given PNR number***")

 def cancelticket(self,n):  #ticket cancellation module
  if self.head==None:
   print("No reservations have been made yet")
  elif self.head.pnr==n:
   self.head=self.head.next
   print("***Ticket Cancelled Successfully***")
  else:
   p=self.head
   while p.next!=None:
    if p.next.pnr==n:
     p.next=p.next.next
     print("***Ticket Cancelled Successfully***")
     return
    p=p.next
   print("***No ticket found with given PNR number***")

 def travellersinfo(self):  #travellers info module
  if self.head==None:
   print("***No reservations have been made yet***")
  else:
   p=self.head
   i=1
   while p!=None:
    print("***Passenger",i,"Details***")
    print("PNR:",p.pnr)
    print("Name:",p.fname,p.lname)
    print("Age:",p.age)
    print("Gender:",p.gend)
    print("Contact:",p.contact)
    print("Email:",p.email)
    print("Flight:",p.flight)
    print("Departure:",p.deptime)
    print("Arrival:",p.arrtime)
    print("Date:",p.date)
    p=p.next
    i+=1

 def cargoservices(self):   #cargo services module
  self.cargo=input("Enter description of your cargo:")
  self.cargodes=input("Enter destination of your cargo:")
  self.cargocharges=int(input("Enter charges for your cargo:"))
  print("***Cargo details saved successfully***")

 def checkin(self):  #check-in module
  if self.head is None:
    print("***No reservation exists to check-in***")
  else:
    pnr=int(input("Enter your PNR number for check-in: "))
    temp=self.head
    while temp is not None:
        if temp.pnr==pnr:
            print("***Passenger Found, Check-in Successful!***")
            print("PNR:",temp.pnr)
            print("Name:",temp.fname,temp.lname)
            print("Flight:",temp.flight)
            print("Departure:",temp.deptime)
            print("Arrival:",temp.arrtime)
            print("Date:",temp.date)
            print("Checked-in successfully. Have a nice flight!")
            return
        temp=temp.next
    print("***No reservation found with given PNR number.***")

#initializing data for airport hotels
firstclass_rooms = [6, 7, 8, 9]
executive_rooms = [1, 2, 3, 4, 5]
economy_rooms = [10, 11, 12, 13, 14]

fir_occ = []
ex_occ = []
eco_occ = []

class hotel:
 def airporthotels(self):
  print("***Airport Hotels Available***")
  print("1.First class Rooms")
  print("2.Executive Rooms")
  print("3.Economy Rooms")
  ch=int(input("Enter your choice:"))
  if ch==1:
   print("Available First Class Rooms:")
   for i in firstclass_rooms:
    if i not in fir_occ:
     print(i,end=" ")
   r=int(input("\nEnter room number to book:"))
   if r in firstclass_rooms and r not in fir_occ:
    fir_occ.append(r)
    print("***First Class Room Booked Successfully***")
   else:
    print("***Invalid Room Number or Room Already Booked***")
  elif ch==2:
   print("Available Executive Rooms:")
   for i in executive_rooms:
    if i not in ex_occ:
     print(i,end=" ")
   r=int(input("\nEnter room number to book:"))
   if r in executive_rooms and r not in ex_occ:
    ex_occ.append(r)
    print("***Executive Room Booked Successfully***")
   else:
    print("***Invalid Room Number or Room Already Booked***")
  elif ch==3:
   print("Available Economy Rooms:")
   for i in economy_rooms:
    if i not in eco_occ:
     print(i,end=" ")
   r=int(input("\nEnter room number to book:"))
   if r in economy_rooms and r not in eco_occ:
    eco_occ.append(r)
    print("***Economy Room Booked Successfully***")
   else:
    print("***Invalid Room Number or Room Already Booked***")
  else:
   print("***Invalid Choice***")

def menu():
  print("                                  Welcome To IST Flight Reservation System                    ")
  print("                               **********************************************                 ")
  print("                               Book Your Flight Tickets at affordable prices!                 ")
  print("                               **********************************************                 ")
  print("                                             ******MENU******                                 ")
  print("                                            1.Seat Reservation                                ")
  print("                                            2.Checking Tickets                                ")
  print("                                            3.Ticket Cancellaton                              ")
  print("                                            4.Cargo Services                                  ")
  print("                                            5.Airport hotels                                  ")
  print("                                            6.Traveller's Information                         ")
  print("                                            7.Check-in                                        ")
  print("                                            8.Exit                                            ")
  c=int(input("Enter choice:"))
  return c

l=Seatreservation()
k=hotel()
while True:
 ch=menu()
 if ch==1:
  l.insert()
 elif ch==2:
  pos=int(input("Enter your PNR number:"))
  l.checkticket(pos)
 elif ch==3:
  n=int(input("Enter PNR number of ticket that you want to cancel:"))
  l.cancelticket(n)
 elif ch==6:
  l.travellersinfo()
 elif ch==4:
  l.cargoservices()
 elif ch==5:
  k.airporthotels()
 elif ch==7:
  l.checkin()
 elif ch==8:
  print("Exit")
  break
 else:
   print("--Please enter a valid choice--") 
  def calculate_total(price, quantity):
    discount = 0.1  # 🔴 declared but never used
    total = price * quantity
    return total
