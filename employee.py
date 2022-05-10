from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
import sqlite3
from PIL import ImageTk,Image

conn=sqlite3.connect("HospitalDB.db")
print("DATABASE CONNECTION SUCCESSFUL")

#Class for EMPLOYEE REGISTRATION 
class Employee:
    def __init__(self,master):
        self.master = master
        
        self.master.title("MONORAMA HOSPITAL")
        self.master.iconbitmap("download.ico")
        self.master.geometry("1500x700+0+0")
        #self.master.config(bg="sky blue")
        #self.master = Frame(self.master,bg="sky blue")
        #self.master.pack()
        
        self.image=ImageTk.PhotoImage(Image.open("manor.png"))
        self.panel=Label(master,image=self.image)
        self.panel.pack()
        #=============ATTRIBUTES===========
        
        self.emp_ID=StringVar()
        self.emp_name=StringVar()
        self.emp_sex=StringVar()
        self.emp_age=IntVar()
        self.emp_type=StringVar()
        self.emp_salary=IntVar()
        self.emp_exp=StringVar()
        self.emp_email=StringVar()
        self.emp_phno=IntVar()


        #===============TITLE==========
        self.lblTitle = Label(self.master,text = "EMPLOYEE REGISTRATION FORM", font="Helvetica 20 bold",bg="sky blue")
        self.lblTitle.place(x =400 ,y = 30)
        #==============FRAME==========
        #self.master = Frame(self.master,width=400,height=80,relief="ridge",bg="sky blue",bd=20)
        #self.master.place(x=1,y=0)
        
        #self.master2 = Frame(self.master,width=400,height=80,relief="ridge",bg="sky blue",bd=20)
        #self.master2.place(x=2,y=0)
        #===========LABELS=============          
        self.lblempid = Label(self.master,text="EMPLOYEE ID",font="Helvetica 14 bold",bd=22)
        self.lblempid.place(x=100,y=100)
        self.lblempid  = Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable= self.emp_ID)
        self.lblempid.place(x=300,y=115)
        
        self.lblempname = Label(self.master,text="EMPLOYEE NAME",font="Helvetica 14 bold",bd=22)
        self.lblempname.place(x=700,y=100)
        self.lblempname  = Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable= self.emp_name)
        self.lblempname.place(x=920,y=115)

        self.lblsex = Label(self.master,text="SEX",font="Helvetica 14 bold",bd=22)
        self.lblsex.place(x=100,y=200)
        self.etype1 =Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable= self.emp_sex)
        self.etype1.place(x=300,y=215)
        

        self.lblage = Label(self.master,text="AGE",font="Helvetica 14 bold",bd=22)
        self.lblage.place(x=700,y=200)
        self.lblage  = Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable= self.emp_age)
        self.lblage.place(x=900,y=215)
        
        self.etype1=Label(self.master,text="EMPLOYEE DESIGNATION",font="Helvetica 14 bold",bd=22)
        self.etype1.place(x=100,y=300)
        self.etype1 =Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable= self.emp_type)
        self.etype1.place(x=370,y=315)

        self.lblCon = Label(self.master,text="SALARY",font="Helvetica 14 bold",bd=22)
        self.lblCon.place(x=700,y=300)
        self.lblCon  = Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable= self.emp_salary)
        self.lblCon.place(x=900,y=315)
        
        self.lblAlt = Label(self.master,text="EXPERIENCE",font="Helvetica 14 bold",bd=22)
        self.lblAlt.place(x=100,y=400)
        self.lblAlt  = Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable= self.emp_exp)
        self.lblAlt.place(x=300,y=415)
        
        self.lbleid = Label(self.master,text="CONTACT NUMBER",font="Helvetica 14 bold",bd=22)
        self.lbleid.place(x=700,y=400)
        self.lbleid  = Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable= self.emp_phno)
        self.lbleid.place(x=920,y=415)
        
        self.lbleid = Label(self.master,text="EMAIL",font="Helvetica 14 bold",bd=22)
        self.lbleid.place(x=100,y=500)
        self.lbleid  = Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable= self.emp_email)
        self.lbleid.place(x=300,y=515)

        self.button2 = Button(self.master, text="SAVE",width =10,font="Helvetica 14 bold",command = self.INSERT_EMP)
        self.button2.place(x=100,y=620)
        
        self.button3 = Button(self.master, text="DELETE",width =10,font="Helvetica 14 bold",command= self.DE_DISPLAY)
        self.button3.place(x=300,y=620)
     
        self.button6 = Button(self.master, text="EXIT",width =10,font="Helvetica 14 bold",command = self.Exit)
        self.button6.place(x=500,y=620)
        

   #FUNCTION TO EXIT PATIENT FORM
    def Exit(self):            
        self.master.destroy()
        
    #FUNCTION TO INSERT DATA IN EMPLOYEE FORM
        
    def INSERT_EMP(self):
        global e1,e2,e3,e4,e5,e6,e7,e8,e9,var
        e1=(self.emp_ID.get())
        e2=(self.emp_name.get())
        e3=(self.emp_sex.get())
        e4=(self.emp_age.get())
        e5=(self.emp_type.get())
        e6=(self.emp_salary.get())
        e7=(self.emp_exp.get())
        e8=(self.emp_email.get())
        e9=(self.emp_phno.get())
        conn = sqlite3.connect("HospitalDB.db")     
        p = list(conn.execute("SELECT * FROM employee  WHERE EMP_ID =?",(e1,)))
        x=len(p)
        if x!=0:
             tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM", "EMPLOYEE ID ALREADY EXISTS")     
        else:
            conn.execute("INSERT INTO employee VALUES(?,?,?,?,?,?,?,?,?)",(e1,e2,e3,e4,e5,e6,e7,e8,e9,))
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "EMPLOYEE DATA ADDED")
        conn.commit()
                
    #FUNCTION TO OPEN DELETE PATIENT DISPLAY WINDOW
    def DE_DISPLAY(self):
        self.newWindow = Toplevel(self.master)
        self.app = D_EMP(self.newWindow)


