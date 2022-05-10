from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
import sqlite3
from PIL import ImageTk,Image

conn=sqlite3.connect("HospitalDB.db")
print("DATABASE CONNECTION SUCCESSFUL")
                      
#Class for PATIENT REGISTRATION 
class Patient:
    def __init__(self,master):

        
        self.master = master
        '''
        self.master.title("MONORAMA HOSPITAL ")
        self.master.iconbitmap("download.ico")
        self.master.geometry("1500x700+0+0")
        self.master.config( )
        self.frame = Frame(self.master, )
        self.frame.pack()
        '''

        self.image=ImageTk.PhotoImage(Image.open("manor.png"))
        self.panel=Label(master,image=self.image)
        self.panel.pack()
        self.master.title("MONORAMA HOSPITAL")
        self.master.iconbitmap("download.ico")
        self.master.geometry("1500x700+0+0")
     





       
        #=============ATTRIBUTES===========
        
        self.pat_ID=IntVar()
        self.pat_name=StringVar()
        self.pat_dob=StringVar()
        self.pat_address=StringVar()
        self.pat_sex=StringVar()
        self.pat_BG=StringVar()
        self.pat_email=StringVar()
        self.pat_contact=IntVar()
        self.pat_contactalt=IntVar()
        self.pat_CT=StringVar()


        #===============TITLE==========
        self.lblTitle = Label(self.master,text = "PATIENT REGISTRATION FORM", font="Helvetica 20 bold",bg="sky blue" )
        self.lblTitle.place(x=350,y=5)
        #==============FRAME==========
        #self.master = Frame(self.frame,width=400,height=80,relief="ridge", ,bd=20)
        #self.master.place(x=1,y=0)
        
        #self.master2 = Frame(self.frame,width=400,height=80,relief="ridge", ,bd=20)
        #self.master2.place(x=2,y=0)
        #===========LABELS=============          
        self.lblpatid = Label(self.master,text="PATIENT ID",font="Helvetica 14 bold", )
        self.lblpatid.place(x=100,y=100)
        self.lblpatid  = Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable= self.pat_ID)
        self.lblpatid.place(x=210,y=100)
        
        self.lblPatname = Label(self.master,text="PATIENT NAME",font="Helvetica 14 bold", bd=22)
        self.lblPatname.place(x=630,y=100)
        self.lblPatname  = Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable= self.pat_name)
        self.lblPatname.place(x=850,y=120)

        self.lblsex = Label(self.master,text="SEX",font="Helvetica 14 bold", bd=22)
        self.lblsex.place(x=100,y=200)
        self.lblsex  = Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable= self.pat_sex)
        self.lblsex.place(x=200,y=220)

        self.lblDOB = Label(self.master,text="DOB (YYYY-MM-DD)",font="Helvetica 14 bold", bd=22)
        self.lblDOB.place(x=630,y=200)
        self.lblDOB  = Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable= self.pat_dob)
        self.lblDOB.place(x=850,y=220)
        
        self.lblbgrp = Label(self.master,text="BLOOD GROUP",font="Helvetica 14 bold", bd=22)
        self.lblbgrp.place(x=100,y=300)
        self.lblbgrp  = Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable= self.pat_BG)
        self.lblbgrp.place(x=270,y=320)
        
        self.lblCon = Label(self.master,text="CONTACT NUMBER",font="Helvetica 14 bold", bd=22)
        self.lblCon.place(x=630,y=300)
        self.lblCon  = Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable= self.pat_contact)
        self.lblCon.place(x=850,y=320)
        
        self.lblAlt = Label(self.master,text="ALTERNATE CONTACT",font="Helvetica 14 bold", bd=22)
        self.lblAlt.place(x=100,y=400)
        self.lblAlt  = Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable= self.pat_contactalt)
        self.lblAlt.place(x=350,y=420)
        
        self.lbleid = Label(self.master,text="EMAIL",font="Helvetica 14 bold", bd=22)
        self.lbleid.place(x=630,y=400)
        self.lbleid  = Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable= self.pat_email)
        self.lbleid.place(x=850,y=410)
        self.lbldoc = Label(self.master,text="CONSULTING DOCTOR",font="Helvetica 14 bold", bd=22)
        self.lbldoc.place(x=100,y=500)
        self.lbldoc  = Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable= self.pat_CT)
        self.lbldoc.place(x=350,y=520)

        self.lbladd = Label(self.master,text="ADDRESS",font="Helvetica 14 bold", bd=22)
        self.lbladd.place(x=630,y=500)
        self.lbladd  = Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable= self.pat_address)
        self.lbladd.place(x=850,y=510)
        
        #===========BUTTONS============= 
        self.button2 = Button(self.master, text="SUBMIT",width =10,font="Helvetica 14 bold", command = self.INSERT_PAT)
        self.button2.place(x=100,y=650)
        
        self.button3 = Button(self.master, text="UPDATE",width =10,font="Helvetica 14 bold", command= self.UPDATE_PAT)
        self.button3.place(x=300,y=650)
        
        self.button4 = Button(self.master, text="DELETE",width =10,font="Helvetica 14 bold", command= self.D_DISPLAY)
        self.button4.place(x=500,y=650)
        
        self.button5 = Button(self.master, text="SEARCH",width =10,font="Helvetica 14 bold", command= self.S_DISPLAY)
        self.button5.place(x=700,y=650)
        
        self.button6 = Button(self.master, text="EXIT",width =10,font="Helvetica 14 bold", command = self.Exit)
        self.button6.place(x=900,y=650)
            

    #FUNCTION TO INSERT DATA IN PATIENT FORM
    def INSERT_PAT(self):
        global pp1, pp2, pp3, pp4, pp5, pp6, pp7, pp8, pp9, pp10,ce1,conn
        conn=sqlite3.connect("HospitalDB.db")
        conn.cursor()
        p1=(self.pat_ID.get())
        p2=(self.pat_name.get())
        p3=(self.pat_sex.get())
        p4=(self.pat_BG.get())
        p5=(self.pat_dob.get())
        p6=(self.pat_contact.get())
        p7=(self.pat_contactalt.get())
        p8=(self.pat_address.get())
        p9=(self.pat_CT.get())
        p10=(self.pat_email.get())
        p = list(conn.execute("SELECT * FROM PATIENT  WHERE PATIENT_ID =?",(p1,)))
        x=len(p)
        if x!=0:
             tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM","PATIENT_ID ALREADY EXISTS")
        else:
            conn.execute('INSERT INTO PATIENT VALUES(?,?,?,?,?,?,?,?)',(p1,p2,p3,p4,p5,p8,p9,p10,))
            conn.execute('INSERT INTO CONTACT_NO VALUES (?,?,?)',(p1,p6,p7,))
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM","DETAILS INSERTED INTO DATABASE")
        conn.commit()
        
    #FUNCTION TO UPDATE DATA IN PATIENT FORM

    def UPDATE_PAT(self):
        global u1, u2, u3, u4, u5, u6, u7, u8, u9, u10, ue1, conn
        conn.cursor()
        u1 = (self.pat_ID.get())
        u2 = (self.pat_name.get())
        u3 = (self.pat_sex.get())
        u4 = (self.pat_dob.get())
        u5 = (self.pat_BG.get())
        u6 = (self.pat_contact.get())
        u7 = (self.pat_contactalt.get())
        u8 = (self.pat_email.get())
        u9 = (self.pat_CT.get())
        u10 = (self.pat_address.get())
        conn = sqlite3.connect("HospitalDB.db")
        p = list(conn.execute("Select * from PATIENT where PATIENT_ID=?", (u1,)))
        if len(p) != 0:
            conn.execute('UPDATE PATIENT SET NAME=?,SEX=?,DOB=?,BLOOD_GROUP=?,ADDRESS=?,CONSULT_TEAM=?,EMAIL=? where PATIENT_ID=?', ( u2, u3, u4, u5, u10, u9, u8,u1,))
            conn.execute('UPDATE CONTACT_NO set CONTACTNO=?,ALT_CONTACT=? WHERE PATIENT_ID=?', ( u6, u7,u1,))
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "DETAILS UPDATED INTO DATABASE")
            conn.commit()

        else:
            tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM", "PATIENT IS NOT REGISTERED")
            
    #FUNCTION TO EXIT PATIENT REGISTRATION WINDOW
    def Exit(self):            
        self.master.destroy()

    #FUNCTION TO OPEN DELETE PATIENT DISPLAY WINDOW
    def D_DISPLAY(self):
        self.newWindow = Toplevel(self.master)
        self.app = DMenu(self.newWindow)
        
    #FUNCTION TO OPEN SEARCH PATIENT DISPLAY WINDOW
    def S_DISPLAY(self):
        self.newWindow= Toplevel(self.master)
        self.app = SMenu(self.newWindow)

