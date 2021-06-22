#PRAGYA BHARTI RA1911030010063
from tkinter import *
from tkinter import messagebox 
from PIL import ImageTk,Image
from tkinter import ttk
import sqlite3
root = Tk()
Head_label = Label(root, text = "CAR RENTAL RECEIPT", font='Helvetica 18 bold').grid(row=0,column=2)
Date_label = Label(root, text = "Date:").grid(row=1,column=0)
en1=StringVar()
Date_entry = Entry(root,width=30,textvariable=en1)
Date_entry.grid(row=1,column=1)

Receipt_label = Label(root, text = "Receipt#:").grid(row=2,column=0)
en2=StringVar()
Receipt_entry = Entry(root,width=30,textvariable=en2)
Receipt_entry.grid(row=2,column=1)

RentalCompanyInfo_label = Label(root, text = "Rental Company Info",font='Helventica 15 bold').grid(row=3,column=0)

Company_label = Label(root, text = "Company:").grid(row=4,column=0)
en3=StringVar()
Company_entry = Entry(root,width=30,textvariable=en3)
Company_entry.grid(row=4,column=1)

Representative_label = Label(root, text = "Representative:").grid(row=5,column=0)
en4=StringVar()
Representative_entry = Entry(root,width=30,textvariable=en4)
Representative_entry.grid(row=5,column=1)

Location_label = Label(root, text = "Location:").grid(row=6,column=0)
en5=StringVar()
Location_entry = Entry(root,width=30,textvariable=en5)
Location_entry.grid(row=6,column=1)

City_label = Label(root, text = "City/State/ZIP:").grid(row=7,column=0)
en6=StringVar()
City_entry = Entry(root,width=30,textvariable=en6)
City_entry.grid(row=7,column=1)

Phone_label = Label(root, text = "Phone:").grid(row=8,column=0)
en7=StringVar()
Phone_entry = Entry(root,width=30,textvariable=en7)
Phone_entry.grid(row=8,column=1)

LeesseInfo_label = Label(root, text = "Leesse Info",font='Helventica 15 bold').grid(row=3,column=2)
Name_label = Label(root, text = "Name:").grid(row=4,column=2)
en8=StringVar()
Name_entry = Entry(root,width=30,textvariable=en8)
Name_entry.grid(row=4,column=3)

License_label = Label(root, text = "License #:").grid(row=5,column=2)
en9=StringVar()
License_entry = Entry(root,width=30,textvariable=en9)
License_entry.grid(row=5,column=3)

Address_label = Label(root, text = "Address:").grid(row=6,column=2)
en10=StringVar()
Address_entry = Entry(root,width=30,textvariable=en10)
Address_entry.grid(row=6,column=3)

CSZ_label = Label(root, text = "City/State/ZIP:").grid(row=7,column=2)
en11=StringVar()
CSZ_entry = Entry(root,width=30,textvariable=en11)
CSZ_entry.grid(row=7,column=3)

phone_label = Label(root, text = "Phone:").grid(row=8,column=2)
en12=StringVar()
phone_entry = Entry(root,width=30,textvariable=en12)
phone_entry.grid(row=8,column=3)

VehicleInfo_label = Label(root, text = "Vehicle Information",font='Helventica 15 bold').grid(row=9,column=0)
VIN_label = Label(root, text = "VIN:").grid(row=10,column=0)
en13=StringVar()
VIN_entry = Entry(root,width=30,textvariable=en13)
VIN_entry.grid(row=10,column=1)

Make_label = Label(root, text = "Make:").grid(row=11,column=0)
en14=StringVar()
Make_entry = Entry(root,width=30,textvariable=en14)
Make_entry.grid(row=11,column=1)

Year_label = Label(root, text = "Year:").grid(row=12,column=0)
en15=StringVar()
Year_entry = Entry(root,width=30,textvariable=en15)
Year_entry.grid(row=12,column=1)

Color_label = Label(root, text = "Color:").grid(row=13,column=0)
en16=StringVar()
Color_entry = Entry(root,width=30,textvariable=en16)
Color_entry.grid(row=13,column=1)

