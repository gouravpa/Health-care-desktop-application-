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
class SEA_AP:
    def __init__(self,master):    
        global inp_s,entry,SearchB
        self.master = master
        
        self.master.title("MONORAMA HOSPITAL")
        self.master.iconbitmap("download.ico")
        self.master.geometry("1500x700+0+0")
        #self.master.config(bg="sky blue")
        #self.master = Frame(self.master,bg="sky blue")
        #self.master.pack()
        self.image=ImageTk.PhotoImage(Image.open("manor.png"))
        self.panel=Label(master,image=self.image)
        self.panel.place(x=0,y=0)
        self.entry=StringVar()
        self.lblTitle = Label(self.master,text = "SEARCH APPOINTMENT WINDOW", font="Helvetica 20 bold",bg="sky blue")
        self.lblTitle.grid(row=0,column=3)
        #==============FRAME==========
        '''self.master = Frame(self.master,width=400,height=80,relief="ridge",bg="sky blue",bd=20)
        self.master.place(x=100,y=100)
        self.master2 = Frame(self.master,width=400,height=80,relief="ridge",bg="sky blue",bd=20)
        self.master2.place(x=100,y=100)'''
        
        #===========LABELS=============          
        self.did = Label(self.master,text="ENTER DOCTOR ID TO SEARCH APPOINTMENTS",font="Helvetica 14 bold",bd=22)
        self.did.grid(row=1,column=1)
        self.did= Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable= self.entry)
        self.did.grid(row=1,column=3)

        self.SearchB = Button(self.master,text="SEARCH",width =10,font="Helvetica 14 bold",command = self.SEARCH_AP)
        self.SearchB.grid(row=1,column=4)

               
        self.lbl1 = Label(self.master,text="Patient ID",font="Helvetica 14 bold",bd=22)
        self.lbl1.grid(row=2,column=0)

        self.lbl2 = Label(self.master,text="Doctor ID",font="Helvetica 14 bold",bd=22)
        self.lbl2.grid(row=2,column=1)
 

        self.lbl1 = Label(self.master,text="Appoint. No",font="Helvetica 14 bold",bd=22)
        self.lbl1.grid(row=2,column=2)


        self.lbl1 = Label(self.master,text="Time",font="Helvetica 14 bold",bd=22)
        self.lbl1.grid(row=2,column=3)

        self.lbl1 = Label(self.master,text="Date",font="Helvetica 14 bold",bd=22)
        self.lbl1.grid(row=2,column=4)


        self.lbl1 = Label(self.master,text="Description",font="Helvetica 14 bold",bd=22)
        self.lbl1.grid(row=2,column=5)

       


        
    #FUNCTION TO SEARCH DATA IN APPOINTMENT FORM   
    def SEARCH_AP(self):



        global inp_s,entry,errorS,t,i,q,dis1,dis2,dis3,dis4,dis5,dis6,dis7,dis8,dis9,dis10,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,c1
        self.app=self.did.get()


        self.c=conn.cursor()
        self.c.execute("select * from appointment where DoctorID=%s"%(self.app))
        
        self.r=self.c.fetchall()
        self.num=3
        for i in self.r:

            
            self.pid=Label(self.master,text=i[0],font="time 12 bold")
            self.pid.grid(row=self.num,column=0,padx=10,pady=10)

            self.did=Label(self.master,text=i[1],font="time 12 bold")
            self.did.grid(row=self.num,column=1,padx=10,pady=10)

            self.apno=Label(self.master,text=i[2],font="time 12 bold")
            self.apno.grid(row=self.num,column=2,padx=10,pady=10)

            self.apdate=Label(self.master,text=i[3],font="time 12 bold")
            self.apdate.grid(row=self.num,column=3,padx=10,pady=10)

            self.aptime=Label(self.master,text=i[4],font="time 12 bold")
            self.aptime.grid(row=self.num,column=4,padx=10,pady=10)

            self.desc=Label(self.master,text=i[5],font="time 12 bold")
            self.desc.grid(row=self.num,column=5,padx=10,pady=10)


            self.num=self.num+1

        self.master.mainloop()     


















        
        '''
        self.result=conn.execute("select * from appointment where DoctorID=%s"%(self.app))
        self.master.geometry("1500x1500")
      
        i=3
        for appoint in self.result:
            
            for j in range(len(appoint)):
                e=Entry(self.master,width=12,fg="black", font="arial 16")
                e.grid(row=i,column=j,ipadx=5,ipady=5,padx=3,pady=5,sticky="nw")
                e.insert(END,appoint[j])
                
            i=i+1    
        self.master.mainloop() 
        '''

        '''
        global inp_s,entry,errorS,t,i,q,dis1,dis2,dis3,dis4,dis5,dis6,dis7,dis8,dis9,dis10,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,c1
        self.conn=sqlite3.connect("HospitalDB.db")
        c1=self.conn.cursor()
        ap=(self.entry.get())
        p = list(c1.execute("select count(*) from appointment where DoctorID=1"))
        if (len(p) == 0):
            tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM","THERE'S NO APPOINTMENT BOOKED")
        else:
            t=c1.execute('SELECT PATIENT_ID,AP_NO,DoctorID,AP_DATE,AP_TIME FROM appointment where DoctorID=? ',(ap,))          
            
            for i in t:
                self.ser=t.fetchall()
                self.l1 = Label(self.master,text="PATIENT ID",font="Helvetica 14 bold",bd=22)
                self.l1.place(x=100,y=200)
                self.dis1= Label(self.master,font="Helvetica 14 bold",bd=2,text=i[0])
                self.dis1.place(x=300,y=220)                      

                #self.l2 = Label(self.master,text="PATIENT NAME",font="Helvetica 14 bold",bd=22)
                #self.l2.place(x=600,y=200)
                #self.dis2=Label(self.master,font="Helvetica 14 bold",bd=2,text=i[1])
                #self.dis2.place(x=800,y=220)

                self.l3 = Label(self.master,text="APPOINTMENT NO",font="Helvetica 14 bold",bd=22)
                self.l3.place(x=100,y=300)
                self.dis3  = Label(self.master,font="Helvetica 14 bold",bd=2,text=i[1])
                self.dis3.place(x=310,y=320)

                self.l4 = Label(self.master,text="DOCTOR ID",font="Helvetica 14 bold",bd=22)
                self.l4.place(x=600,y=300)
                self.dis4= Label(self.master,font="Helvetica 14 bold",bd=2,text=i[2])
                self.dis4.place(x=800,y=320)
                        
                self.l5 = Label(self.master,text="APPOINTMENT TIME(HH:MM:SS)",font="Helvetica 14 bold",bd=22)
                self.l5.place(x=100,y=400)
                self.dis5 = Label(self.master,font="Helvetica 14 bold",bd=2,text=i[4])
                self.dis5.place(x=450,y=420)



                self.lbldes = Label(self.master,text="APPOINTMENT DATE",font="Helvetica 14 bold",bd=22)
                self.lbldes.place(x=600,y=400)
                self.lbldes =Label(self.master,font="Helvetica 14 bold",bd=2,text=i[3])
                self.lbldes.place(x=850,y=420)

                '''
        
        
               
           
        #def patientcommunity(self):
            #self.conn=sqlite3.connect("HospitalDB.db")
            #self.t=Tk()
            #self.t.geometry("1500x1500")
                 
        
