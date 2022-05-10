from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
import sqlite3
conn=sqlite3.connect("HospitalDB.db")
from PIL import ImageTk,Image

#Class for ROOM ALLOCATION    
class Room:
    
    def __init__(self,master):

        self.master = master
        
        self.master.title("MONORAMA HOSPITAL")
        self.master.iconbitmap("download.ico")
        self.master.geometry("1500x700+0+0")
        #self.master.config(bg="sky blue")
        #self.frame = Frame(self.master,bg="sky blue")
        #self.frame.pack()

        self.image=ImageTk.PhotoImage(Image.open("manor.png"))
        self.panel=Label(master,image=self.image)
        self.panel.pack()

        #=============ATTRIBUTES===========
        self.P_id=IntVar()
        self.room_t=StringVar()
        self.room_no=StringVar()
        self.rate=IntVar()
        self.da=StringVar()
        self.dd=StringVar()
      
        #===============TITLE==========
        self.lblTitle = Label(self.master,text = "ROOM ALLOCATION FORM", font="Helvetica 20 bold",bg="sky blue")
        self.lblTitle.place(x =450,y=20)
        #==============FRAME==========
        #self.master = Frame(self.frame,width=400,height=80,relief="ridge",bg="sky blue",bd=20)
        #self.master.place(x=1,y=0)
        
        #self.master2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="sky blue",bd=20)
        #self.master2.place(x=2,y=0)
        #===========LABELS=============          
        self.lblpatid = Label(self.master,text="PATIENT ID",font="Helvetica 14 bold",bd=22)
        self.lblpatid.place(x=100,y=100)
        self.lblpatid  = Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable= self.P_id)
        self.lblpatid.place(x=300,y=110)
        
        self.room_no1=Label(self.master,text="ROOM NUMBER ",font="Helvetica 14 bold",bd=22)
        self.room_no1.place(x=700,y=100)

        self.room_no1 = Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable= self.room_no)
        self.room_no1.place(x=910,y=110)
        
        self.lblda=Label(self.master,text="DATE ADMITTED",font="Helvetica 14 bold",bd=22)
        self.lblda.place(x=100,y=200)
        self.lblda=Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable= self.da)
        self.lblda.place(x=310,y=230)
        self.lbldd=Label(self.master,text="DATE DISCHARGED",font="Helvetica 14 bold",bd=22)
        self.lbldd.place(x=700,y=200)
        self.lbldd=Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable= self.dd)
        self.lbldd.place(x=930,y=230)
    
        self.room_t1= Label(self.master,text="ROOM TYPE\nSINGLE ROOM: Rs 4500\nTWIN SHARING : Rs2500\nTRIPLE SHARING: Rs2000\n",font="Helvetica 14 bold",bd=22)
        self.room_t1.place(x=100,y=300)
        self.room_t1 = Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable= self.room_t)
        self.room_t1.place(x=390,y=330)
        
        self.lblrate=Label(self.master,text="ROOM CHARGES",font="Helvetica 14 bold",bd=22)
        self.lblrate.place(x=700,y=300)
        self.lblrate=Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable= self.rate)
        self.lblrate.place(x=910,y=310)

        
        #===========BUTTONS============= 
        self.button2 = Button(self.master, text="SUBMIT",width =10,font="Helvetica 14 bold",command=self.INSERT_ROOM)
        self.button2.place(x=100,y=600)
        
        self.button3 = Button(self.master, text="UPDATE",width =10,font="Helvetica 14 bold",command=self.UPDATE_ROOM)
        self.button3.place(x=300,y=600)
        
        self.button5 = Button(self.master, text="ROOM DETAILS",width =15,font="Helvetica 14 bold",command=self.SEARCH_ROOM)
        self.button5.place(x=500,y=600)
        
        self.button6 = Button(self.master, text="EXIT",width =10,font="Helvetica 14 bold",command = self.Exit)
        self.button6.place(x=700,y=600)
        
    #FUNCTION TO INSERT DATA IN ROOM ALLOCATION FORM
    def INSERT_ROOM(self):
        global r1,r2,r3,r4,r5,r6,conn,p
        conn = sqlite3.connect("HospitalDB.db")
        conn.cursor()
        r1=(self.P_id.get())
        r2=(self.room_t.get())
        r3=(self.room_no.get())
        r4=(self.rate.get())
        r5=(self.da.get())
        r6=(self.dd.get())
        p = list(conn.execute("SELECT * FROM ROOM WHERE ROOM_NO=?",(r3,)))
        x=len(p)
        if x!=0:
             tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM","ROOM_NO IS CURRENTLY OCCUPIED")
        else:
            conn.execute('INSERT INTO ROOM VALUES(?,?,?,?,?,?)',(r1,r3, r2, r4, r5, r6,))
            tkinter.messagebox.showinfo("HOSPITAL DATABSE SYSTEM", "ROOM ALLOCATED")
            conn.commit()
            
    #FUNCTION TO OPEN SEARCH MENU IN ROOM ALLOCATION FORM
    def SEARCH_ROOM(self):
        self.newWindow= Toplevel(self.master)
        self.app = S_Room(self.newWindow)
        
    #FUNCTION TO EXIT ROOM ALLOCATION FORM
    def Exit(self):            
        self.master.destroy()   

    #FUNCTION TO UPDATE DATA IN ROOM ALLOCATION FORM       
    def UPDATE_ROOM(self):
        global P_id,r1,r2,room_t,da,dd,rate,room_no,r3,r4,r5,r6,conn
        r1=(self.P_id.get())
        r2=(self.room_t.get())
        r3=(self.room_no.get())
        r4=(self.rate.get())
        r5=(self.da.get())
        r6=(self.dd.get())
        p = list(conn.execute("Select * from ROOM where PATIENT_ID=? AND ROOM_NO=?",(r1,r3,)))
        if len(p) != 0:
            tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM", "PATIENT IS NOT ALLOCATED A ROOM")

        else:
            conn.execute('UPDATE ROOM SET ROOM_NO=?,ROOM_TYPE=?,RATE=?,DATE_ADMITTED=?,DATE_DISCHARGED=? where PATIENT_ID=?',(r3, r2, r4, r5, r6,r1,))
            tkinter.messagebox.showinfo("HOSPITAL DATABSE SYSTEM", "ROOM DETAILS UPDATED")
            conn.commit()

