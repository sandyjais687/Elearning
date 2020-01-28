import smtplib 
import logging
import time
from tkinter import *
from tkinter import messagebox

format="%(asctime)s : %(message)s"
logging.basicConfig(format=format,level=logging.INFO,filename="ProjectLog.log", filemode="w",datefmt="%D, %H:%M:%S")


def aboutpage():
    logging.info("Project: About Page Opened.")
    def mailsend():
        useremail=emailentry.get()
        userpassword=passwordentry.get()
        msg=text.get("1.0", END)
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls() 
        s.login(useremail,userpassword)
        s.sendmail(useremail, "sandyjais687@gmail.com", msg) 
        s.quit()
        messagebox.showinfo("Email", "Email Sent Successfully")
        logging.info("About: Mail Sent to Developer.")
        
    abtwin=Toplevel()
    abtwin.geometry("620x400")
    myself=PhotoImage(file=r"images/me.png")

    lbl1=Label(abtwin, text="Developers Info.", fg="Red", font=("Times 14")).place(x=75, y=5)
    melbl=Label(abtwin, image=myself).place(x=60, y=30)

    lbl1=Label(abtwin, text="Name :", fg="Red", font=("Times 14")).place(x=20, y=250)
    lbl2=Label(abtwin, text="Contact :", fg="Red", font=("Times 14")).place(x=20, y=290)
    lbl3=Label(abtwin, text="Email :", fg="Red", font=("Times 14")).place(x=20, y=330)
    lbl4=Label(abtwin, text="Facebook:", fg="Red", font=("Times 14")).place(x=20, y=370)

    lbl11=Label(abtwin, text="Sudhir Jaiswar", fg="blue", font=("Times 14")).place(x=105, y=250)
    lbl12=Label(abtwin, text="8652621752", fg="blue", font=("Times 14")).place(x=105, y=290)
    lbl13=Label(abtwin, text="sandyjais687@outlook.com", fg="blue", font=("Times 14")).place(x=105, y=330)
    lbl14=Label(abtwin, text="facebook.com/sandyjais687", fg="blue", font=("Times 14")).place(x=105, y=370)

    lblemail=Label(abtwin, text="Email :", font=("Times 12")).place(x=330, y=50)
    emailentry=Entry(abtwin, width=32)
    emailentry.place(x=410, y=50)
    lblpasswd=Label(abtwin, text="Password :", font=("Times 12")).place(x=330, y=100)
    passwordentry=Entry(abtwin, width=32,show="*")
    passwordentry.place(x=410, y=100)
    lblmsg=Label(abtwin, text="Message :", font=("Times 12")).place(x=330, y=150)
    text=Text(abtwin, height=5, width=24)
    text.place(x=410, y=150)
    sendmail=Button(abtwin, text="Send Email", bg="Light Green", command=mailsend).place(x=410, y=270)
    abtwin.mainloop()