#CLASS FOR DISPLAY MENU FOR DELETE PATIENT
class DMenu:
    def __init__(self,master):    
        global inp_d,entry1,DeleteB
        self.master = master
        
        self.master.title("MONORAMA HOSPITAL")
        self.master.iconbitmap("download.ico")
        self.master.geometry("1500x700+0+0")

        self.image=ImageTk.PhotoImage(Image.open("manor.png"))
        self.panel=Label(master,image=self.image)
        self.panel.pack()
        #self.master.config( )
        #self.frame = Frame(self.master, )
        #self.frame.pack()
        
        self.del_pid=IntVar()
        self.lblTitle = Label(self.master,text = "DELETE WINDOW", font="Helvetica 20 bold",bg="sky blue" )
        self.lblTitle.place(x =450 ,y = 50)
        #==============FRAME==========
        '''
        self.master = Frame(self.frame,width=400,height=80,relief="ridge", ,bd=20)
        self.master.place(x=1,y=0)
        self.master2 = Frame(self.frame,width=400,height=80,relief="ridge", ,bd=20)
        self.master2.place(x=2,y=0)

        '''
        #===========LABELS=============          
        self.lblpatid = Label(self.master,text="ENTER PATIENT ID TO DELETE",font="Helvetica 14 bold", bd=22)
        self.lblpatid.place(x=100,y=200)
        self.lblpatid= Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable= self.del_pid)
        self.lblpatid.place(x=600,y=210)

        self.DeleteB = Button(self.master, text="DELETE",width =10,font="Helvetica 14 bold", command = self.DELETE_PAT)
        self.DeleteB.place(x=400,y=400)

    #FUNCTION TO DELETE DATA IN PATIENT FORM
    def DELETE_PAT(self):        
        global inp_d,del_pid
        c1= conn.cursor()
        inp_d = (self.del_pid.get())
        p=list(conn.execute("select * from PATIENT where PATIENT_ID=?", (inp_d,)))
        if (len(p)==0):
            tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM","PATIENT RECORD NOT FOUND")
        else:
            conn.execute('DELETE FROM PATIENT where PATIENT_ID=?',(inp_d,))
            conn.execute('DELETE FROM CONTACT_NO WHERE PATIENT_ID=?', (inp_d,))
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "DETAILS DELETED FROM DATABASE")
            conn.commit()