Rn_label = Label(root, text = "Registration #:").grid(row=10,column=2)
en17=StringVar()
Rn_entry = Entry(root,width=30,textvariable=en17)
Rn_entry.grid(row=10,column=3)

Model_label = Label(root, text = "Model:").grid(row=11,column=2)
en18=StringVar()
Model_entry = Entry(root,width=30,textvariable=en18)
Model_entry.grid(row=11,column=3)

Mileage_label = Label(root, text = "Mileage:").grid(row=12,column=2)
en19=StringVar()
Mileage_entry = Entry(root,width=30,textvariable=en19)
Mileage_entry.grid(row=12,column=3)

vin_label = Label(root, text="VIN", font='Helventica 15 bold').grid(row=14,column=0)
cost_label = Label(root, text="Cost/Day", font= 'Helventica 15 bold').grid(row=14,column=1)
nd_label = Label(root, text="# of Days",  font= 'Helventica 15 bold').grid(row=14,column=2)
AC = Label(root, text="Additional Costs",  font= 'Helventica 15 bold').grid(row=14,column=4)
Line = Label(root, text="Line Total",  font= 'Helventica 15 bold').grid(row=14,column=5)

en20=StringVar()
e1= Entry(root,width=10,textvariable=en20)
e1.grid(row=15,column=0)
en21=StringVar()
e2= Entry(root,width=10,textvariable=en21)
e2.grid(row=15,column=1)
en22=StringVar()
e3= Entry(root,width=10,textvariable=en22)
e3.grid(row=15,column=2)
en23=StringVar()
e4= Entry(root,width=10,textvariable=en23)
e4.grid(row=15,column=4)
en24=StringVar()
e5= Entry(root,width=10,textvariable=en24)
e5.grid(row=15,column=5)
en25=StringVar()
e6= Entry(root,width=10,textvariable=en25)
e6.grid(row=16,column=0)
en26=StringVar()
e7= Entry(root,width=10,textvariable=en26)
e7.grid(row=16,column=1)
en27=StringVar()
e8= Entry(root,width=10,textvariable=en27)
e8.grid(row=16,column=2)
en28=StringVar()
e9= Entry(root,width=10,textvariable=en28)
e9.grid(row=16,column=4)
en29=StringVar()
e10= Entry(root,width=10,textvariable=en29)
e10.grid(row=16,column=5)
en30=StringVar()
e11= Entry(root,width=10,textvariable=en30)
e11.grid(row=17,column=0)
en31=StringVar()
e12= Entry(root,width=10,textvariable=en31)
e12.grid(row=17,column=1)
en32=StringVar()
e13= Entry(root,width=10,textvariable=en32)
e13.grid(row=17,column=2)
en33=StringVar()
e14= Entry(root,width=10,textvariable=en33)
e14.grid(row=17,column=4)
en34=StringVar()
e15= Entry(root,width=10,textvariable=en34)
e15.grid(row=17,column=5)
PM_label= Label(root,text="Payment Method:",font= 'Helventica 15 bold').grid(row=18,column=0)
var=IntVar()
c1= Checkbutton(root,text="Cash",variable=var).grid(row=19,column=0)
var1=IntVar()
c2= Checkbutton(root,text="Check. No.:",variable=var1).grid(row=19,column=1)
var2=IntVar()

en35=StringVar()
e16= Entry(root,width=13,textvariable=en35)
e16.grid(row=19,column=2)

c3= Checkbutton(root,text="Credit. No.:",variable=var2).grid(row=20,column=0)

en36=StringVar()
e17= Entry(root,width=13,textvariable=en36)
e17.grid(row=20,column=1)

var3=IntVar()
c4= Checkbutton(root,text="Other:",variable=var3).grid(row=21,column=0)

en37=StringVar()
e18= Entry(root,width=13,textvariable=en37)
e18.grid(row=21,column=1)

St_label= Label(root,text="Subtotal:",font= 'Helventica 15 bold').grid(row=18,column=3)

