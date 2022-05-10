from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
import sqlite3

from PIL import ImageTk,Image
from tkinter import ttk

    
conn=sqlite3.connect("HospitalDB.db")
print("DATABASE CONNECTION SUCCESSFUL")
       
#CLASS FOR DISPLAY MENU FOR SEARCH APPOINTMENT          
class Medicalaccess:
    def __init__(self,master):

        import tkinter as tk
        global inp_s,entry,SearchB
        self.master = master
        
        self.master.title("MONORAMA HOSPITAL")
        self.master.iconbitmap("download.ico")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="sky blue")
        self.frame = Frame(self.master,bg="sky blue")
        #self.frame.pack()


        '''
        tree=ttk.Treeview(self.master,column=("c1","c2","c3","c4"),show='headings')
        tree.column("#1",anchor=tk.CENTER)
        tree.heading("#1",text="PID")
        tree.column("#2",anchor=tk.CENTER)
        tree.heading("#2",text="Medicine")

        
        tree.column("#3",anchor=tk.CENTER)
        tree.heading("#3",text="M.Cost")

        
        tree.column("#4",anchor=tk.CENTER)
        tree.heading("#4",text="M.Quantity")
        tree.pack()
    


        
        
        self.image=ImageTk.PhotoImage(Image.open("manor.png"))
        self.panel=Label(master,image=self.image)
        self.panel.pack()
        '''

        
        self.entry=StringVar()
        #self.lblTitle = Label(self.master,text = "MEDICAL RECORD", font="Helvetica 20 bold",bg="sky blue")
        #self.lblTitle.grid(row=0,column=4)


        self.mast=Label(self.master,text="",font="Helvetica 20 bold",bg="sky blue")
        self.mast.grid(row=2,column=0)

        
        self.mast=Label(self.master,text="",font="Helvetica 20 bold",bg="sky blue")
        self.mast.grid(row=3,column=0)

        self.mast=Label(self.master,text="Medical Records",font="Helvetica 20 bold",bg="sky blue")
        self.mast.grid(row=4,column=2)


        
        self.mast=Label(self.master,text="PID",font="Helvetica 20 bold",bg="sky blue")
        self.mast.grid(row=5,column=0)
        
        self.mast=Label(self.master,text="Medicine",font="Helvetica 20 bold",bg="sky blue")
        self.mast.grid(row=5,column=1)
        self.mast=Label(self.master,text="M.Cost",font="Helvetica 20 bold",bg="sky blue")
        self.mast.grid(row=5,column=2)

        self.mast=Label(self.master,text="M.Quantity",font="Helvetica 20 bold",bg="sky blue")
        self.mast.grid(row=5,column=3)
        

        
        

        self.result=conn.execute("select * from MEDICINE")
        i=15
        
        for medical in self.result:
            for j in range(len(medical)):
                e=Entry(self.master,width=13,fg="black",font="arial 16")
                e.grid(row=i,column=j)
                e.insert(END,medical[j])
            i=i+1    
        self.master.mainloop()        

  
        '''
        c1=conn.cursor()
        
        c1.execute("select * from MEDICINE")
        rows=c1.fetchall()
        for row in rows:
            print(row)
            tree.insert("",self.master.END,values=row)

        conn.close()

















        '''
        #==============FRAME==========
        '''self.master = Frame(self.master,width=400,height=80,relief="ridge",bg="sky blue",bd=20)
        self.master.place(x=100,y=100)
        self.master2 = Frame(self.master,width=400,height=80,relief="ridge",bg="sky blue",bd=20)
        self.master2.place(x=100,y=100)'''
        
        #===========LABELS=============          

        '''
        self.lblpatid = Label(self.master,text="ENTER DOCTOR ID TO SEARCH APPOINTMENTS",font="Helvetica 14 bold",bd=22)
        self.lblpatid.place(x=200,y=100)
        self.lblpatid= Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable= self.entry)
        self.lblpatid.place(x=630,y=120)

        self.SearchB = Button(self.master, text="SEARCH",width =10,font="Helvetica 14 bold",command = self.SEARCH_AP)
        self.SearchB.place(x=900,y=110)
        
    #FUNCTION TO SEARCH DATA IN APPOINTMENT FORM   
    def SEARCH_AP(self):
        global inp_s,entry,errorS,t,i,q,dis1,dis2,dis3,dis4,dis5,dis6,dis7,dis8,dis9,dis10,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10
        c1=conn.cursor()
        ap=(self.entry.get())
        p = list(c1.execute("select * from appointment where DoctorID=?", (ap,)))
        if (len(p) == 0):
            tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM","THERE'S NO APPOINTMENT BOOKED")
        else:
            t=c1.execute('SELECT PATIENT_ID,NAME,AP_NO,DoctorID,AP_DATE,AP_TIME FROM PATIENT NATURAL JOIN appointment where DoctorID=? ',(ap,))          
            for i in t:
                self.l1 = Label(self.master,text="PATIENT ID",font="Helvetica 14 bold",bd=22)
                self.l1.place(x=100,y=200)
                self.dis1= Label(self.master,font="Helvetica 14 bold",bd=2,bg="sky blue",text=i[0])
                self.dis1.place(x=300,y=200)                      
                self.l2 = Label(self.master,text="PATIENT NAME",font="Helvetica 14 bold",bd=22)
                self.l2.place(x=600,y=200)
                self.dis2=Label(self.master,font="Helvetica 14 bold",bd=2,bg="sky blue",text=i[1])

                self.dis2.place(x=800,y=200)

                self.l3 = Label(self.master,text="APPOINTMENT NO",font="Helvetica 14 bold",bd=22)
                self.l3.place(x=100,y=300)
                self.dis3  = Label(self.master,font="Helvetica 14 bold",bg="sky blue",bd=2,text=i[2])
                self.dis3.place(x=300,y=300)

                self.l4 = Label(self.master,text="DOCTOR ID",font="Helvetica 14 bold",bd=22)
                self.l4.place(x=600,y=300)
                self.dis4= Label(self.master,font="Helvetica 14 bold",bg="sky blue",bd=2,text=i[3])
                self.dis4.place(x=800,y=300)
                        
                self.l5 = Label(self.master,text="APPOINTMENT TIME(HH:MM:SS)",font="Helvetica 14 bold",bd=22)
                self.l5.place(x=100,y=400)
                self.dis5 = Label(self.master,font="Helvetica 14 bold",bd=2,text=i[5])
                self.dis5.place(x=300,y=400)


                '''  
               
  
