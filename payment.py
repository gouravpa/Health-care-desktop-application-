

from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
import sqlite3
from PIL import ImageTk,Image
from tkinter import messagebox
    

#Class for BILLING  
class Payment:
    def pay(self,master):
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
        
                
        #===============TITLE==========
        self.lblTitle = Label(self.master,text = "PAYMENT WINDOW", font="Helvetica 20 bold",bg="sky blue")
        self.lblTitle.place(x =350,y = 10)


        self.b=Button(self.master,text="Pay Now",command=self.show())
        self.b.place(x=100,y=400)



        def show(self):
            messagebox.showinfo("information","Payment Method Is Not Available For Now")
        #==============master==========




    

    

        
        

