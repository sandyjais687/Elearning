import logging
from tkinter import *
from tkinter import messagebox
import time

import sqlite3

import course
from course import *

import Aptitude
from Aptitude import *

import profile
from profile import *

import about
from about import *

mydb=sqlite3.connect("elearning.db")
cur=mydb.cursor()

format="%(asctime)s : %(message)s"
logging.basicConfig(format=format,level=logging.INFO,filename="ProjectLog.log",filemode="w",datefmt="%D, %H:%M:%S")

root=Tk()
root.geometry('300x450')
root.configure(bg="cadetblue1")
varusername=StringVar() #Signup username
varpasswd=StringVar()#Signup password
varname=StringVar() #Signup name
varmob=StringVar() #Signup mob

var3=StringVar()#login username
var4=StringVar()#login passwd
bgclr="cadetblue1"

signupimg=PhotoImage(file=r"images/signup.png")
loginimg=PhotoImage(file=r"images/login.png")
logo=PhotoImage(file=r"images/python.png")
aboutimg=PhotoImage(file=r"images/about.png")


#***************Signup window Starts From here*******************
def signup():
    root.withdraw()
    logging.info("Project: SingUP Page Opened.")

    def SignupFunction():   #Signup Function
        logging.info("Project: SingUP Function Called.")
        try:
            a=varname.get()
            b=int(varmob.get())
            c=varusername.get()
            d=varpasswd.get()
            cur.execute("create table if not exists userpass(name varchar(30), mob int(11),username varchar(15) primary key not null, passwd varchar(15) not null, marks int)")
            if a!='' and c!='' and d!='':
                if len(str(b))==10 and b!=1234567890 and b!=0000000000 and b!=1111111111:
                    cur.execute('''insert into userpass(name, mob, username, passwd) values('%s','%d','%s', '%s')''' %(a,b,c,d))
                    mydb.commit()
                    messagebox.showinfo("Singup", "SingedUp SuccessFully.")
                    varusername.set("")
                    varpasswd.set("")
                    varname.set("")
                    varmob.set("")
                else:
                    messagebox.showerror("Mobile", "Enter VALID Mobile Number, All Fields are Complusary ")
            else:
                messagebox.showerror("Field","All Fields are Complusory ")
        except ValueError:
            messagebox.showerror("Error", "Enter Mobile Number Properly >:(")
            
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username Already Exist, Use another.")
            
    #SignupWindowDesign
    root1=Toplevel()
    root1.configure(bg="cadetblue1")
    root1.geometry('300x300')
    Label(root1, text="Name:",bg=bgclr, font=("Segoe ui", 12)).place(x=20, y=20)
    e=Entry(root1, textvar=varname, width=30).place(x=100, y=20)
    Label(root1, text="UserName:",bg=bgclr, font=("Segoe ui", 11)).place(x=20, y=50)
    e2=Entry(root1, textvar=varusername, width=30).place(x=100, y=50)
    Label(root1, text="Password:",bg=bgclr, font=("Segoe ui", 12)).place(x=20, y=80)
    e3=Entry(root1, textvar=varpasswd, width=30).place(x=100, y=80)
    Label(root1, text="Mobile:",bg=bgclr, font=("Segoe ui", 12)).place(x=20, y=120)
    e4=Entry(root1, textvar=varmob, width=30).place(x=100, y=120)
    b1=Button(root1, command=SignupFunction, image=signupimg, bg="cadetblue1", relief=FLAT).place(x=100, y=170)
    b2=Button(root1,command=lambda:[root.deiconify(), root1.destroy()], text="Back", bg="red").place(x=70, y=250)
    root1.mainloop()

#***************Signup window Ends here*******************





