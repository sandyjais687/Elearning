from tkinter import *
from tkinter import messagebox
import sqlite3
def profileWindow(username1):
    mydb= sqlite3.connect("elearning.db")
    cur=mydb.cursor()
    profilewindow=Toplevel()
    profilewindow.geometry("400x400")
    profilewindow.configure(bg="sky blue")
    profileimg=PhotoImage(file="images/profile.png")
     
    def updt():
        try:            
            cur.execute('''update userpass set name="%s" where username="%s"''' %(varname.get(), username1))
            cur.execute('''update userpass set mob="%d" where username="%s"''' %(int(varmob.get()), username1))
            cur.execute('''update userpass set passwd="%s" where username="%s"''' %(varpass.get(), username1))
            mydb.commit() 
        except ValueError:
            messagebox.showerror("Error", "Enter Mobile Number Properly > : (")
        else:
            messagebox.showinfo("Updated", "Updated SuccessFully.")
    
    cur.execute("select name from userpass where username='%s'" %(username1))
    a=cur.fetchone()
    a=str(a).strip("(").strip(")").strip(",").strip("'")
    cur.execute("select username from userpass where username='%s'" %(username1))
    b=cur.fetchone()
    b=str(b).strip("(").strip(")").strip(",").strip("'")
    cur.execute("select mob from userpass where username='%s'" %(username1))
    c=cur.fetchone()
    c=str(c).strip("(").strip(")").strip(",").strip("'")
    cur.execute("select passwd from userpass where username='%s'" %(username1))
    d=cur.fetchone()
    d=str(d).strip("(").strip(")").strip(",").strip("'")

    
    lblname=Label(profilewindow, text="Name", bg="sky blue", font=("Georgia 14"))
    lblname.place(x=10, y=20)

    varname=StringVar()
    ename=Entry(profilewindow, textvar=varname, width=30).place(x=150, y=20)
    
    lbluser=Label(profilewindow, text="UserName", bg="sky blue", font=("Georgia 14"))
    lbluser.place(x=10, y=70)

    #varuser=StringVar()
    euser=Label(profilewindow, bg="sky blue")
    euser.place(x=150, y=70)
    euser.config(text=username1)

    
    lblmob=Label(profilewindow, text="Mobile", bg="sky blue", font=("Georgia 14"))
    lblmob.place(x=10, y=120)
    varmob=StringVar()
    emob=Entry(profilewindow, textvar=varmob, width=30).place(x=150, y=120)


    lblpass=Label(profilewindow, text="Password", bg="sky blue", font=("Georgia 14"))
    lblpass.place(x=10, y=170)
    
    varpass=StringVar()
    epass=Entry(profilewindow, textvar=varpass, width=30).place(x=150, y=170)

    btnupdt=Button(profilewindow, text="Update", bg="silver", command=updt).place(x=150, y=220)

    varname.set(a)
    varpass.set(d)
    #varuser.set(b)
    varmob.set(c)
    
    profilewindow.mainloop()