#CLASS FOR SEARCH MENU FOR SEARCH PATIENT
class SMenu:
    def __init__(self,master):    
        global inp_s,s_pid,g_pid,SearchB
        self.master = master
        
        self.master.title("MONORAMA HOSPITAL")
        self.master.iconbitmap("download.ico")
        self.master.geometry("1500x700+0+0")
        #self.master.config( )
        #self.frame = Frame(self.master, )
        #self.frame.pack()


        self.image=ImageTk.PhotoImage(Image.open("manor.png"))
        self.panel=Label(master,image=self.image)
        self.panel.pack()
        

        
        self.s_pid=IntVar()
        self.g_pid=StringVar()
        self.lblTitle = Label(self.master,text = "SEARCH WINDOW", font="Helvetica 20 bold", bg="sky blue")
        self.lblTitle.place(x =450,y =0)
        #==============FRAME==========
        #self.master = Frame(self.frame,width=400,height=80,relief="ridge", ,bd=20)
        #self.master.place(x=1,y=0)
        #self.master2 = Frame(self.frame,width=400,height=80,relief="ridge", ,bd=20)
        #self.master2.place(x=2,y=0)
        
        #===========LABELS=============          
        self.lblpatid = Label(self.master,text="ENTER PATIENT ID TO SEARCH",font="Helvetica 14 bold", bd=22)
        self.lblpatid.place(x=50,y=20)
        self.lblpatid= Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable= self.s_pid)
        self.lblpatid.place(x=500,y=40)

        self.lblpatid = Label(self.master,text="ENTER PATIENT GMAIL ID TO SEARCH",font="Helvetica 14 bold", bd=22)
        self.lblpatid.place(x=700,y=20)
        self.lblpatid= Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable= self.g_pid)
        self.lblpatid.place(x=1200,y=40)


        self.SearchB = Button(self.master, text="PSEARCH",width =10,font="Helvetica 14 bold", command = self.SEARCH_PAT)
        self.SearchB.place(x=1300,y=100)

        self.SearchB = Button(self.master, text="GSEARCH",width =10,font="Helvetica 14 bold", command = self.GSEARCH_PAT)
        self.SearchB.place(x=1300,y=200)
        

        
    #FUNCTION TO SEARCH DATA IN PATIENT FORM
    def SEARCH_PAT(self):
        global inp_s,s_pid,errorS,t,i,q,dis1,dis2,dis3,dis4,dis5,dis6,dis7,dis8,dis9,dis10,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10
        c1=conn.cursor()
        inp_s=(self.s_pid.get())                
        p=list(conn.execute('select * from PATIENT where PATIENT_ID=?',(inp_s,)))
        if (len(p)==0):
            tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM","PATIENT RECORD NOT FOUND")
                    
        else:
            t=c1.execute('SELECT * FROM PATIENT NATURAL JOIN CONTACT_NO where PATIENT_ID=?',(inp_s,));
            for i in t:
                        self.l1 = Label(self.master,text="PATIENT ID",font="Helvetica 14 bold", bd=22)
                        self.l1.place(x=100,y=100)
                        self.dis1= Label(self.master,font="Helvetica 14 bold",bd=2,text=i[0])
                        self.dis1.place(x=320,y=115)
                        
                        self.l2 = Label(self.master,text="PATIENT NAME",font="Helvetica 14 bold", bd=22)
                        self.l2.place(x=700,y=100)
                        self.dis2=Label(self.master,font="Helvetica 14 bold",bd=2,text=i[1])
                        self.dis2.place(x=900,y=110)

                        self.l3 = Label(self.master,text="SEX",font="Helvetica 14 bold", bd=22)
                        self.l3.place(x=100,y=200)
                        self.dis3  =Label(self.master,font="Helvetica 14 bold",bd=2,text=i[2])
                        self.dis3.place(x=200,y=220)

                        self.l4 = Label(self.master,text="DOB (YYYY-MM-DD)",font="Helvetica 14 bold", bd=22)
                        self.l4.place(x=700,y=200)
                        self.dis4=Label(self.master,font="Helvetica 14 bold",bd=2,text=i[4])
                        self.dis4.place(x=940,y=210)
                        
                        self.l5 = Label(self.master,text="BLOOD GROUP",font="Helvetica 14 bold", bd=22)
                        self.l5.place(x=100,y=300)
                        self.dis5 =Label(self.master,font="Helvetica 14 bold",bd=2,text=i[3])
                        self.dis5.place(x=300,y=320)
                        
                        self.l6 = Label(self.master,text="CONTACT NUMBER",font="Helvetica 14 bold", bd=22)
                        self.l6.place(x=700,y=300)
                        self.dis6  = Label(self.master,font="Helvetica 14 bold",bd=2,text=i[8])
                        self.dis6.place(x=940,y=310)
                        
                        self.l7 = Label(self.master,text="ALTERNATE CONTACT",font="Helvetica 14 bold", bd=22)
                        self.l7.place(x=100,y=400)
                        self.dis7  = Label(self.master,font="Helvetica 14 bold",bd=2,text=i[9])
                        self.dis7.place(x=400,y=415)
                        
                        self.l8 = Label(self.master,text="EMAIL",font="Helvetica 14 bold", bd=22)
                        self.l8.place(x=700,y=400)
                        self.dis8  = Label(self.master,font="Helvetica 14 bold",bd=2,text=i[7])
                        self.dis8.place(x=900,y=410)

                        self.l9 = Label(self.master,text="CONSULTING TEAM / DOCTOR",font="Helvetica 14 bold", bd=22)
                        self.l9.place(x=100,y=500)
                        self.dis9  = Label(self.master,font="Helvetica 14 bold",bd=2,text=i[6])
                        self.dis9.place(x=450,y=515)

                        self.l10 = Label(self.master,text="ADDRESS",font="Helvetica 14 bold", bd=22)
                        self.l10.place(x=700,y=500)
                        self.dis10 = Label(self.master,font="Helvetica 14 bold",bd=2,text=i[5])
                        self.dis10.place(x=900,y=510)
                        


    
        
    #FUNCTION TO SEARCH DATA IN PATIENT FORM
    def GSEARCH_PAT(self):
        global inp_s,g_pid,errorS,t,i,q,dis1,dis2,dis3,dis4,dis5,dis6,dis7,dis8,dis9,dis10,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10
        c1=conn.cursor()
        inp_s=(self.g_pid.get())                
        p=list(conn.execute('select * from PATIENT where EMAIL=?',(inp_s,)))
        if (len(p)==0):
            tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM","PATIENT RECORD NOT FOUND")
                    
        else:
            t=c1.execute('SELECT * FROM PATIENT where EMAIL=?',(inp_s,));
            for i in t:
                        self.l1 = Label(self.master,text="PATIENT ID",font="Helvetica 14 bold", bd=22)
                        self.l1.place(x=100,y=100)
                        self.dis1= Label(self.master,font="Helvetica 14 bold",bd=2,text=i[0])
                        self.dis1.place(x=320,y=115)
                        
                        self.l2 = Label(self.master,text="PATIENT NAME",font="Helvetica 14 bold", bd=22)
                        self.l2.place(x=700,y=100)
                        self.dis2=Label(self.master,font="Helvetica 14 bold",bd=2,text=i[1])
                        self.dis2.place(x=900,y=110)

                        self.l3 = Label(self.master,text="SEX",font="Helvetica 14 bold", bd=22)
                        self.l3.place(x=100,y=200)
                        self.dis3  =Label(self.master,font="Helvetica 14 bold",bd=2,text=i[2])
                        self.dis3.place(x=200,y=220)

                        self.l4 = Label(self.master,text="DOB (YYYY-MM-DD)",font="Helvetica 14 bold", bd=22)
                        self.l4.place(x=700,y=200)
                        self.dis4=Label(self.master,font="Helvetica 14 bold",bd=2,text=i[4])
                        self.dis4.place(x=940,y=210)
                        
                        self.l5 = Label(self.master,text="BLOOD GROUP",font="Helvetica 14 bold", bd=22)
                        self.l5.place(x=100,y=300)
                        self.dis5 =Label(self.master,font="Helvetica 14 bold",bd=2,text=i[3])
                        self.dis5.place(x=300,y=320)
                        '''
                        #self.l6 = Label(self.master,text="CONTACT NUMBER",font="Helvetica 14 bold", bd=22)
                        #self.l6.place(x=700,y=300)
                        self.dis6  = Label(self.master,font="Helvetica 14 bold",bd=2,text=i[8])
                        self.dis6.place(x=940,y=310)
                        
                        self.l7 = Label(self.master,text="ALTERNATE CONTACT",font="Helvetica 14 bold", bd=22)
                        self.l7.place(x=100,y=400)
                        self.dis7  = Label(self.master,font="Helvetica 14 bold",bd=2,text=i[9])
                        self.dis7.place(x=400,y=415)
                        '''
                        self.l8 = Label(self.master,text="EMAIL",font="Helvetica 14 bold", bd=22)
                        self.l8.place(x=700,y=400)
                        self.dis8  = Label(self.master,font="Helvetica 14 bold",bd=2,text=i[7])
                        self.dis8.place(x=900,y=410)

                        self.l9 = Label(self.master,text="CONSULTING TEAM / DOCTOR",font="Helvetica 14 bold", bd=22)
                        self.l9.place(x=100,y=500)
                        self.dis9  = Label(self.master,font="Helvetica 14 bold",bd=2,text=i[6])
                        self.dis9.place(x=450,y=515)

                        self.l10 = Label(self.master,text="ADDRESS",font="Helvetica 14 bold", bd=22)
                        self.l10.place(x=700,y=500)
                        self.dis10 = Label(self.master,font="Helvetica 14 bold",bd=2,text=i[5])
                        self.dis10.place(x=900,y=510)