#CLASS FOR DISPLAY MENU FOR SEARCH ROOM
class S_Room:
    def __init__(self,master):    
        global inp_s,entry,SearchB
        self.master = master
        
        self.master.title("MONORAMA HOSPITAL")
        self.master.iconbitmap("download.ico")
        self.master.geometry("1500x700+0+0")
        # self.master.config(bg="sky blue")
        #self.frame = Frame(self.master,bg="sky blue")
        #self.frame.pack()


        

        self.image=ImageTk.PhotoImage(Image.open("manor.png"))
        self.panel=Label(master,image=self.image)
        self.panel.pack()
        self.Pr_id=IntVar()
        self.lblTitle = Label(self.master,text = "SEARCH PATIENT DETAILS", font="Helvetica 20 bold",bg="sky blue")
        self.lblTitle.place(x =400 ,y =20)
        #==============FRAME==========
        #self.master = Frame(self.frame,width=400,height=80,relief="ridge",bg="sky blue",bd=20)
        #self.master.place(x=1,y=0)
        #self.master2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="sky blue",bd=20)
        #self.master2.place(x=2,y=0)
        
        #===========LABELS=============          
        self.lblpatid = Label(self.master,text="ENTER PATIENT ID TO SEARCH",font="Helvetica 14 bold",bd=22)
        self.lblpatid.place(x=100,y=120)
        self.lblpatid= Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable= self.Pr_id)
        self.lblpatid.place(x=600,y=130)
        self.SearchB = Button(self.master, text="SEARCH",width =10,font="Helvetica 14 bold",command = self.ROOM_DISPLAY)
        self.SearchB.place(x=1000,y=120)    

    #FUNCTION TO SEARCH DATA IN ROOM ALLOCATION FORM
    def ROOM_DISPLAY(self):
        global pat_rm,lr1,dis1,lr2,dis2,c1,i,conn,c1,Pr_id
        conn = sqlite3.connect("HospitalDB.db")
        
        

        c1=conn.cursor()        
        pat_rm=(self.Pr_id.get())
        p=list(c1.execute('select * from  ROOM  where PATIENT_ID=?',(pat_rm,)))
        if (len(p)==0):
            tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM","PATIENT NOT ALLOCATED ROOM")
        else:
            t=c1.execute('SELECT PATIENT_ID,NAME,ROOM_NO,ROOM_TYPE FROM ROOM NATURAL JOIN PATIENT where PATIENT_ID=?',(pat_rm,));
            for i in t:
            
                self.l1 = Label(self.master,text="PATIENT ID",font="Helvetica 14 bold",bd=22)
                self.l1.place(x=200,y=300)
                self.dis1= Label(self.master,font="Helvetica 14 bold",bd=2,text=i[0])
                self.dis1.place(x=400,y=315)
                        
                self.l2 = Label(self.master,text="PATIENT NAME",font="Helvetica 14 bold",bd=22)
                self.l2.place(x=600,y=300)
                self.dis2=Label(self.master,font="Helvetica 14 bold",bd=2,text=i[1])
                self.dis2.place(x=800,y=315)

                self.l3 = Label(self.master,text="ROOM NO",font="Helvetica 14 bold",bd=22)
                self.l3.place(x=200,y=400)
                self.dis3= Label(self.master,font="Helvetica 14 bold",bd=2,text=i[2])
                self.dis3.place(x=400,y=415)

                self.l4 = Label(self.master,text="ROOM TYPE",font="Helvetica 14 bold",bd=22)
                self.l4.place(x=600,y=400)
                self.dis4= Label(self.master,font="Helvetica 14 bold",bd=2,text=i[3])
                self.dis4.place(x=800,y=415)                 
                       

  

