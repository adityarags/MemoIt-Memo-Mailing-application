import tkinter as tk                
from tkinter import font as tkfont
from tkinter.constants import END  
from PIL import ImageTk,Image
import databaseconnection as dbconnect
import sys
import subprocess
from emailsenderapp import sendMemo

RECIPIENT = " "


class StartPage(tk.Frame):  

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        imgs = ImageTk.PhotoImage(Image.open("PageLogo.png"))
        Label1 = tk.Label(self,image=imgs)
        Label1.image=imgs
        Label1.grid(row=1,column=0,columnspan=2)
        Label3 = tk.Label(self,text="Password:")
        Label3.grid(row=2,column=0)
        self.Entry2 = tk.Entry(self,show='*')
        self.Entry2.grid(row = 2,column= 1)
        Button1 = tk.Button(self,text="Submit",command =lambda: self.checkpswd(self.Entry2.get())).grid(row=3,column=0,columnspan=2)
        Label4 = tk.Label(self,text = "Thank You for Using Our Services!").grid(row=4,column=0,columnspan=2)
    
    def checkpswd(self,pswd):
        self.Entry2.delete(0,END)
        f = open("Passwords.txt")
        password = f.readlines()[2].strip('\n')
        if pswd == password:
            _connectionDetail = dbconnect.login_to_database().is_connected()
            if _connectionDetail:
                print("Connected To Database!")
            else:
                return self.controller.showFrame("WrongPasswordPage")
            
            return self.controller.showFrame("PageOne")
            
        else:
            self.controller.showFrame("WrongPasswordPage")

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        imgs = ImageTk.PhotoImage(Image.open("PageLogo.png"))
        Label1 = tk.Label(self,image=imgs)
        Label1.image=imgs
        Label1.grid(row=1,column=0,columnspan=2)
        
        Button1 = tk.Button(self,text="Send Memo",command =lambda: controller.showFrame("PageTwo")).grid(row=2,column=0,columnspan=2)
        Button2 = tk.Button(self,text="Add New Employee",command =lambda: controller.showFrame("PageThree")).grid(row=3,column=0,columnspan=2)
        Button3 = tk.Button(self,text="Log Out",command =lambda: controller.showFrame("StartPage")).grid(row=4,column=0,columnspan=2)
        Label4 = tk.Label(self,text = "Thank You for Using Our Services!").grid(row=5,column=0,columnspan=2)
    

class WrongPasswordPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="WRONG PASSWORD!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.showFrame("StartPage"))
        button.pack()



class PageTwo(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Employees = dbconnect.getemployees()
        if Employees == []:
            Employees = [' ']
        imgs = ImageTk.PhotoImage(Image.open("PageLogo.png"))
        Label1 = tk.Label(self,image=imgs)
        Label1.image=imgs
        Label1.grid(row=1,column=0,columnspan=2)
        clicked = tk.StringVar(self)
        clicked.set(Employees[0])
        companyName = tk.OptionMenu(self,clicked,*Employees).grid(row = 2,column=0,rowspan=2)
        button = tk.Button(self, text="Enter",
                           command=lambda: self.setEmailReciever(controller,clicked.get())).grid(row = 4,column = 0,rowspan=2)
        button2 = tk.Button(self, text="Go Back",
                           command=lambda: controller.showFrame("PageOne")).grid(row = 6,column = 0,rowspan=2)
        Label4 = tk.Label(self,text = "Thank You for Using Our Services!").grid(row=8,column=0,columnspan=2)
    
    def setEmailReciever(self,controller,recipient):
        global RECIPIENT
        idindex = recipient.index(':')
        RECIPIENT = recipient[:idindex]
        controller.showFrame("PageFour")
    

class PageThree(tk.Frame):
    
    def __init__(self, parent, controller):
        self.p = parent;self.c = controller
        tk.Frame.__init__(self, parent)
        imgs = ImageTk.PhotoImage(Image.open("PageLogo.png"))
        Label1 = tk.Label(self,image=imgs)
        Label1.image=imgs
        Label1.grid(row=1,column=0,columnspan=2)
        Label2 = tk.Label(self,text="Employee ID:")
        Label2.grid(row=2,column=0)
        self.Entry2 = tk.Entry(self)
        self.Entry2.grid(row = 2,column= 1)
        Label3 = tk.Label(self,text="Employee Name:")
        Label3.grid(row=3,column=0)
        self.Entry3 = tk.Entry(self)
        self.Entry3.grid(row = 3,column= 1)
        Label4 = tk.Label(self,text="Employee Email:")
        Label4.grid(row=4,column=0)
        self.Entry4 = tk.Entry(self)
        self.Entry4.grid(row = 4,column= 1)
        Button1 = tk.Button(self,text="Submit",command =lambda: self.sendtodb(self.Entry2.get(),self.Entry3.get(),self.Entry4.get())).grid(row=5,column=0,columnspan=2)
        Button2 = tk.Button(self,text="Go Back",command =lambda: controller.showFrame("PageOne")).grid(row=6,column=0,columnspan=2)

    def sendtodb(self,id,name,email):
        x = dbconnect.updatevals(id,name,email)
        if x:
            self.Entry2.delete(0,END)
            self.Entry3.delete(0,END)
            self.Entry4.delete(0,END)
            subprocess.Popen(["py", "MainApp.py"])
            sys.exit()

            
class PageFour(tk.Frame):
    def __init__(self, parent, controller):
        self.p = parent;self.c = controller
        tk.Frame.__init__(self, parent)
        imgs = ImageTk.PhotoImage(Image.open("PageLogoLarge.png"))
        Label1 = tk.Label(self,image=imgs)
        Label1.image=imgs
        Label1.grid(row=1,column=0,columnspan=2)
        Label2 = tk.Label(self,text="Subject")
        Label2.grid(row=2,column=0)
        self.Entry2 = tk.Text(self,width = 50,height = 1)
        self.Entry2.grid(row = 2,column= 1)
        Label3 = tk.Label(self,text="Type a Memo")
        Label3.grid(row=3,column=0)
        self.Entry3 = tk.Text(self,height=10)
        self.Entry3.grid(row = 3,column= 1)
        Button1 = tk.Button(self,text="Send Mail",command =lambda:sendingTheMemo(self.Entry2.get(1.0,END),self.Entry3.get(1.0,END),controller)).grid(row=6,column=0,columnspan=2)
        Button2 = tk.Button(self,text="Go Back",command =lambda:controller.showFrame("PageTwo")).grid(row=7,column=0,columnspan=2)

def sendingTheMemo(subject,body,controller):
    to = dbconnect.getRecipientEmail(RECIPIENT)
    sendMemo(to,subject,body)
    controller.showFrame("PageTwo")