#CLASS FOR DISPLAY MENU FOR DELETE EMPLOYEE
class D_EMP:
    def __init__(self,master):    
        global de1_emp,de
        self.master = master
        
        self.master.title("MONORAMA HOSPITAL")
        self.master.iconbitmap("download.ico")
        self.master.geometry("1500x700+0+0")
        
        self.image=ImageTk.PhotoImage(Image.open("manor.png"))
        self.panel=Label(master,image=self.image)
        self.panel.pack()
        #self.master.config(bg="sky blue")
        #self.master = Frame(self.master,bg="sky blue")
        # self.master.pack()
        self.de1_emp=StringVar()
        self.lblTitle = Label(self.master,text = "DELETE EMPLOYEE WINDOW", font="Helvetica 20 bold",bg="sky blue")
        self.lblTitle.place(x =450 ,y =10)
        #==============FRAME==========
        #self.master = Frame(self.master,width=400,height=80,relief="ridge",bg="sky blue",bd=20)
        #self.master.place(x=1,y=0)
        #self.master2 = Frame(self.master,width=400,height=80,relief="ridge",bg="sky blue",bd=20)
        #self.master2.place(x=2,y=0)
        #===========LABELS=============          
        self.lblpatid = Label(self.master,text="ENTER EMPLOYEE ID TO DELETE",font="Helvetica 14 bold",bd=22)
        self.lblpatid.place(x=100,y=200)
        self.lblpatid= Entry(self.master,font="Helvetica 14 bold",bd=2,textvariable= self.de1_emp)
        self.lblpatid.place(x=600,y=210)

        self.DeleteB = Button(self.master, text="DELETE",width =10,font="Helvetica 14 bold",command = self.DELETE_EMP)
        self.DeleteB.place(x=650,y=350)
        
    #FUNCTION TO DELETE DATA IN EMPLOYEE FORM 
    def DELETE_EMP(self):        
        global inp_d
        de = str(self.de1_emp.get())
        conn = sqlite3.connect("HospitalDB.db")
        p = list(conn.execute("select * from employee where EMP_ID=?", (de,)))
        if (len(p) != 0):
            conn.execute("DELETE from employee where EMP_ID=?", (de,))
            dme = tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "EMPLOYEE DATA DELETED")
            
        else:
            error = tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", "EMPLOYEE DATA DOESN'T EXIST")
        conn.commit()   
