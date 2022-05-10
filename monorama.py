from appointment1 import*
from patient import*
from patientcount import*
from bill import*
from employee import*
from database import*
import tkinter
from tkinter import*
import sqlite3
from sqlite3 import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import font
from room import Room
from search import*
from PIL import ImageTk,Image
from medicalaccess import*


conn=sqlite3.connect("HospitalDB.db")
class Hospital:
    def Main(self):
        try:
            self.t.destroy()
            self.t=Tk()
        except:
            try:
                self.t=Tk()
            except:
                pass
           
        self.t.title("Monorama Hospital")
        self.t.geometry("1500x1500")
        self.t.iconbitmap("download.ico")
        
        self.f=Frame(self.t,height=90,width=1500)
        self.f.logo=PhotoImage(file="mann.png")
        self.l=Label(self.f,image=self.f.logo)
        self.l.place(x=0,y=0)
        self.f.pack(fill=BOTH,expand=1)
        self.f1=Frame(self.t,height=200,width=1366)
        self.c=Canvas(self.f1,height=618,width=1566)
        self.c.pack()
        self.f1.logo=PhotoImage(file="man4.png")
        self.l1=Label(self.f1,image=self.f1.logo)
        self.l1.place(x=0,y=0)
        self.f1.pack(fill=BOTH,expand=1)
        self.b1=Button(self.f1,text="Contact Us",width=20,bg="light grey",fg="black",font="elephant 10",command=lambda:self.Contact())
        self.b1.place(x=1100,y=50)
        self.b1=Button(self.f1,text="Facilities",width=20,bg="light grey",fg="black",font="elephant 10",command=lambda:self.Facility())
        self.b1.place(x=800,y=50)

       
        self.b=Button(self.f1,text="Welcome to Monorama ",bg="light grey",fg="black",font="elephant 20",width=20,command=lambda:self.login())
        self.b.place(x=950,y=480)
        self.t.mainloop()
        '''self.b1=Button(self.f1,text="Doctor Profile",bg="light grey",fg="black",font="elephant 10",command="")
        self.b1.place(x=50,y=20)
        self.b2=Button(self.f1,text="Appointment Scheduling",bg="light grey",fg="black",font="elephant 10",command="")
        self.b2.place(x=200,y=20)
        self.b3=Button(self.f1,text="Access To Medical Records",bg="light grey",fg="black",font="elephant 10",command="")
        self.b3.place(x=450,y=20)
        self.b4=Button(self.f1,text="Prescription Tracking",bg="light grey",fg="black",font="elephant 10",command="")
        self.b4.place(x=700,y=20)
        self.b5=Button(self.f1,text="Patient Community",bg="light grey",fg="black",font="elephant 10",command="")
        self.b5.place(x=940,y=20)
        self.b6=Button(self.f1,text="Admin Register",bg="light grey",fg="black",font="elephant 10",command=lambda:self.Register())
        self.b6.place(x=1150,y=20)
        self.b7=Button(self.f1,text="Patient Register",bg="light grey",fg="black",font="elephant 10",command=lambda:self.pRegister())
        self.b7.place(x=1370,y=20)'''
        
        '''self.b=Button(self.f1,text="Welcome to Manorama ",bg="light grey",fg="black",font="elephant 20",width=20,command=lambda:self.login())
        self.b.place(x=950,y=480)
        self.t.mainloop()'''
    def AdminMain(self):
        self.t.destroy()
        self.t=Tk()
        self.t.title("Monorama Hospital")
        self.t.geometry("1500x1500")
        self.t.iconbitmap("download.ico")
        
        self.f=Frame(self.t,height=90,width=1350)
        self.f.logo=PhotoImage(file="mann.png")
        self.l=Label(self.f,image=self.f.logo)
        self.l.place(x=0,y=0)
        self.f.pack(fill=BOTH,expand=1)
        self.f1=Frame(self.t,height=200,width=1366)
        self.c=Canvas(self.f1,height=618,width=1566)
        self.c.pack()
        self.f1.logo=PhotoImage(file="man4.png")
        self.l1=Label(self.f1,image=self.f1.logo)
        self.l1.place(x=0,y=0)
        self.f1.pack(fill=BOTH,expand=1)
        self.b1=Button(self.f1,text="Doctor Profile",bg="light grey",fg="black",font="elephant 10",command=lambda:self.Doctor())
        self.b1.place(x=50,y=20)
        self.b2=Button(self.f1,text="Appointment Scheduling",bg="light grey",fg="black",font="elephant 10",command=lambda:self.Appointment_Form())

        self.b2.place(x=200,y=20)
        self.b3=Button(self.f1,text="Access To Medical Records",bg="light grey",fg="black",font="elephant 10",command=lambda:self.Medicalaccess())
        self.b3.place(x=450,y=20)
        self.b4=Button(self.f1,text="View Appointment",bg="light grey",fg="black",font="elephant 10",command=lambda:self.doctorsearch())
        self.b4.place(x=700,y=20)
        self.b5=Button(self.f1,text="Patient Community",bg="light grey",fg="black",font="elephant 10",command=lambda:self.PatientCount())
        self.b5.place(x=940,y=20)
        self.b6=Button(self.f1,text="Doctor Register ",bg="light grey",fg="black",font="elephant 10",command=lambda:self.DoctorRegister())
        self.b6.place(x=1150,y=20)
        self.b7=Button(self.f1,text="Patient Register",bg="light grey",fg="black",font="elephant 10",command=lambda:self.Patient_Reg())
        self.b7.place(x=1350,y=20)
        self.b8=Button(self.f1,text="Room Allocation",bg="light grey",fg="black",font="elephant 10",command=lambda:self.Room_Allocation())
        self.b8.place(x=50,y=60)
        self.b9=Button(self.f1,text="Employee Register",bg="light grey",fg="black",font="elephant 10",command=lambda:self.Employee_Reg())
        self.b9.place(x=220,y=60)
        self.b10=Button(self.f1,text="Billing",bg="light grey",fg="black",font="elephant 10",command=lambda:self.Billing_Form())
        self.b10.place(x=500,y=60)
        self.b11=Button(self.f1,text="OT Records",bg="light grey",fg="black",font="elephant 10",command=lambda:self.OT())
        self.b11.place(x=700,y=60)
        
        
        self.b=Button(self.f1,text="Welcome to Manorama ",bg="light grey",fg="black",font="elephant 20",width=20,command=lambda:self.login())
        self.b.place(x=950,y=480)
        self.t.mainloop()

    


    def DoctorMain(self):
        self.t.destroy()
        self.t=Tk()
        self.t.title("Monorama Hospital")
        self.t.geometry("1500x1500")
        self.t.iconbitmap("download.ico")
        
        self.f=Frame(self.t,height=90,width=1350)
        self.f.logo=PhotoImage(file="mann.png")
        self.l=Label(self.f,image=self.f.logo)
        self.l.place(x=0,y=0)
        self.f.pack(fill=BOTH,expand=1)
        self.f1=Frame(self.t,height=200,width=1366)
        self.c=Canvas(self.f1,height=618,width=1566)
        self.c.pack()
        self.f1.logo=PhotoImage(file="man4.png")
        self.l1=Label(self.f1,image=self.f1.logo)
        self.l1.place(x=0,y=0)
        self.f1.pack(fill=BOTH,expand=1)
        self.b1=Button(self.f1,text="Doctor Profile",bg="light grey",fg="black",font="elephant 10",command=lambda:self.Doctor())
        self.b1.place(x=100,y=20)
        #self.b2=Button(self.f1,text="Appointment Scheduling",bg="light grey",fg="black",font="elephant 10",command=lambda:self.Appointment_Form())

        #self.b2.place(x=200,y=20)
        self.b3=Button(self.f1,text="Access To Medical Records",bg="light grey",fg="black",font="elephant 10",command=lambda:self.Medicalaccess())
        self.b3.place(x=350,y=20)
        self.b4=Button(self.f1,text="View Appointment",bg="light grey",fg="black",font="elephant 10",command=lambda:self.doctorsearch())
        self.b4.place(x=700,y=20)
        #self.b5=Button(self.f1,text="Patient Community",bg="light grey",fg="black",font="elephant 10",command=lambda:self.PatientCount())
        #self.b5.place(x=940,y=20)
        self.b6=Button(self.f1,text="Doctor Register ",bg="light grey",fg="black",font="elephant 10",command=lambda:self.DoctorRegister())
        self.b6.place(x=1000,y=20)
        #self.b7=Button(self.f1,text="Patient Register",bg="light grey",fg="black",font="elephant 10",command=lambda:self.Patient_Reg())
        #self.b7.place(x=1350,y=20)
        #self.b8=Button(self.f1,text="Room Allocation",bg="light grey",fg="black",font="elephant 10",command=lambda:self.Room_Allocation())
        #self.b8.place(x=50,y=60)
        #self.b9=Button(self.f1,text="Employee Register",bg="light grey",fg="black",font="elephant 10",command=lambda:self.Employee_Reg())
        #self.b9.place(x=220,y=60)
        #self.b10=Button(self.f1,text="Billing",bg="light grey",fg="black",font="elephant 10",command=lambda:self.Billing_Form())
        #self.b10.place(x=500,y=60)
        #self.b11=Button(self.f1,text="OT Records",bg="light grey",fg="black",font="elephant 10",command=lambda:self.OT())
        #self.b11.place(x=700,y=60)
        
        
        self.b=Button(self.f1,text="Welcome to Monorama ",bg="light grey",fg="black",font="elephant 20",width=20,command=lambda:self.login())
        self.b.place(x=950,y=480)
        self.t.mainloop()











            

    def Contact(self):

        self.t.destroy()
        self.t=Tk()
        self.t.title("Contact Us")
        self.t.geometry("1366x768")
        self.t.iconbitmap("download.ico")
        self.loginf1=Frame(self.t,height=150,width=1366)
        self.logo=PhotoImage(file="mann.png")
        self.ba=Label(self.loginf1,image=self.logo,height=150).place(x=0,y=0)
        self.loginf1.pack(fill=BOTH,expand=1)
        self.loginf2=Frame(self.t,height=618,width=1366)
        self.c=Canvas(self.loginf2,height=618,width=1366)
        self.c.pack()
        self.logo1=PhotoImage(file="manor.png")
        self.c.create_image(683,309,image=self.logo1)
        self.loginf2.pack(fill=BOTH,expand=1)

 
        self.lblpid = Label(self.t,text="Contact Us",font="Helvetica 14 bold",bd=22)
        self.lblpid.place(x=350,y=200)
        
        self.lblpid = Label(self.t,text="Enter Your Name",font="Helvetica 14 bold",bd=22)
        self.lblpid.place(x=100,y=300)
        self.lblpid  = Entry(self.t,font="Helvetica 14 bold",bd=2,textvariable="")
        self.lblpid.place(x=320,y=320)
        
        self.lbldid = Label(self.t,text="Enter Your Mobile No.",font="Helvetica 14 bold",bd=22)
        self.lbldid.place(x=100,y=400)
        self.lbldid  = Entry(self.t,font="Helvetica 14 bold",bd=2,textvariable="")
        self.lbldid.place(x=320,y=420)

    
        self.b1=Button(self.t,text="Submit",bg="light grey",fg="black",font="elephant 10",command=lambda:self.Contactsave())
        self.b1.place(x=400,y=500)
        
        

    def Facility(self):


        self.t.destroy()
        self.t=Tk()
        self.t.title("Shusisha's Pizza")
        self.t.geometry("1366x768")
        #self.t.resizable(False, False)
        
        self.menuf1=Frame(self.t,height=150,width=1366)
        self.c=Canvas(self.menuf1,height=150,width=1366)
        self.c.pack()
        self.logo=PhotoImage(file="flogo.PNG")
        self.c.create_image(683,75,image=self.logo)
        
        '''
        self.f=Frame(self.t,height=90,width=1350)
        self.f.logo=PhotoImage(file="mann.png")
        self.l=Label(self.f,image=self.f.logo)
        self.l.place(x=0,y=0)
        self.f.pack(fill=BOTH,expand=1)
        '''
        
        self.menuf1.pack(fill=BOTH,expand=1)

        self.menuf2=Frame(self.t,height=200,width=1366)
        self.c=Canvas(self.menuf2,height=618,width=1566)
        self.c.pack()
  
        #self.localtime=time.asctime(time.localtime(time.time()))
        #self.c.create_text(10,50,text=self.localtime,fill="red",font=("default",16))
       




        
        self.logo1=PhotoImage(file="manor.png")
        self.c.create_image(683,309,image=self.logo1)
        self.c.create_rectangle(50, 0, 1316, 840,fill="#d3ede6",outline="white",width=6)

        self.lab=Label(self.menuf2,text="FACILITIES",bg="yellow",font=("Cooper Black",22))
        self.lab.place(x=600,y=4)
        self.icul=PhotoImage(file="icu.png")
        self.c.create_image(230,180,image=self.icul)
        self.icu=Label(self.menuf2,text="ICU",cursor="hand2",fg="white",bg="#0b1335",bd=5,font=("default",18,'bold'))
        self.icu.place(x=170,y=280)
        self.mod=PhotoImage(file="modularot.png")
        self.c.create_image(530,180,image=self.mod)
        self.modl=Label(self.menuf2,text="MODULAR OT",cursor="hand2",fg="white",bg="#0b1335",bd=5,font=("default",18,'bold'))
        self.modl.place(x=440,y=280)
        self.ct=PhotoImage(file="CT.png")
        self.c.create_image(830,180,image=self.ct)
        self.ctl=Label(self.menuf2,text="CT",cursor="hand2",fg="white",bg="#0b1335",bd=5,font=("default",18,'bold'))
        self.ctl.place(x=730,y=280)
        self.pat=PhotoImage(file="Pathology.png")
        self.c.create_image(1130,180,image=self.pat)
        self.patl=Label(self.menuf2,text="PATHOLOGY",cursor="hand2",fg="white",bg="#0b1335",bd=5,font=("default",18,'bold'))
        self.patl.place(x=1000,y=280)


        #self.c.create_rectangle(50, 280, 1316, 660,fill="#d3ede6",outline="black",width=6)

        self.amb=PhotoImage(file="ambulance.png")
        self.c.create_image(230,450,image=self.amb)
        self.ambl=Label(self.menuf2,text="AMBULANCE",cursor="hand2",fg="white",bg="#0b1335",bd=5,font=("default",18,'bold'))
        self.ambl.place(x=170,y=550)
        self.nicu=PhotoImage(file="nicu.png")
        self.c.create_image(530,450,image=self.nicu)
        self.nicul=Label(self.menuf2,text="N.I.C.U",cursor="hand2",fg="white",bg="#0b1335",bd=5,font=("default",18,'bold'))
        self.nicul.place(x=440,y=550)
        self.gyn=PhotoImage(file="gyano.png")
        self.c.create_image(830,450,image=self.gyn)
        self.gyanol=Label(self.menuf2,text="GYANO",cursor="hand2",fg="white",bg="#0b1335",bd=5,font=("default",18,'bold'))
        self.gyanol.place(x=730,y=550)
        self.ortho=PhotoImage(file="ortho.png")
        self.c.create_image(1130,450,image=self.ortho)
        self.orthol=Label(self.menuf2,text="ORTHO",cursor="hand2",fg="white",bg="#0b1335",bd=5,font=("default",18,'bold'))
        self.orthol.place(x=1010,y=550)


        
        self.menuf2.pack(fill=BOTH,expand=1)
        self.t.mainloop()



    



        
                
        

    def Doctor(self):
        self.t.destroy()
        self.t=Tk()
        self.t.title("Doctor Profile")
        self.t.geometry("1500x1500")
        self.t.iconbitmap("download.ico")
        self.f=Frame(self.t,height=90,width=1350)
        self.f.logo=PhotoImage(file="mann.png")
        self.l=Label(self.f,image=self.f.logo)
        self.l.place(x=0,y=0)
        self.f.pack(fill=BOTH,expand=1)
        self.f1=Frame(self.t,height=200,width=1366)
        self.c=Canvas(self.f1,height=618,width=1566)
        self.c.pack()
        
        self.f1.logo=PhotoImage(file="man4.png")
        self.l1=Label(self.f1,image=self.f1.logo)
        self.l1.place(x=0,y=0)
        self.f1.pack(fill=BOTH,expand=1)
        self.b1=Button(self.f1,text="Dr.V.K Porwal",bg="light grey",fg="black",font="elephant 10",command=lambda:self.VK())
        self.b1.place(x=50,y=20)
        self.b2=Button(self.f1,text="Dr.Devendra Ghanekar",bg="light grey",fg="black",font="elephant 10",command=lambda:self.Devendra())
        self.b2.place(x=200,y=20)
        self.b3=Button(self.f1,text="Dr.Neha Agrawal",bg="light grey",fg="black",font="elephant 10",command=lambda:self.Neha())
        self.b3.place(x=450,y=20)
        self.b4=Button(self.f1,text="Dr.Rahul Jain",bg="light grey",fg="black",font="elephant 10",command=lambda:self.Rahul())
        self.b4.place(x=700,y=20)
        self.b5=Button(self.f1,text="Dr.Rashmi Shad",bg="light grey",fg="black",font="elephant 10",command=lambda:self.Rashmi())
        self.b5.place(x=940,y=20)
        self.b6=Button(self.f1,text="Dr.Sameer Nivsarkar",bg="light grey",fg="black",font="elephant 10",command=lambda:self.Sameer())
        self.b6.place(x=1150,y=20)
        self.b7=Button(self.f1,text="Dr. Madhu Goyal",bg="light grey",fg="black",font="elephant 10",command=lambda:self.Madhu())
        self.b7.place(x=1370,y=20)
        self.b=Button(self.f1,text= "Home",command=lambda:self.Main(),cursor="hand2", bd=10,font=("cooper black",30, 'bold'),fg="white",bg="#0b1335")
        self.b.place(x=580,y=250)
        self.t.mainloop()


    def VK(self):
        self.t.destroy()
        self.t=Tk()
        self.t.title("V.K Profile")
        self.t.geometry("1500x1500")
        self.t.iconbitmap("download.ico")
        #self.t.resizable(False, False)
        self.f=Frame(self.t,height=150,width=1000)
        self.f.logo=PhotoImage(file="logo.png")
        self.l=Label(self.f,image=self.f.logo)
        self.l.place(x=0,y=0)
        self.f.pack(fill=BOTH,expand=1)
        self.pizf2=Frame(self.t,height=618,width=1566)
        self.c=Canvas(self.pizf2,height=695,width=1566)
        self.c.pack()
        self.logo1=PhotoImage(file="db.png")
        self.c.create_image(683,309,image=self.logo1)
        self.c.create_rectangle(400,120,966,470,fill="#d3ede6",outline="white",width=2)
        self.deli=PhotoImage(file="vk.png")
        self.c.create_image(540,260,image=self.deli)
        self.l1=Label(text="Did :1 \nName:-VK Porwal\nEducation:-MBBS, MD (Peds)\n Experince:-10yrs\n Specialization:-PediatricInten \nTime:8Am-12Am",font=("Elephant"))
        self.l1.place(x=660,y=360)
        
        #self.pic=PhotoImage(file="vk.png")
        #self.c.create_image(825,260,image=self.pic)
        self.de=Button(self.pizf2,text="Schedule your Appoinment",cursor="hand2",fg="white",command=lambda:self.AdminMain(),bg="#0b1335",font=("default",20),bd=5)
        self.de.place(x=510,y=400)
       
        #self.c.create_rectangle(405,125,678,465,outline="black",width=2)
        #self.c.create_rectangle(688,125,960,465,outline="black",width=2)
        self.pizf2.pack(fill=BOTH,expand=1)
        self.t.mainloop()

        
    def Devendra(self):
        self.t.destroy()
        self.t=Tk()
        self.t.title("Devendra Profile")
        self.t.geometry("1500x1500")
        self.t.iconbitmap("download.ico")
        #self.t.resizable(False, False)
        self.f=Frame(self.t,height=150,width=1000)
        self.f.logo=PhotoImage(file="logo.png")
        self.l=Label(self.f,image=self.f.logo)
        self.l.place(x=0,y=0)
        self.f.pack(fill=BOTH,expand=1)
        self.pizf2=Frame(self.t,height=618,width=1566)
        self.c=Canvas(self.pizf2,height=695,width=1566)
        self.c.pack()
        self.logo1=PhotoImage(file="db.png")
        self.c.create_image(683,309,image=self.logo1)
        self.c.create_rectangle(400,120,966,470,fill="#d3ede6",outline="white",width=2)
        self.deli=PhotoImage(file="devendra.png")
        self.c.create_image(540,260,image=self.deli)
        self.l1=Label(text="Did :2 \nName:-Dr. Devendra Ghanekar \nEducation:-MBBS\n Experince:-5 yrs\n Specialization:-DA Consultant \nTime:1PM-3PM",font=("Elephant"))
        self.l1.place(x=665,y=360)
        
        #self.pic=PhotoImage(file="vk.png")
        #self.c.create_image(825,260,image=self.pic)
        self.de=Button(self.pizf2,text="Schedule your Appoinment",cursor="hand2",fg="white",command=lambda:self.Doctor(),bg="#0b1335",font=("default",20),bd=5)
        self.de.place(x=420,y=400)
       
        #self.c.create_rectangle(405,125,678,465,outline="black",width=2)
        #self.c.create_rectangle(688,125,960,465,outline="black",width=2)
        self.pizf2.pack(fill=BOTH,expand=1)
        self.t.mainloop()

        
    def Neha(self):
        self.t.destroy()
        self.t=Tk()
        self.t.title("Neha Profile")
        self.t.geometry("1500x1500")
        self.t.iconbitmap("download.ico")
        #self.t.resizable(False, False)
        self.f=Frame(self.t,height=150,width=1000)
        self.f.logo=PhotoImage(file="logo.png")
        self.l=Label(self.f,image=self.f.logo)
        self.l.place(x=0,y=0)
        self.f.pack(fill=BOTH,expand=1)
        self.pizf2=Frame(self.t,height=618,width=1566)
        self.c=Canvas(self.pizf2,height=695,width=1566)
        self.c.pack()
        self.logo1=PhotoImage(file="db.png")
        self.c.create_image(683,309,image=self.logo1)
        self.c.create_rectangle(400,120,966,470,fill="#d3ede6",outline="white",width=2)
        self.deli=PhotoImage(file="neha.png")
        self.c.create_image(540,260,image=self.deli)
        self.l1=Label(text="Did :3 \nName:-Dr.Neha Agrawal \nEducation:-MBBS,MD \n Experince:-7 yrs\n Specialization:- DM Consultant\nTime:2PM-4PM",font=("Elephant"))
        self.l1.place(x=665,y=360)
        
        #self.pic=PhotoImage(file="vk.png")
        #self.c.create_image(825,260,image=self.pic)
        self.de=Button(self.pizf2,text="Schedule your Appoinment",cursor="hand2",fg="white",command=lambda:self.Doctor(),bg="#0b1335",font=("default",20),bd=5)
        self.de.place(x=510,y=400)
       
        #self.c.create_rectangle(405,125,678,465,outline="black",width=2)
        #self.c.create_rectangle(688,125,960,465,outline="black",width=2)
        self.pizf2.pack(fill=BOTH,expand=1)
        self.t.mainloop()

    def Rahul(self):
        self.t.destroy()
        self.t=Tk()
        self.t.title("Rahul Profile")
        self.t.geometry("1500x1500")
        self.t.iconbitmap("download.ico")
        #self.t.resizable(False, False)
        self.f=Frame(self.t,height=150,width=1000)
        self.f.logo=PhotoImage(file="logo.png")
        self.l=Label(self.f,image=self.f.logo)
        self.l.place(x=0,y=0)
        self.f.pack(fill=BOTH,expand=1)
        self.pizf2=Frame(self.t,height=618,width=1566)
        self.c=Canvas(self.pizf2,height=695,width=1566)
        self.c.pack()
        self.logo1=PhotoImage(file="db.png")
        self.c.create_image(683,309,image=self.logo1)
        self.c.create_rectangle(400,120,966,470,fill="#d3ede6",outline="white",width=2)
        self.deli=PhotoImage(file="rahul.png")
        self.c.create_image(540,260,image=self.deli)
        self.l1=Label(text="Did:4 \n Name:-Dr.Rahul Jain \nEducation:-MBBS,MD \n Experince:-6 yrs\n Specialization:- Pathologist Consultant \nTime:9AM-11AM",font=("Elephant"))
        self.l1.place(x=665,y=360)
        
        #self.pic=PhotoImage(file="vk.png")
        #self.c.create_image(825,260,image=self.pic)
        self.de=Button(self.pizf2,text="Schedule your Appoinment",cursor="hand2",fg="white",command=lambda:self.Doctor(),bg="#0b1335",font=("default",20),bd=5)
        self.de.place(x=420,y=400)
       
        #self.c.create_rectangle(405,125,678,465,outline="black",width=2)
        #self.c.create_rectangle(688,125,960,465,outline="black",width=2)
        self.pizf2.pack(fill=BOTH,expand=1)
        self.t.mainloop()

    def Rashmi(self):
        self.t.destroy()
        self.t=Tk()
        self.t.title("Rashmi Profile")
        self.t.geometry("1500x1500")
        self.t.iconbitmap("download.ico")
        #self.t.resizable(False, False)
        self.f=Frame(self.t,height=150,width=1000)
        self.f.logo=PhotoImage(file="logo.png")
        self.l=Label(self.f,image=self.f.logo)
        self.l.place(x=0,y=0)
        self.f.pack(fill=BOTH,expand=1)
        self.pizf2=Frame(self.t,height=618,width=1566)
        self.c=Canvas(self.pizf2,height=695,width=1566)
        self.c.pack()
        self.logo1=PhotoImage(file="db.png")
        self.c.create_image(683,309,image=self.logo1)
        self.c.create_rectangle(400,120,966,470,fill="#d3ede6",outline="white",width=2)
        self.deli=PhotoImage(file="rashmi.png")
        self.c.create_image(540,260,image=self.deli)
        self.l1=Label(text="Did :5 \nName:-Dr.Rashmi Shad \nEducation:-MBBS \n Experince:-4 yrs\n Specialization:- DNB Consultant \nTime:4PM-6PM",font=("Elephant"))
        self.l1.place(x=665,y=360)
        
        #self.pic=PhotoImage(file="vk.png")
        #self.c.create_image(825,260,image=self.pic)
        self.de=Button(self.pizf2,text="Schedule your Appoinment",cursor="hand2",fg="white",command=lambda:self.Doctor(),bg="#0b1335",font=("default",20),bd=5)
        self.de.place(x=420,y=400)
       
        #self.c.create_rectangle(405,125,678,465,outline="black",width=2)
        #self.c.create_rectangle(688,125,960,465,outline="black",width=2)
        self.pizf2.pack(fill=BOTH,expand=1)
        self.t.mainloop()

    
    def Sameer(self):
        self.t.destroy()
        self.t=Tk()
        self.t.title("Sameer Profile")
        self.t.geometry("1500x1500")
        self.t.iconbitmap("download.ico")
        #self.t.resizable(False, False)
        self.f=Frame(self.t,height=150,width=1000)
        self.f.logo=PhotoImage(file="logo.png")
        self.l=Label(self.f,image=self.f.logo)
        self.l.place(x=0,y=0)
        self.f.pack(fill=BOTH,expand=1)
        self.pizf2=Frame(self.t,height=618,width=1566)
        self.c=Canvas(self.pizf2,height=695,width=1566)
        self.c.pack()
        self.logo1=PhotoImage(file="db.png")
        self.c.create_image(683,309,image=self.logo1)
        self.c.create_rectangle(400,120,966,470,fill="#d3ede6",outline="white",width=2)
        self.deli=PhotoImage(file="sameer.png")
        self.c.create_image(540,260,image=self.deli)
        self.l1=Label(text="Did :6\nName:-Dr.Sameer Nivsarkar\nEducation:-MBBS \n Experince:-3 yrs\n Specialization:-Consultant E.N.T \nTime:3PM-6PM",font=("Elephant"))
        self.l1.place(x=665,y=360)
        
        #self.pic=PhotoImage(file="vk.png")
        #self.c.create_image(825,260,image=self.pic)
        self.de=Button(self.pizf2,text="Schedule your Appoinment",cursor="hand2",fg="white",command=lambda:self.Doctor(),bg="#0b1335",font=("default",20),bd=5)
        self.de.place(x=510,y=400)
       
        #self.c.create_rectangle(405,125,678,465,outline="black",width=2)
        #self.c.create_rectangle(688,125,960,465,outline="black",width=2)
        self.pizf2.pack(fill=BOTH,expand=1)
        self.t.mainloop()

       
    def Madhu(self):
        self.t.destroy()
        self.t=Tk()
        self.t.title("Madhu Profile")
        self.t.geometry("1500x1500")
        self.t.iconbitmap("download.ico")
        #self.t.resizable(False, False)
        self.f=Frame(self.t,height=150,width=1000)
        self.f.logo=PhotoImage(file="logo.png")
        self.l=Label(self.f,image=self.f.logo)
        self.l.place(x=0,y=0)
        self.f.pack(fill=BOTH,expand=1)
        self.pizf2=Frame(self.t,height=618,width=1566)
        self.c=Canvas(self.pizf2,height=695,width=1566)
        self.c.pack()
        self.logo1=PhotoImage(file="db.png")
        self.c.create_image(683,309,image=self.logo1)
        self.c.create_rectangle(400,120,966,470,fill="#d3ede6",outline="white",width=2)
        self.deli=PhotoImage(file="madhu.png")
        self.c.create_image(540,260,image=self.deli)
        self.l1=Label(text="Did : 7\nName:-Dr.Madhu Goyal\nEducation:-MBBS,MD \n Experince:-8 yrs\n Specialization:-Consultant Pediatrics \nTime:6PM-8PM",font=("Elephant"))
        self.l1.place(x=665,y=360)
        
        #self.pic=PhotoImage(file="vk.png")
        #self.c.create_image(825,260,image=self.pic)
        self.de=Button(self.pizf2,text="Schedule your Appoinment",cursor="hand2",fg="white",command=lambda:self.Doctor(),bg="#0b1335",font=("default",20),bd=5)
        self.de.place(x=420,y=400)
       
        #self.c.create_rectangle(405,125,678,465,outline="black",width=2)
        #self.c.create_rectangle(688,125,960,465,outline="black",width=2)
        self.pizf2.pack(fill=BOTH,expand=1)
        self.t.mainloop()
 
 
    def login(self):
        self.t.destroy()
        self.t=Tk()
        self.t.title("Admin login")
        self.t.geometry("1366x768")
        self.t.iconbitmap("download.ico")
        self.loginf1=Frame(self.t,height=150,width=1366)
        self.logo=PhotoImage(file="mann.png")
        self.ba=Label(self.loginf1,image=self.logo,height=150).place(x=0,y=0)
        self.loginf1.pack(fill=BOTH,expand=1)
        self.loginf2=Frame(self.t,height=618,width=1366)
        self.c=Canvas(self.loginf2,height=618,width=1366)
        self.c.pack()
        self.logo1=PhotoImage(file="login.png")
        self.c.create_image(683,309,image=self.logo1)
        self.loginf2.pack(fill=BOTH,expand=1)
        self.b=Button(self.loginf2,text="HOME",command=lambda:self.Main())
        self.b.place(x=1100,y=140)
        self.b1=Button(self.loginf2,text="REGISTER YOURSELF",command=lambda:self.Register(),width=15)
        self.b1.place(x=1170,y=140)
        self.l=Label(self.loginf2,text="Admin Signin",font=("Elephant 30"))
        self.l.place(x=120,y=50)
        self.l1=Label(self.loginf2,text="User Name",font=("Elephant "))
        self.l1.place(x=100,y=130)
        self.e=Entry(self.loginf2)
        self.e.place(x=220,y=130)
        self.l2=Label(self.loginf2,text="Password",font=("Elephant "))
        self.l2.place(x=100,y=170)
        self.e1=Entry(self.loginf2,show="*")
        self.e1.place(x=220,y=170)
        self.l1=Label(self.loginf2,text="Doctor ID",font=("Elephant "))
        self.l1.place(x=100,y=200)
        self.e2=Entry(self.loginf2)
        self.e2.place(x=220,y=200)
        self.b3=Button(self.loginf2,text="AdminLogin",command=lambda:self.adminlog(),font=("Elephant"),width=10)
        self.b3.place(x=200,y=260)
        self.b3=Button(self.loginf2,text="DoctorLogin",command=lambda:self.doclog(),font=("Elephant"),width=10)
        self.b3.place(x=350,y=260)
        self.t.mainloop()        

    def logres(self):
        self.loguser=self.e.get()
        self.logpass=self.e1.get()
    
        return self.loguser,self.logpass   

    '''
    def Registration(self):
        self.t.destroy()
        self.t=Tk()
        self.t.title(" Registration Form")
        self.t.geometry("1366x768")
        self.t.iconbitmap("download.ico")
        self.loginf1=Frame(self.t,height=150,width=1366)
        self.logo=PhotoImage(file="mann.png")
        self.ba=Label(self.loginf1,image=self.logo,height=150).place(x=0,y=0)
        self.loginf1.pack(fill=BOTH,expand=1)
        self.loginf2=Frame(self.t,height=618,width=1366)
        self.c=Canvas(self.loginf2,height=618,width=1366)
        self.c.pack()
        self.logo1=PhotoImage(file="login.png")
        self.c.create_image(683,309,image=self.logo1)
        self.loginf2.pack(fill=BOTH,expand=1)
        self.b=Button(self.loginf2,text="Admin Registration",command=lambda:self.Register())
        self. b.place(x=1000,y=140)
        self. b1=Button(self.loginf2,text="Doctor Registration",width=15,command=lambda:self.login())
        self. b1.place(x=1200,y=140)
        '''
    


    def Register(self):
        self.t.destroy()
        self.t=Tk()
        self.t.title("Admin Registration Form")
        self.t.geometry("1366x768")
        self.t.iconbitmap("download.ico")
        self.loginf1=Frame(self.t,height=150,width=1366)
        self.logo=PhotoImage(file="mann.png")
        self.ba=Label(self.loginf1,image=self.logo,height=150).place(x=0,y=0)
        self.loginf1.pack(fill=BOTH,expand=1)
        self.loginf2=Frame(self.t,height=618,width=1366)
        self.c=Canvas(self.loginf2,height=618,width=1366)
        self.c.pack()
        self.logo1=PhotoImage(file="login.png")
        self.c.create_image(683,309,image=self.logo1)
        self.loginf2.pack(fill=BOTH,expand=1)
        self.b=Button(self.loginf1,text="HOME",command=lambda:self.Main())
        self. b.place(x=1000,y=140)
        self. b1=Button(self.loginf1,text="Login Now",width=15,command=lambda:self.login())
        self. b1.place(x=1070,y=140)
        self.l=Label(self.loginf2,text="Registration Form",font=("Elephant 30"))
        self.l.place(x=120,y=50)
        self.l1=Label(self.loginf2,text="First Name",font=("Elephant"))
        self.l1.place(x=100,y=130)
        self.fn=Entry(self.loginf2)
        self.fn.place(x=220,y=130)
        self.l1=Label(self.loginf2,text="Last Name",font=("Elephant"))
        self.l1.place(x=100,y=160)
        self.ln=Entry(self.loginf2)
        self.ln.place(x=220,y=160)
        self.l2=Label(self.loginf2,text="User Name",font=("Elephant"))
        self.l2.place(x=100,y=190)
        self.un=Entry(self.loginf2)
        self.un.place(x=220,y=190)
        self.l2=Label(self.loginf2,text="Password",font=("Elephant"))
        self.l2.place(x=100,y=220)
        self.pw=Entry(self.loginf2,show="*")
        self.pw.place(x=220,y=220)
        self.l1=Label(self.loginf2,text="Address",font=("Elephant "))
        self.l1.place(x=100,y=250)
        self.ad=Entry(self.loginf2)
        self.ad.place(x=220,y=250)
        self.l1=Label(self.loginf2,text="Email",font=("Elephant"))
        self.l1.place(x=100,y=280)
        self.email=Entry(self.loginf2)
        self.email.place(x=220,y=280)
        self.l1=Label(self.loginf2,text="Mob.No.",font=("Elephant"))
        self.l1.place(x=100,y=310)
        self.mn=Entry(self.loginf2)
        self.mn.place(x=220,y=310)
        self.l1=Label(self.loginf2,text="Gender",font=("Elephant"))
        self.l1.place(x=100,y=340)
        self.g=Entry(self.loginf2)
        self.g.place(x=220,y=340)
        self.l1=Label(self.loginf2,text="DOB",font=("Elephant"))
        self.l1.place(x=100,y=370)
        self.d=Entry(self.loginf2)
        self.d.place(x=220,y=370)
        self.b3=Button(self.loginf2,text="Register",font=("Elephant"),width=8,command=lambda:self.adminreg())
        self.b3.place(x=160,y=430)

    def DoctorRegister(self):
        self.t.destroy()
        self.t=Tk()
        self.t.title("Doctor Registration Form")
        self.t.geometry("1366x768")
        self.t.iconbitmap("download.ico")
        self.loginf1=Frame(self.t,height=150,width=1366)
        self.logo=PhotoImage(file="mann.png")
        self.ba=Label(self.loginf1,image=self.logo,height=150).place(x=0,y=0)
        self.loginf1.pack(fill=BOTH,expand=1)
        self.loginf2=Frame(self.t,height=618,width=1366)
        self.c=Canvas(self.loginf2,height=618,width=1366)
        self.c.pack()
        self.logo1=PhotoImage(file="login.png")
        self.c.create_image(683,309,image=self.logo1)
        self.loginf2.pack(fill=BOTH,expand=1)
        self.b=Button(self.loginf1,text="HOME",command=lambda:self.Main())
        self. b.place(x=1000,y=140)
        self. b1=Button(self.loginf1,text="Login Now",width=15,command=lambda:self.login())
        self. b1.place(x=1070,y=140)
        self.l=Label(self.loginf2,text="Registration Form",font=("Elephant 30"))
        self.l.place(x=120,y=50)
        self.l1=Label(self.loginf2,text="Doctor Name",font=("Elephant"))
        self.l1.place(x=100,y=130)
        self.dn=Entry(self.loginf2)
        self.dn.place(x=220,y=130)
        self.l1=Label(self.loginf2,text="Last Name",font=("Elephant"))
        self.l1.place(x=100,y=160)
        self.ln=Entry(self.loginf2)
        self.ln.place(x=220,y=160)
        self.l2=Label(self.loginf2,text="User Name",font=("Elephant"))
        self.l2.place(x=100,y=190)
        self.un=Entry(self.loginf2)
        self.un.place(x=220,y=190)
        self.l2=Label(self.loginf2,text="Password",font=("Elephant"))
        self.l2.place(x=100,y=220)
        self.pw=Entry(self.loginf2,show="*")
        self.pw.place(x=220,y=220)
        self.l1=Label(self.loginf2,text="Address",font=("Elephant "))
        self.l1.place(x=100,y=250)
        self.ad=Entry(self.loginf2)
        self.ad.place(x=220,y=250)
        self.l1=Label(self.loginf2,text="Email",font=("Elephant"))
        self.l1.place(x=100,y=280)
        self.em=Entry(self.loginf2)
        self.em.place(x=220,y=280)
        self.l1=Label(self.loginf2,text="Mob.No.",font=("Elephant"))
        self.l1.place(x=100,y=310)
        self.mn=Entry(self.loginf2)
        self.mn.place(x=220,y=310)
        self.l1=Label(self.loginf2,text="Gender",font=("Elephant"))
        self.l1.place(x=100,y=340)
        self.g=Entry(self.loginf2)
        self.g.place(x=220,y=340)
        self.l1=Label(self.loginf2,text="DOB",font=("Elephant"))
        self.l1.place(x=100,y=370)
        self.d=Entry(self.loginf2)
        self.d.place(x=220,y=370)
        self.l1=Label(self.loginf2,text="Doctor ID",font=("Elephant"))
        self.l1.place(x=100,y=400)
        self.dd=Entry(self.loginf2)
        self.dd.place(x=220,y=400)
        
        self.b3=Button(self.loginf2,text="Register",font=("Elephant"),width=8,command=lambda:self.doctorreg())
        self.b3.place(x=160,y=430)
    
    def docres(self):

        
        self.username=self.un.get()
        self.password=self.pw.get()
        self.first=self.dn.get()
        self.last=self.ln.get()
        self.address=self.ad.get()
        self.email=self.em.get()
        self.mobile=self.mn.get()
        self.gender=self.g.get()
        self.dob=self.d.get()
        self.did=self.dd.get()

        return self.did,self.username,self.password,self.first,self.last,self.address,self.email,self.mobile,self.gender,self.dob
           

    def doclogres(self):
        self.loguser=self.e.get()
        self.logpass=self.e1.get()
        self.Did=self.e2.get()
        return  self.Did,self.loguser,self.logpass   

       



    def adminres(self):
        self.user=self.un.get()

        self.password=self.pw.get()
        self.first=self.fn.get()
        self.last=self.ln.get()
        self.address=self.ad.get()
        self.email=self.email.get()
        self.mobile=self.mn.get()
        self.gender=self.g.get()
        self.dob=self.d.get()

        

        return self.user,self.password,self.first,self.last,self.address,self.email,self.mobile,self.gender,self.dob
 
    




    def OT(self):
        self.t.destroy()
        self.t=Tk()
        self.t.title("OT")
        self.t.geometry("1366x768")
        self.t.iconbitmap("download.ico")
        self.loginf1=Frame(self.t,height=150,width=1366)
        self.logo=PhotoImage(file="mann.png")
        self.ba=Label(self.loginf1,image=self.logo,height=150).place(x=0,y=0)
        self.loginf1.pack(fill=BOTH,expand=1)
        self.loginf2=Frame(self.t,height=618,width=1366)
        self.c=Canvas(self.loginf2,height=618,width=1366)
        self.c.pack()
        self.logo1=PhotoImage(file="login.png")
        self.c.create_image(683,309,image=self.logo1)
        self.loginf2.pack(fill=BOTH,expand=1)
        self.b=Button(self.loginf2,text="HOME",command=lambda:self.Main())
        self. b.place(x=1100,y=140)
        self. b1=Button(self.loginf2,text="REGISTER YOURSELF",command=lambda:self.Register(),width=15)
        self. b1.place(x=1170,y=140)
        self.l=Label(self.loginf2,text="OT Schedule",font=("Elephant 30"))
        self.l.place(x=120,y=50)
        self.l1=Label(self.loginf2,text="Did",font=("Elephant "))
        self.l1.place(x=100,y=130)
        self.e=Entry(self.loginf2)
        self.e.place(x=280,y=130)
        
        self.l1=Label(self.loginf2,text="Doctor Name",font=("Elephant "))
        self.l1.place(x=100,y=170)
        self.e1=Entry(self.loginf2)
        self.e1.place(x=280,y=170)
        self.l2=Label(self.loginf2,text="Desgnation",font=("Elephant "))
        self.l2.place(x=100,y=210)
        self.e2=Entry(self.loginf2)
        self.e2.place(x=280,y=210)
        self.l3=Label(self.loginf2,text="Operation Type",font=("Elephant "))
        self.l3.place(x=100,y=250)
        self.e3=Entry(self.loginf2)
        self.e3.place(x=280,y=250)

        self.l3=Label(self.loginf2,text="Pid",font=("Elephant "))
        self.l3.place(x=100,y=290)
        self.e4=Entry(self.loginf2)
        self.e4.place(x=280,y=290)
        

        self.l3=Label(self.loginf2,text="Patient Name",font=("Elephant "))
        self.l3.place(x=100,y=330)
        self.e5=Entry(self.loginf2)
        self.e5.place(x=280,y=330)
        self.l3=Label(self.loginf2,text="Charges",font=("Elephant "))
        self.l3.place(x=100,y=370)
        self.e6=Entry(self.loginf2)
        self.e6.place(x=280,y=370)
        self.b3=Button(self.loginf2,text="Schedule OT",font=("Elephant"),width=15,command=lambda:self.OTreg())
        self.b3.place(x=160,y=400)
        self.t.mainloop()

        
    
    def OTres(self):

        self.pid=self.e.get()
        self.doctor=self.e1.get()
        self.designation=self.e2.get()
        self.type=self.e3.get()
        self.pid=self.e4.get()
        self.patient=self.e5.get()
        self.charges=self.e6.get()

        return  self.pid,self.doctor,self.designation,self.type,self.pid,self.patient,self.charges

        
    
    
    def doctorsearch(self):
        
        self.newWindow = Toplevel(self.t)
        self.app = SEA_AP(self.newWindow)


    #Function to open Patient Registration Window   
    def Patient_Reg(self):
        self.newWindow = Toplevel(self.t)
        self.app = Patient(self.newWindow)
        
    #Function to open Room Allocation Window   

    def Room_Allocation(self):
        self.newWindow = Toplevel(self.t)
        self.app = Room(self.newWindow)
        
    #Function to open Employee Registration Window 
    def Employee_Reg(self):
        self.newWindow = Toplevel(self.t)
        self.app = Employee(self.newWindow)
        
    #Function to open Appointment Window
    def Appointment_Form(self):
        self.newWindow = Toplevel(self.t)
        self.app = Appointment(self.newWindow)
        
    #Function to open Billing Window
    def Billing_Form(self):
        self.newWindow = Toplevel(self.t)
        self.app = Billing(self.newWindow)

    def Medicalaccess(self):
        self.newWindow = Toplevel(self.t)
        self.app = Medicalaccess(self.newWindow)
    
    
    def PatientCount(self):
        self.newWindow = Toplevel(self.t)
        self.app = Patientcount(self.newWindow)









    


        
    def adminreg(self):
        self.credreg=self.adminres()
        self.con=connect("HospitalDB.db")
        self.cur=self.con.cursor()
        try:
            self.cur.execute("create table admins(username varchar(50) not null,password varchar(50) not null,first varchar(50) not null,last varchar(50) not null,address varchar(50) not null,email varchar(50),mob varchar(50) not null,gender varchar(50) not null,dob varchar(50) not null)")
        except:
            pass
        x=self.cur.execute("select count(*) from admins where username=%r and dob=%r "%(self.credreg[0],self.credreg[8]))
        if list(x)[0][0]==0:
            if self.credreg[0]=="" or self.credreg[1]=="" or self.credreg[2]=="" or self.credreg[3]=="" or self.credreg[5]=="" or self.credreg[6]=="" or self.credreg[7]=="" or self.credreg[8]=="":
                messagebox.showinfo("Register","Empty Entry is not Allowed")
            else:
                self.cur.execute("insert into admins values(%r,%r,%r,%r,%r,%r,%r,%r,%r)"%(self.credreg[0],self.credreg[1],self.credreg[2],self.credreg[3],self.credreg[4],self.credreg[5],self.credreg[6], self.credreg[7],self.credreg[8]))
                self.con.commit()
                messagebox.showinfo("Register","Admin You are Successelfully Registered")
                self.login()
        else:
            messagebox.showinfo("Register","Username Already Exist \nEnter New Username")

    def adminlog(self):
        self.credlog=self.logres()
        self.con=connect("HospitalDB.db")
        self.cur=self.con.cursor()
        try:
            self.cur.execute("create table admins(username varchar(50) not null,password varchar(50) not null,first varchar(50) not null,last varchar(50) not null,address varchar(50) not null,email varchar(50),mob varchar(50) not null,gender varchar(50) not null,dob varchar(50) not null )")
        except:
            pass
        x=self.cur.execute("select count(*) from admins where username=%r and password=%r"%(self.credlog[0],self.credlog[1]))
        if list(x)[0][0]==0:
            if self.credlog[0]=="" or self.credlog[1]=="":
                messagebox.showinfo("Login","Empty Entry is not allowed")
            else:
                messagebox.showinfo("Login","You are Not Registered Yet")
            
        else:
            messagebox.showinfo("Login","You have Succeselfully Log In\nWelcome to Manorama Hospital")            
            self.AdminMain()

   
            
    def doctorreg(self):
        self.credreg=self.docres()
        self.con=connect("HospitalDB.db")
        self.cur=self.con.cursor()
        try:
            self.cur.execute("create table doctor(DoctorID varchar(50) not null,username varchar(50) not null,password varchar(50) not null,DoctorName varchar(50) not null,last varchar(50) not null,address varchar(50) not null,email varchar(50),mob varchar(50) not null,gender varchar(50) not null,dob varchar(50) not null)")
        except:
            pass
        x=self.cur.execute("select count(*) from doctor where DoctorID=%r and username=%r "%(self.credreg[0],self.credreg[1]))
        if list(x)[0][0]==0:
            if self.credreg[0]=="" or self.credreg[1]=="" or self.credreg[2]=="" or self.credreg[3]=="" or self.credreg[5]=="" or self.credreg[6]=="" or self.credreg[7]=="" or self.credreg[8]=="" or self.credreg[9]=="":
                messagebox.showinfo("Register","Empty Entry is not Allowed")
            else:
                self.cur.execute("insert into doctor values(%r,%r,%r,%r,%r,%r,%r,%r,%r,%r)"%(self.credreg[0],self.credreg[1],self.credreg[2],self.credreg[3],self.credreg[4],self.credreg[5],self.credreg[6], self.credreg[7],self.credreg[8],self.credreg[9]))
                self.con.commit()
                messagebox.showinfo("Register","Doctor You are Successelfully Registered")
                self.login()
        else:
            messagebox.showinfo("Register","Username Already Exist \nEnter New Username")

    def doclog(self):
        self.credlog=self.doclogres()
        self.con=connect("HospitalDB.db")
        self.cur=self.con.cursor()
        try:
            self.cur.execute("create table doctor(DoctorID varchar(50),username varchar(50) not null,password varchar(50) not null,first varchar(50) not null,last varchar(50) not null,address varchar(50) not null,email varchar(50),mob varchar(50) not null,gender varchar(50) not null,dob varchar(50) not null )")
        except:
            pass
        x=self.cur.execute("select count(*) from doctor where DoctorID=%r and username=%r and password=%r"%(self.credlog[0],self.credlog[1],self.credlog[2]))
        if list(x)[0][0]==0:
            if self.credlog[0]=="" or self.credlog[1]=="":
                messagebox.showinfo("Login","Empty Entry is not allowed")
            else:
                messagebox.showinfo("Login","You are Not Registered Yet")
            
        else:
            messagebox.showinfo("Login","You have Succeselfully Log In\nWelcome to Manorama Hospital")            
            self.DoctorMain()

   


    
    def OTreg(self):
        self.credreg=self.OTres()
        self.con=connect("HospitalDB.db")
        self.cur=self.con.cursor()
        try:
            self.cur.execute("create table OT(Did varchar(50) not null,Doctorname varchar(50) not null, Designation varchar(50) not null,Operation_type varchar(50) not null,Pid varchar(50) not null,Patient_name varchar(50) not null,Charges varchar(50) not null)")
        except:
            pass
        x=self.cur.execute("select count(*) from OT where Did=%r and Doctorname=%r "%(self.credreg[0],self.credreg[1]))
        if list(x)[0][0]==0:
            if self.credreg[0]=="" or self.credreg[1]=="" or self.credreg[2]=="" or self.credreg[3]=="" or self.credreg[5]=="" or self.credreg[6]=="":
                messagebox.showinfo("Register","Empty Entry is not Allowed")
            else:
                self.cur.execute("insert into OT values(%r,%r,%r,%r,%r,%r,%r)"%(self.credreg[0],self.credreg[1],self.credreg[2],self.credreg[3],self.credreg[4],self.credreg[5],self.credreg[6]))
                self.con.commit()
                messagebox.showinfo("Register","OT Successelfully Schedule")
                self.login()
        else:
            messagebox.showinfo("Register","Username Already Exist \nEnter New Username")



     
    def Contactsave(self):
        self.credreg=self.contactres()
        self.con=connect("HospitalDB.db")
        self.cur=self.con.cursor()
        try:
            self.cur.execute("create table doctor(DoctorID varchar(50) not null,username varchar(50) not null,password varchar(50) not null,DoctorName varchar(50) not null,last varchar(50) not null,address varchar(50) not null,email varchar(50),mob varchar(50) not null,gender varchar(50) not null,dob varchar(50) not null)")
        except:
            pass
        x=self.cur.execute("select count(*) from doctor where DoctorID=%r and username=%r "%(self.credreg[0],self.credreg[1]))
        if list(x)[0][0]==0:
            if self.credreg[0]=="" or self.credreg[1]=="" or self.credreg[2]=="" or self.credreg[3]=="" or self.credreg[5]=="" or self.credreg[6]=="" or self.credreg[7]=="" or self.credreg[8]=="" or self.credreg[9]=="":
                messagebox.showinfo("Register","Empty Entry is not Allowed")
            else:
                self.cur.execute("insert into doctor values(%r,%r,%r,%r,%r,%r,%r,%r,%r,%r)"%(self.credreg[0],self.credreg[1],self.credreg[2],self.credreg[3],self.credreg[4],self.credreg[5],self.credreg[6], self.credreg[7],self.credreg[8],self.credreg[9]))
                self.con.commit()
                messagebox.showinfo("Register","Doctor You are Successelfully Registered")
                self.login()
        else:
            messagebox.showinfo("Register","Username Already Exist \nEnter New Username")




    '''
    def appointmentreg(self):
        self.credreg=self.appointmentres()
        self.con=connect("manorama.db")
        self.cur=self.con.cursor()
        try:z
        
            self.cur.execute("create table appointment(doctor_name varchar(50) not null,date varchar(50) not null,time varchar(50) not null)")
        except:
            pass
        x=self.cur.execute("select count(*) from appointment where doctor_name=%r and time=%r "%(self.credreg[0],self.credreg[2]))
        if list(x)[0][0]==0:
            if self.credreg[0]=="" or self.credreg[1]=="" or self.credreg[2]=="" or self.credreg[3]=="":
                messagebox.showinfo("Register","Empty Entry is not Allowed(except Email)")
            else:
                self.cur.execute("insert into appointment values(%r,%r,%r)"%(self.credreg[0],self.credreg[1],self.credreg[2]))
                self.con.commit()
                messagebox.showinfo("Register","Your Appointment Successelfully Registered")
                self.login()
        else:
            messagebox.showinfo("Register","Username Already Exist \nEnter New Username")
    '''
    

    def patientcommunity(self):
        self.my_connection=sqlite3.connect("HospitalDB.db")
        self.t=Tk()
        self.t.geometry("1500x1500")
        self.result=self.my_connection.execute("select * from patient")
        i=0
        for patient in self.result:
            for j in range(len(patient)):
                e=Entry(self.t,width=13,fg="black", font="arial 16")
                e.grid(row=i,column=j)
                e.insert(END,patient[j])
                
            i=i+1    
        self.t.mainloop()        

    '''
    def accessmedical(self):
        self.my_connection=sqlite3.connect("HospitalDB.db")
        self.t=Tk()
        self.t.geometry("1500x1500")

        
        self.image=ImageTk.PhotoImage(Image.open("manor.png"))
        self.panel=Label(master,image=self.image)
        self.panel.pack()
        

        
        
        self.lblTitle = Label(self.master,text = "MEDICAL RECORD", font="Helvetica 20 bold", bg="sky blue")
        self.lblTitle.place(x =450,y =0)
    

        
        self.result=self.my_connection.execute("select * from MEDICINE")
        i=0
        for medical in self.result:
            for j in range(len(medical)):
                e=Entry(self.t,width=13,fg="black", font="arial 16")
                e.grid(row=i,column=j)
                e.insert(END,medical[j])
                
            i=i+1    
        self.t.mainloop()        
    '''

    

x=Hospital()
x.Main()   
        
