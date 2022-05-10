import tkinter
from tkinter import*
import sqlite3
from sqlite3 import *
from tkinter import messagebox
from tkinter import ttk

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
           
        self.t.title("Manorama Hospital")
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

        self.b=Button(self.f1,text="Welcome to Manorama ",bg="light grey",fg="black",font="elephant 20",width=20,command=lambda:self.login())
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
        self.t.title("Manorama Hospital")
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
        self.b2=Button(self.f1,text="Appointment Scheduling",bg="light grey",fg="black",font="elephant 10",command=lambda:self.appointment())
        self.b2.place(x=200,y=20)
        self.b3=Button(self.f1,text="Access To Medical Records",bg="light grey",fg="black",font="elephant 10",command="")
        self.b3.place(x=450,y=20)
        self.b4=Button(self.f1,text="Prescription Tracking",bg="light grey",fg="black",font="elephant 10",command="")
        self.b4.place(x=700,y=20)
        self.b5=Button(self.f1,text="Patient Community",bg="light grey",fg="black",font="elephant 10",command=lambda:self.patientcommunity())
        self.b5.place(x=940,y=20)
        self.b6=Button(self.f1,text="Admin Register",bg="light grey",fg="black",font="elephant 10",command=lambda:self.Register())
        self.b6.place(x=1150,y=20)
        self.b7=Button(self.f1,text="Patient Register",bg="light grey",fg="black",font="elephant 10",command=lambda:self.patreg())
        self.b7.place(x=1200,y=50)
        
        self.b=Button(self.f1,text="Welcome to Manorama ",bg="light grey",fg="black",font="elephant 20",width=20,command=lambda:self.login())
        self.b.place(x=950,y=480)
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
        self.l1=Label(text="Name:-VK Porwal\nEducation:-MBBS, MD (Peds)\n Experince:-10yrs\n Specialization:-PediatricInten \n Timing:8AM-12AM",font=("Elephant"))
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
        self.l1=Label(text="Name:-Dr. Devendra Ghanekar \nEducation:-MBBS\n Experince:-5 yrs\n Specialization:-DA Consultant \n Timing:9AM-1PM",font=("Elephant"))
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
        self.l1=Label(text="Name:-Dr.Neha Agrawal \nEducation:-MBBS,MD \n Experince:-7 yrs\n Specialization:- DM Consultant",font=("Elephant"))
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
        self.l1=Label(text="Name:-Dr.Rahul Jain \nEducation:-MBBS,MD \n Experince:-6 yrs\n Specialization:- Pathologist Consultant",font=("Elephant"))
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
        self.l1=Label(text="Name:-Dr.Rashmi Shad \nEducation:-MBBS \n Experince:-4 yrs\n Specialization:- DNB Consultant",font=("Elephant"))
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
        self.l1=Label(text="Name:-Dr.Sameer Nivsarkar\nEducation:-MBBS \n Experince:-3 yrs\n Specialization:-Consultant E.N.T",font=("Elephant"))
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
        self.l1=Label(text="Name:-Dr.Madhu Goyal\nEducation:-MBBS,MD \n Experince:-8 yrs\n Specialization:-Consultant Pediatrics",font=("Elephant"))
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
        self. b.place(x=1100,y=140)
        self. b1=Button(self.loginf2,text="REGISTER YOURSELF",command=lambda:self.Register(),width=15)
        self. b1.place(x=1170,y=140)
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
        self.b3=Button(self.loginf2,text="Signin",command=lambda:self.adminlog(),font=("Elephant"),width=8)
        self.b3.place(x=160,y=220)
        self.t.mainloop()        

    def logres(self):
        self.loguser=self.e.get()
        self.logpass=self.e1.get()
    
        return self.loguser,self.logpass   







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
 
   

    def appointment(self):

        self.t.destroy()
        self.t=Tk()
        self.t.title("Appointment")
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
        self.l=Label(self.loginf2,text="Appointment Schedule",font=("Elephant 30"))
        self.l.place(x=120,y=50)
        self.l1=Label(self.loginf2,text="Doctor Name",font=("Elephant "))
        self.l1.place(x=100,y=130)
        self.e=Entry(self.loginf2)
        self.e.place(x=250,y=130)
        self.l2=Label(self.loginf2,text="Date",font=("Elephant "))
        self.l2.place(x=100,y=170)
        self.e1=Entry(self.loginf2)
        self.e1.place(x=220,y=170)
        self.l3=Label(self.loginf2,text="Time",font=("Elephant "))
        self.l3.place(x=100,y=210)
        self.e2=Entry(self.loginf2)
        self.e2.place(x=220,y=210)
        self.b3=Button(self.loginf2,text="Schedule",font=("Elephant"),width=8,command=lambda:self.appointmentreg())
        self.b3.place(x=160,y=240)
        self.t.mainloop()

        


    def appointmentres(self):

        self.doctor=self.e.get()
        self.date=self.e1.get()
        self.time=self.e2.get()

        return self.doctor,self.date,self.time



        
    def adminreg(self):
        self.credreg=self.adminres()
        self.con=connect("manorama.db")
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
        self.con=connect("manorama.db")
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

    def patientregistration(self,x):
        self.credreg=self.patientresult()
        self.con=connect("manor.db")
        self.cur=self.con.cursor()
        try:
            self.cur.execute("create table demo(pid varchar(10) not null,first varchar(50) not null,last varchar(50) not null,gender varchar(50) not null,age varchar(50),email varchar(50) not null,mob varchar(50) not null,address varchar(50) not null,doctor varchar(50) not null,,disease varchar(50))")


        except:
            pass
        x=self.cur.execute("select count(*) from  demo where first=%r and doctor=%r "%(self.credreg[0],self.credreg[9]))
        if list(x)[0][0]==0:
            if self.credreg[0]=="" or self.credreg[1]=="" or self.credreg[2]=="" or self.credreg[3]=="" or self.credreg[5]=="" or self.credreg[6]=="" or self.credreg[7]=="" or self.credreg[8]=="" or self.credreg[9]=="":
                messagebox.showinfo("Register","Empty Entry is not Allowed(except Email)")
            else:
                self.cur.execute("insert into  demo values(%r,%r,%r,%r,%r,%r,%r,%r,%r)"%(self.credreg[0],self.credreg[1],self.credreg[2],self.credreg[3],self.credreg[4],self.credreg[5],self.credreg[6],self.credreg[7],self.credreg[8],self.credreg[9]))
                self.con.commit()
                messagebox.showinfo("Register","You are Successelfully Registered")
                self.AdminMain()
        else:
            messagebox.showinfo("Register","Patient Already Register \nEnter New Username")
        
   

    










    '''
    def appointmentreg(self):
        self.credreg=self.appointmentres()
        self.con=connect("manorama.db")
        self.cur=self.con.cursor()
        try:
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
    
    def appointmentreg(self):
        self.credreg=self.appointmentres()
        self.con=connect("manorama.db")
        self.cur=self.con.cursor()
        try:
            self.cur.execute("create table appointment(doctor varchar(50) not null,date varchar(50) not null,time varchar(50) not null)")
        except:
            pass
        x=self.cur.execute("select count(*) from appointment where doctor=%r and date=%r "%(self.credreg[0],self.credreg[1]))
        if list(x)[0][0]==0:
            if self.credreg[0]=="" or self.credreg[1]=="" or self.credreg[2]=="":
                messagebox.showinfo("Register","Empty Entry is not Allowed")
            else:
                self.cur.execute("insert into appointment values(%r,%r,%r)"%(self.credreg[0],self.credreg[1],self.credreg[2]))
                self.con.commit()
                messagebox.showinfo("Register","Dear Patient your Appointment is Schedule")
                self.AdminMain()
        else:
            
            messagebox.showinfo("Register","Patient Already Exist \nEnter New Username")


    def patientcommunity(self):
        self.my_connection=sqlite3.connect("manorama.db")
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
    def patreg(self):
       
         
           
        self.t=Tk()
        self.t.title("Patient Register")
        self.t.iconbitmap('download.ico')
        self.label=Label(self.t,text="Add patient Details",font=('arial',20,'bold'),bg="light blue",fg="red")
        self.label.pack(side=TOP,fill=X)

        self.label=Label(self.t,text="Registration",font=('arial',16,'bold'),bg="light blue",fg="red")
        self.label.pack(side=BOTTOM,fill=X)
        
        def create(self,x):
            
            self.conn=sqlite3.connect("databases.db")
            self.c=self.conn.cursor()
            self.c.execute("create table patients(pid integer primary key autoincrement,first_name TEXT,last_name TEXT, mob_number integer,email_id TEXT,address TEXT,DocterName TEXT,gender TEXT,age integer,disease TEXT, insert_date DATE DEFAULT CURRENT_DATE NOT NULL)")
            self.conn.commit()
            self.conn.close()
            self.create(self,x)

        self.label=Label(self.t,text="First Name",font=('arial',13,'bold'))
        self.label.place(x=30,y=60)

        self.name_entry = StringVar()
        self.name_entry = ttk.Entry(self.t,textvariable=self.name_entry)

        self.name_entry=ttk.Entry(self.t)
        self.name_entry.place(x=170,y=60,width=200,height=25)
        
        self.name_entry.focus()
        
        self.label1=Label(self.t,text="Last Name",font=('arial',13,'bold'))
        self.label1.place(x=30,y=100)

        self.name_entry2=StringVar()
        self.name_entry2=ttk.Entry(self.t,textvariable=self.name_entry2)
        self.name_entry2=ttk.Entry(self.t)
        self.name_entry2.place(x=170,y=100,width=200,height=25)

        self.label=Label(self.t,text="Mobile Number",font=('arial',13,'bold'))
        self.label.place(x=30,y=140)

        self.name_entry3=IntVar()
        self.name_entry3=ttk.Entry(self.t,textvariable=self.name_entry3)
        self.name_entry3=ttk.Entry(self.t)
        self.name_entry3.place(x=170,y=140,width=200,height=25)

        self.label1=Label(self.t,text="Email Id",font=('arial',13,'bold'))
        self.label1.place(x=30,y=180)

        self.name_entry4=StringVar()
        self.name_entry4=ttk.Entry(self.t,textvariable=self.name_entry4)
        self.name_entry4=ttk.Entry(self.t)
        self.name_entry4.place(x=170,y=180,width=200,height=25)

        self.label1=Label(self.t,text="Address",font=('arial',13,'bold'))
        self.label1.place(x=30,y=220)

        self.name_entry5=StringVar()
        self.name_entry5=ttk.Entry(self.t,textvariable=self.name_entry5)
        self.name_entry5=ttk.Entry(self.t)
        self.name_entry5.place(x=170,y=220,width=200,height=25)
        
        self.label1=Label(self.t,text="Doctor Name",font=('arial',13,'bold'))
        self.label1.place(x=30,y=260)

        self.name_entry6=StringVar()
        self.name_entry6=ttk.Entry(self.t,textvariable=self.name_entry6)
        self.name_entry6=ttk.Entry(self.t)
        self.name_entry6.place(x=170,y=260,width=200,height=25)
        
        self.label1=Label(self.t,text="Gender",font=('arial',13,'bold'))
        self.label1.place(x=30,y=300)
        self.name_entry7=StringVar()
        
        self.name_entry7=ttk.Entry(self.t,textvariable=self.name_entry7)
        self.name_entry7=ttk.Entry(self.t)
        self.name_entry7.place(x=170,y=300,width=200,height=25)

        self.label1=Label(self.t,text="Age",font=('arial',13,'bold'))
        self.label1.place(x=30,y=340)

        self.name_entry8=StringVar()
        self.name_entry8=ttk.Entry(self.t,textvariable=self.name_entry8)
        self.name_entry8=ttk.Entry(self.t)
        self.name_entry8.place(x=170,y=340,width=200,height=25)
        
        self.label1=Label(self.t,text="Disease",font=('arial',13,'bold'))
        self.label1.place(x=30,y=380)

        self.name_entry9=StringVar()
        self.name_entry9=ttk.Entry(self.t,textvariable=self.name_entry9)
        self.name_entry9=ttk.Entry(self.t)
        self.name_entry9.place(x=170,y=380,width=200,height=25)

        def savedata():
            self.conn=sqlite3.connect('databases.db')
            self.c=self.conn.cursor()
            self.c.execute("insert into patients(first_name,last_name,mob_number,email_id,address,DocterName,gender,age,disease) VALUES (?,?,?,?,?,?,?,?,?)",(self.name_entry.get(),self.name_entry2.get(),self.name_entry3.get(),self.name_entry4.get(),self.name_entry5.get(),self.name_entry6.get(),self.name_entry7.get(),self.name_entry8.get(),self.name_entry9.get()))
            self.conn.commit()
            print("saved")
    
        self.btn=ttk.Button(self.t,text="SAVE DATA",command=savedata)
        self.btn.place(x=170,y=440,width=200,height=30)

        self.t.geometry('1500x1500')
        self.t.resizable(False,False)
        self.t.mainloop()
        '''



x=Hospital()
x.Main()   
        
