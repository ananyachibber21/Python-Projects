import mysql.connector
print('*********WELCOME TO HAPPY HOUR RESORT*********')
print('1-Enter your details')
print('2-enter a room plan')
print('3-enter laundry charge')
print('4-club charges')
print('5-calculate total bill charges')
db=mysql.connector.connect(user="root",host="localhost",password="Ananya_2102",database="resort")
cursor=db.cursor()

def entdet():
    name=input("Enter your Name: ")
    num=int(input("Enter your Number: "))
    id=int(input("Your ID: "))
    num_mem=int(input("Enter the Number of Members: "))
    arrive = input("Enter the date of arrival: ")
    depart = input("Enter the date of arrival: ")
    query=("insert into resort(Name,Number,ID,Number_of_Members,Date_of_Arrival,Date_of_Departure) values(%s,%s,%s,%s,%s,%s)")
    data=(name,num,id,num_mem,arrive,depart)
    cursor.execute(query,data)
    db.commit()

def room_plan():
    s4=0
    print('AP[room including all meals]')
    print('CP[room including only breakfast]')
    print('MAP[room including one meal and breakfast]')
    print('EP[no meals included]')
    g=input('Enter the Room Plan of your choice : ')
    if g=='AP':
        q=5000
    elif g=='CP':
        q=3500
    elif g=='MAP':
        q=4000
    elif g=='EP':
        s4=meal()
    m=q+s4  
    query=("insert into resort(Room_Type) values(%s)")
    data=([g])
    cursor.execute(query,data)
    db.commit()
    return(m)

def meal():
    print('breakfast=1000/-')
    print('lunch=1200/-')
    print('dinner=1500/-')
    print('none=0/-')
    h=input('Choose the type of Meal:')
    if h=="breakfast":
        c=1000
    elif h=="lunch":
        c=1200
    elif h=='dinner':
        c=1500
    elif h=='none':
        c=0       
    return(c)
         
def laundry_charge():
    x=input('Enter y or n: ')
    if x=='y':
        print('200/- per cloth')
        v=int(input("enter no of clothes "))
        j=200*v
    elif x=='n':
        j=0
    query=("insert into resort(Laundry) values(%s)")
    data=([x])
    cursor.execute(query,data)
    db.commit() 
    return(j)    
                 
def club():
    print('1.billiards, 2.swimming pool, 3.spa , 4.gym, 5.steam bath' , end="")
    i=int(input('Enter your choice: '))
    if(i==1):
        r=600
    elif(i==2):
        r=400
    elif(i==3):
        r=800
    elif(i==4):
        r=400
    elif (i==5):
        r=1000
    query=("insert into resort(Club) values(%s)")
    data=([i])
    cursor.execute(query,data)
    db.commit() 
    return(r) 

while True:
    n=int(input("Enter choice:-"))
    if n==1:
        entdet()
        print("success")
    elif n==2:
        s1 = room_plan()
        print("success")
    elif n==3:
        s2 = laundry_charge()
        print("success")
    elif n==4:
        s3 = club()
        print("success")
    elif n==5:
        print('total charge is',s1,'+',s2,'+',s3)
        s=s1+s2+s3
        print(s)
        print("Please Pay!")
        break
    


