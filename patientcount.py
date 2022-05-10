from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
import sqlite3
import tkinter as tk
from PIL import ImageTk,Image

    
conn=sqlite3.connect("HospitalDB.db")
print("DATABASE CONNECTION SUCCESSFUL")



#CLASS FOR DISPLAY MENU FOR SEARCH APPOINTMENT          
class Patientcount:
    def __init__(self,master):    
        global inp_s,entry,SearchB,c



        import tkinter as tk
        
        self.master = master
        
        self.master.title("MONORAMA HOSPITAL")
        self.master.iconbitmap("download.ico")
        self.master.geometry("1600x800")
        self.master.config(bg="sky blue")
        self.frame = Frame(self.master,bg="sky blue")




        
        #self.master = tk.Tk()
        '''
        self.master.title("MONORAMA HOSPITAL")
        self.master.iconbitmap("download.ico")
        self.master.geometry("1500x1500")
        #self.master.resizable(1,1)
        self.master.config(bg="sky blue")
        self.master = Frame(self.master,bg="sky blue")
        self.master.pack()
        
        self.image=ImageTk.PhotoImage(Image.open("manor.png"))
        self.panel=Label(master,image=self.image)
        self.panel.pack()
        '''
        self.entry=StringVar()
        self.lblTitle = Label(self.master,text = "PATIENT RECORD", font="Helvetica 20 bold",bg="sky blue")
        self.lblTitle.grid(row=0,column=1,columnspan=20)


        self.p1 = Label(self.master,text = "Patient ID", font="time 15 bold")
        self.p1.grid(row=1,column=0,padx=10,pady=10)

        self.p2 = Label(self.master,text = "Patient Name", font="time 15 bold")
        self.p2.grid(row=1,column=1,padx=10,pady=10)

        self.p3 = Label(self.master,text = "Gender", font="time 15 bold")
        self.p3.grid(row=1,column=2,padx=10,pady=10)

        self.p4 = Label(self.master,text = "Blood Grp", font="time 15 bold")
        self.p4.grid(row=1,column=3,padx=10,pady=10)

        self.p5 = Label(self.master,text = "DOB", font="time 15 bold")
        self.p5.grid(row=1,column=4,padx=10,pady=10)

        self.p6 = Label(self.master,text = "Address", font="time 15 bold")
        self.p6.grid(row=1,column=5,padx=10,pady=10)


        self.p7 = Label(self.master,text = "Doctor", font="time 15 bold")
        self.p7.grid(row=1,column=6,padx=10,pady=10)


        self.p8 = Label(self.master,text = "Email ID", font="time 15 bold")
        self.p8.grid(row=1,column=7,padx=10,pady=10)

        
        #self.lblTitle = Label(self.master,text = "", font="Helvetica 20 bold",bg="sky blue")
        #self.lblTitle.grid(row=0,column=3)



        #self.lblTitle = Label(self.master,text = "PID                  Patient Name         ", font="Helvetica 20 bold",bg="sky blue")
        #self.lblTitle.grid(row=0,column=0)

        
        #self.mast=Label(self.master,text="PID                 Medicine Name                    Medicine Quantity                Medicine Cost",font="Helvetica 20 bold",bg="sky blue")
        #self.mast.grid(row=1,column=1)
      

  

        
    
        #self.my_connection=sqlite3.connect("HospitalDB.db")
        '''
        self.result=conn.execute("select * from patient")
        i=2
        for patient in self.result:
            for j in range(len(patient)):
                e=Entry(self.master,width=15,fg="black", font="arial 16")
                e.grid(row=i,column=j,ipadx=5,ipady=5,padx=5,pady=5)
                e.insert(END,patient[j])
                
            i=i+1
            
        self.master.mainloop() 
        '''
        
        self.c=conn.cursor()
        self.c.execute("select * from patient")
        
        self.r=self.c.fetchall()
        self.num=2
        for i in self.r:

            
            self.pid=Label(self.master,text=i[0],font="time 12 bold")
            self.pid.grid(row=self.num,column=0,padx=10,pady=10)

            self.pname=Label(self.master,text=i[1],font="time 12 bold")
            self.pname.grid(row=self.num,column=1,padx=10,pady=10)

            self.gender=Label(self.master,text=i[2],font="time 12 bold")
            self.gender.grid(row=self.num,column=2,padx=10,pady=10)

            self.bd=Label(self.master,text=i[3],font="time 12 bold")
            self.bd.grid(row=self.num,column=3,padx=10,pady=10)

            self.dob=Label(self.master,text=i[4],font="time 12 bold")
            self.dob.grid(row=self.num,column=4,padx=10,pady=10)

            self.ad=Label(self.master,text=i[5],font="time 12 bold")
            self.ad.grid(row=self.num,column=5,padx=10,pady=10)

            self.dd=Label(self.master,text=i[6],font="time 12 bold")
            self.dd.grid(row=self.num,column=6,padx=10,pady=10)

            self.gm=Label(self.master,text=i[7],font="time 12 bold")
            self.gm.grid(row=self.num,column=7,padx=10,pady=10)

            self.num=self.num+1

        self.master.mainloop()     
        
      
