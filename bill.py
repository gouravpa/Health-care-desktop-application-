
from payment import *
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
import sqlite3
from PIL import ImageTk,Image
from tkinter import messagebox
    
conn=sqlite3.connect("HospitalDB.db")
print("DATABASE CONNECTION SUCCESSFUL")

#Class for BILLING  
class Billing:
    def __init__(self,master):
        self.master = master
        
        self.master.title("MONORAMA HOSPITAL")
        self.master.iconbitmap("download.ico")
        self.master.geometry("1500x700+0+0")

        
        self.image=ImageTk.PhotoImage(Image.open("manor.png"))
        self.panel=Label(master,image=self.image)
        self.panel.pack()
        #self.master.config(bg="cadet blue")
        #self.master = master(self.master,bg="cadet blue")
        #self.master.pack()

        #=============ATTRIBUTES===========
        self.B_id=IntVar()
        self.P_id=IntVar()
        self.dd = StringVar()
        self.treat_1=StringVar()
        self.treat_2=StringVar()
        self.cost_t=IntVar()
        self.med=StringVar()
        self.med_q=IntVar()
        self.price=IntVar()
                
        #===============TITLE==========
        self.lblTitle = Label(self.master,text = "BILLING WINDOW", font="Helvetica 20 bold",bg="sky blue")
        self.lblTitle.place(x =350,y = 10)
        #==============master==========
        '''
        self.Loginmaster = master(self.master,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.Loginmaster.place(x=100,y=100)
        
        self.Loginmaster2 = master(self.master,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.Loginmaster2.place(x=2,y=0)
        '''
        #===========LABELS=============          
        self.lblpid = Label(self.master,text="PATIENT ID",font="Helvetica 14 bold",bd=22)
        self.lblpid.place(x=100,y=100)
        self.lblpid  = Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable=self.P_id )
        self.lblpid.place(x=300,y=110)
        
        self.lbldid = Label(self.master,text="DATE DISCHARGED(YYYY-MM-DD)",font="Helvetica 14 bold",bd=22)
        self.lbldid.place(x=700,y=100)
        self.lbldid  = Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable=self.dd )
        self.lbldid.place(x=1100,y=115)       
        
        self.lbltreat= Label(self.master,text="TREATMENT",font="Helvetica 14 bold",bd=22)
        self.lbltreat.place(x=100,y=200)
        self.lbltreat  = Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable=self.treat_1 )
        self.lbltreat.place(x=300,y=210) 
  
        self.lblcode_t1= Label(self.master,text="BILL_ID",font="Helvetica 14 bold",bd=22)
        self.lblcode_t1.place(x=700,y=200)
        self.lblcode_t1= Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable=self.B_id)
        self.lblcode_t1.place(x=920,y=215)

        
        self.lblap = Label(self.master,text="TREATMENT COST ₹",font="Helvetica 14 bold",bd=22)
        self.lblap.place(x=100,y=300)
        self.lblap  = Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable=self.cost_t)
        self.lblap.place(x=330,y=310)
            
        self.lblmed = Label(self.master,text="MEDICINE",font="Helvetica 14 bold",bd=22)
        self.lblmed.place(x=700,y=300)
        self.lblmed  = Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable=self.med)
        self.lblmed.place(x=920,y=315)
        
        self.med_t1= Label(self.master,text="MEDICINE QUANTITY",font="Helvetica 14 bold",bd=22)
        self.med_t1.place(x=100,y=400)
        self.med_t1 = Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable=self.med_q)
        self.med_t1.place(x=330,y=410)
        
        self.lblapd = Label(self.master,text="MEDICINE PRICE ₹",font="Helvetica 14 bold",bd=22)
        self.lblapd.place(x=700,y=400)
        self.lblapd  = Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable=self.price)
        self.lblapd.place(x=920,y=410)

        
        '''
        self.button2 = Button(self.master, text="UPDATE DISCHARGE DATE",width =25,font="Helvetica 14 bold",command = self.UPDATE_DATE)
        self.button2.place(x=100,y=500)
        '''
        
        #===========BUTTONS=============    

          
        self.button3 = Button(self.master, text="UPDATE DATA",width =15,font="Helvetica 14 bold",command= self.INSERT_BILL)
        self.button3.place(x=100,y=600)
        
        self.button3 = Button(self.master, text="GENERATE BILL",width =15,font="Helvetica 14 bold",command= self.GEN_BILL)
        self.button3.place(x=300,y=600)
        

        
        self.button4 = Button(self.master, text="Pay Now",width =10,font="Helvetica 14 bold",command=lambda:self.show())
        self.button4.place(x=400,y=600)

        self.button6 = Button(self.master, text="EXIT",width =10,font="Helvetica 14 bold",command = self.Exit)
        self.button6.place(x=500,y=600)
        
        
    def Show(self):
        self.newWindow = Toplevel(self.master)
        self.app = Payment(self.newWindow)


    def INSERT_BILL(self):
        global pp1, pp2, pp3, pp4, pp5, pp6, pp7, pp8, pp9, pp10,ce1,conn
        conn=sqlite3.connect("HospitalDB.db")
        conn.cursor()

        p0=(self.B_id.get())
        p1=(self.P_id.get())
        p2=(self.dd.get())
        p3=(self.treat_1.get())
        p4=(self.cost_t.get())
        p5=(self.med.get())
        p6=(self.med_q.get())
        p7=(self.price.get())
        #p = list(conn.execute("SELECT * FROM PATIENT  WHERE PATIENT_ID =?",(p1,)))

        '''
        #x=len(p)
        if x!=0:
             tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM","PATIENT_ID ALREADY EXISTS")
        else:


        '''
        conn.execute('INSERT INTO bill VALUES(?,?,?,?,?,?,?,?)',(p0,p1,p2,p3,p4,p5,p6,p7))
            
        tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM","DETAILS INSERTED INTO DATABASE")
        conn.commit()







    '''
    #FUNCTION TO UPDATE DATE IN BILLING FORM 
    def UPDATE_DATE(self):
        global b1,b2
        conn = sqlite3.connect("HospitalDB.db")
        conn.cursor()
        b1 = (self.P_id.get())
        b2 =(self.dd.get())  
        conn.execute("UPDATE ROOM SET DATE_DISCHARGED=? where PATIENT_ID=?", (b2, b1,))
        conn.commit()
        tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "DISCHARGE DATE UPDATED")
        
    #FUNCTION TO UPDATE DATA IN BILLING FORM 
    def UPDATE_DATA(self):
        global c1, b1, P_id, b3, b4, b5, b6, dd, treat_1, treat_2, cost_t, b7, b8, med, med_q, price, u
        conn = sqlite3.connect("HospitalDB.db")
        c1 = conn.cursor()
        b1 = (self.P_id.get())
        b3 = (self.treat_1.get())
        b4 = (self.treat_2.get())
        b5 = (self.cost_t.get())
        b6 = (self.med.get())
        b7 = (self.med_q.get())
        b8 = (self.price.get())   
        p = list(conn.execute("Select * from TREATMENT where TREATMENT.PATIENT_ID=?", (b1,)))  
        if len(p) != 0:
            tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM", "PATIENT ID IS ALREADY REGISTERED")
        else:
            conn.execute("INSERT INTO TREATMENT VALUES(?,?,?,?)", (b1, b3, b4, b5,))
            conn.execute("INSERT INTO MEDICINE VALUES(?,?,?,?)", (b1, b6, b7, b8,))
            conn.commit()
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "BILLING DATA SAVED")
     '''       
    #FUNCTION TO GENERATE BILL IN BILLING FORM 
    '''
    def GEN_BILL(self):
        global b1
        b1 = (self.P_id.get())
        conn = sqlite3.connect("HospitalDB.db")
        u=conn.execute("Select sum(T_COST+ (M_COST*M_QTY) +(DATE_DISCHARGED-DATE_ADMITTED)*RATE) FROM ROOM NATURAL JOIN TREATMENT natural JOIN MEDICINE where PATIENT_ID=?",(b1,) )
        for ii in u:
            self.pp=Label(self.Loginmaster,text="TOTAL AMOUNT OUTSTANDING",font="Helvetica 14 bold",bg="cadet blue",bd=22)
            self.pp.place(x=5,y=0)
            self.uu=Label(self.Loginmaster,font="Helvetica 14 bold",bg="cadet blue",bd=22,text=ii[0])
            self.uu.place(x=5,y=1) 
   '''
    
    def GEN_BILL(self):
        global b1,cost_t,med_q,price,pp1,pp2,pp3

        


        
        b1 = (self.P_id.get())
        #b6 = (self.med.get())
        b7 = (self.med_q.get())
        b8 = (self.price.get()) 
        conn = sqlite3.connect("HospitalDB.db")
        conn.cursor()


        
        u=conn.execute("select * from bill where Pid=?",(b1,) )
        for ii in u:




            self.pp1=ii[4]
            self.pp2=ii[6]
            self.pp3=ii[7]
            
        self.total=int(self.pp1)+int(self.pp2)*int(self.pp3)
        self.pp=Label(self.master,text="TOTAL AMOUNT OUTSTANDING",font="Helvetica 14 bold",bg="sky blue",bd=22)
        self.pp.place(x=100,y=500)
        self.uu=Label(self.master,font="Helvetica 14 bold",bg="cadet blue",bd=22,text=self.total)
        self.uu.place(x=600,y=500)
    
            


        '''
        self.total=int(self.pp1)+int(self.pp2)*int(self.pp3)
        self.pp=Label(self.master,text="TOTAL AMOUNT OUTSTANDING",font="Helvetica 14 bold",bg="sky blue",bd=22)
        self.pp.place(x=100,y=500)
        self.uu=Label(self.master,font="Helvetica 14 bold",bg="cadet blue",bd=22,text=self.total)
        self.uu.place(x=300,y=500)
            #b5 = (self.cost_t.get())

        
        
        r=int(self.cost_t.get())+int(self.med_q.get())*int(self.price.get())
        print(r)
        self.p=Label(self.master,text=r)
        self.p.place(x=200,y=600)
        '''
    
    
    #FUNCTION TO EXIT BILLING WINDOW
    
    def show(self):
        messagebox.showinfo("Information","Payment Method is not available for now")
        self.master.destroy()
        
    def Exit(self):            
        self.master.destroy()



    

    

        
        