en38=StringVar()
e19= Entry(root,width=10,textvariable=en38)
e19.grid(row=18,column=4)

en39=StringVar()
e20= Entry(root,width=10,textvariable=en39)
e20.grid(row=18,column=5)

Tax_label= Label(root,text="Tax(    %):",font= 'Helventica 15 bold').grid(row=19,column=3)

en40=StringVar()
e21= Entry(root,width=10,textvariable=en40)
e21.grid(row=19,column=4)

en41=StringVar()
e22= Entry(root,width=10,textvariable=en41)
e22.grid(row=19,column=5)

ap_label= Label(root,text="Amount Paid: ",font= 'Helventica 15 bold').grid(row=20,column=3)

en42=StringVar()
e23= Entry(root,width=10,textvariable=en42)
e23.grid(row=20,column=4)

en43=StringVar()
e24= Entry(root,width=10,textvariable=en43)
e24.grid(row=20,column=5)

as_label= Label(root,text="Authorized Signature:",font= 'Helventica 15 bold').grid(row=22,column=3)

en44=StringVar()
e25= Entry(root,width=20,textvariable=en44)
e25.grid(row=22,column=4)

rn_label=Label(root,text="Representative Name:").grid(row=23,column=3)

en45=StringVar()
e26= Entry(root,width=20,textvariable=en45)
e26.grid(row=23,column=4)
def hello():
    a = Date_entry.get()
    b = Receipt_entry.get()
    c = Company_entry.get()
    d = Representative_entry.get()
    e = Location_entry.get()
    f = City_entry.get()
    g = Phone_entry.get()
    h = Name_entry.get()
    i = License_entry.get()
    j = Address_entry.get()
    k = CSZ_entry.get()
    l = phone_entry.get()
    m = VIN_entry.get()
    n = Make_entry.get()
    o = Year_entry.get()
    p = Color_entry.get()
    q = Rn_entry.get()
    r = Model_entry.get()
    s = Mileage_entry.get()
    conn = sqlite3.connect('DATABASE1.db')
    
    with conn:
        cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS DETAILS(date TEXT,rec TEXT,com TEXT,rep TEXT,loc TEXT,city TEXT,ph TEXT,name TEXT,lic TEXT,address TEXT,csz TEXT,phone TEXT,vin TEXT,mak TEXT,yr TEXT,col TEXT,rn TEXT,mod TEXT,mil TEXT)')
    cursor.execute('INSERT INTO DETAILS (date,rec,com,rep,loc,city,ph,name,lic,address,csz,phone,vin,mak,yr,col,rn,mod,mil)VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,))
    conn.commit()
    messagebox.showinfo("Form Report", "Car rental form filled and submitted successfully")
    Date_entry.delete(0, END)
    Receipt_entry.delete(0, END)
    Company_entry.delete(0, END)
    Representative_entry.delete(0, END)
    Location_entry.delete(0, END)
    City_entry.delete(0, END)
    Phone_entry.delete(0, END)
    Name_entry.delete(0, END)
    License_entry.delete(0, END)
    Address_entry.delete(0, END)
    CSZ_entry.delete(0, END)
    phone_entry.delete(0, END)
    VIN_entry.delete(0, END)
    Make_entry.delete(0, END)
    Year_entry.delete(0, END)
    Color_entry.delete(0, END)
    Rn_entry.delete(0, END)
    Model_entry.delete(0, END)
    Mileage_entry.delete(0, END)
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    e9.delete(0, END)
    e10.delete(0, END)
    e11.delete(0, END)
    e12.delete(0, END)
    e13.delete(0, END)
    e14.delete(0, END)
    e15.delete(0, END)
    e16.delete(0, END)
    e17.delete(0, END)
    e18.delete(0, END)
    e19.delete(0, END)
    e20.delete(0, END)
    e21.delete(0, END)
    e22.delete(0, END)
    e23.delete(0, END)
    e24.delete(0, END)
    e25.delete(0, END)
    e26.delete(0, END)
btn = ttk.Button(root ,text="Submit",command = hello).grid(row=30,column=2)
root.mainloop()