#***************Login window Starts From here*******************
def login():
    root.withdraw()
    logging.info("Project: Login Page Opened.")

    
    def LoginFunction():
        logging.info("Project: Login Function Called.")
        userVar=var3.get()
        passwdVar=var4.get()
        #print(userVar)
        ##print(passwdVar)
        cur.execute('''select username from userpass where username="%s"''' %(userVar))
        usernameget=cur.fetchone()
        usernameget=str(usernameget).strip("(").strip(")").strip(",").strip("'")
        print(usernameget)
        
        cur.execute('''select passwd from userpass where username="%s"''' %(userVar))
        passwdget=cur.fetchone()
        passwdget=str(passwdget).strip("(").strip(")").strip(",").strip("'")
        print(passwdget)
        mydb.commit()

        if userVar==usernameget and passwdVar==passwdget:
            logging.info("Project: Login Authentication Successful.")
            #Popen('python DocFrame.py')
            afterlogin=Toplevel()
            root2.withdraw()
            afterlogin.geometry("785x500")
            afterlogin.configure(bg="sky blue")
            courseimg=PhotoImage(file="images/course.png")
            profileimg=PhotoImage(file="images/profile.png")
            quizimg=PhotoImage(file="images/quiz.png")

            lblwlcm=Label(afterlogin, text="Welcome '" +userVar+ "' to Python E-learning\nPlease complete below course then try yourself.", bg="sky blue", font=("Georgia 20"))
            lblwlcm.pack()
            
            coursebtn=Button(afterlogin, image=courseimg, relief=FLAT, bg="sky blue", command=framing).place(x=50, y=250)

            def profileshow():
                profileWindow(usernameget)
            
            profilebtn=Button(afterlogin, image=profileimg, relief=FLAT, bg="sky blue", command=profileshow).place(x=300, y=250)
            quizbtn=Button(afterlogin, image=quizimg, relief=FLAT, bg="sky blue", command=Apti).place(x=550, y=250)
            
            logoutbtn=Button(afterlogin, text="LogOut",fg="Blue", relief=RIDGE, bg="sky blue", command=lambda:[afterlogin.destroy(),root.deiconify()]).place(x=600, y=150)
            quitbtn=Button(afterlogin, text="Quit",fg="red", relief=RIDGE, bg="sky blue", command=root.destroy).place(x=670, y=150)
            afterlogin.mainloop()


        else:
            #errLabel.config(text="Enter Credentials Properly")
            messagebox.showerror("Error", "Enter Proper Credentials.")

    #Login Window Design
    root2=Toplevel()
    root2.geometry('300x300')
    root2.configure(bg=bgclr)
    Label(root2, text="username:",bg=bgclr, font=("Segoe ui", 14)).pack()
    e3=Entry(root2, textvar=var3, width=30).pack()
    Label(root2, text="password:",bg=bgclr, font=("Segoe ui", 14)).pack()
    e4=Entry(root2, textvar=var4,show="*", width=30).pack()
    errLabel=Label(root2, fg="Red", bg=bgclr)
    errLabel.place(x=70, y=110) #Error in wrong credential here.
    b1=Button(root2,command=LoginFunction, image=loginimg, bg=bgclr, relief=FLAT).place(x=70, y=150)
    b2=Button(root2,command=lambda:[root.deiconify(), root2.destroy()], text="Back", bg="Red").place(x=70, y=250)

    root2.mainloop()
#***************Login WIndow Ends Here*********************


l1=Label(root, text="Welcome To",bg="cadetblue1", font=("Segoe ui black", 20)).pack()
l2=Label(root, text="Python E-Learning Portal.",bg="cadetblue1", font=("Segoe ui black" ,17)).pack()
l3=Label(root, image=logo, bg='cadetblue1').pack()
b1=Button(root, command=signup, image=signupimg, bg="cadetblue1", relief=FLAT).place(x=70, y=250)
b2=Button(root, command=login, image=loginimg, bg="cadetblue1", relief=FLAT).place(x=70, y=315)
b3=Button(root, command=aboutpage, image=aboutimg, bg="cadetblue1", relief=FLAT).place(x=70, y=380)
logging.info("Project: Main Window Executed.")
root.mainloop()
