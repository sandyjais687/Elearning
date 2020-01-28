import logging
import time
from tkinter import *
from tkdocviewer import *
format="%(asctime)s : %(message)s"
logging.basicConfig(format=format,level=logging.INFO,filename="ProjectLog.log",filemode="w",datefmt="%D, %H:%M:%S")

def framing():
    logging.info("Login: Course Function Called.")    
    def Introduction():
        f2=Frame(root)
        f2.place(x=80, y=0)
        logging.info("Topic: Introduction Topic Opened.")
        v = DocViewer(f2, width=830, height=700) 
        v.pack()
        v.display_file("docs/1.whatIsPython.pdf")

    def Basic():
        f3=Frame(root)
        f3.place(x=80, y=0)
        logging.info("Topic: Basics Topic Opened.")
        v1 = DocViewer(f3, width=830, height=700) 
        v1.pack()
        v1.display_file("docs/2.Basic Syntax.pdf")
        
    def Variables():
        f4=Frame(root)
        f4.place(x=80, y=0)
        logging.info("Topic: Variable Topic Opened.")
        v = DocViewer(f4, width=830, height=700) 
        v.pack()
        v.display_file("docs/3.Variables.pdf")
        
    def IfElse():
        f5=Frame(root)
        f5.place(x=80, y=0)
        logging.info("Topic: Conditions If-Else Topic Opened.")
        v = DocViewer(f5, width=830, height=700) 
        v.pack()
        v.display_file("docs/4.Decision making If-Else.pdf")
        
    def Loops():
        f6=Frame(root)
        f6.place(x=80, y=0)
        logging.info("Topic: Loops Topic Opened.")
        v = DocViewer(f6, width=830, height=700) 
        v.pack()
        v.display_file("docs/5.Loops.pdf")
        
    def Number():
        f7=Frame(root)
        f7.place(x=80, y=0)
        logging.info("Topic: Number Topic Opened.")
        v = DocViewer(f7, width=830, height=700) 
        v.pack()
        v.display_file("docs/6.Number.pdf")
        
    def String():
        f8=Frame(root)
        f8.place(x=80, y=0)
        logging.info("Topic: String Topic Opened.")
        v = DocViewer(f8, width=830, height=700) 
        v.pack()
        v.display_file("docs/7.String.pdf")
        
    def List():
        f9=Frame(root)
        f9.place(x=80, y=0)
        logging.info("Topic: List Topic Opened.")
        v = DocViewer(f9, width=830, height=700) 
        v.pack()
        v.display_file("docs/8.List.pdf")

    def Tuple():
        f10=Frame(root)
        f10.place(x=80, y=0)
        logging.info("Topic: Tuple Topic Opened.")
        v = DocViewer(f10, width=830, height=700) 
        v.pack()
        v.display_file("docs/9.Tuple.pdf")

    def Dictionary():
        f11=Frame(root)
        f11.place(x=80, y=0)
        logging.info("Topic: Dictionary Topic Opened.")
        v = DocViewer(f11, width=830, height=700) 
        v.pack()
        v.display_file("docs/10.Dictionary.pdf")

    def Functions():
        f12=Frame(root)
        f12.place(x=80, y=0)
        logging.info("Topic: Functions Topic Opened.")
        v = DocViewer(f12, width=830, height=700) 
        v.pack()
        v.display_file("docs/11.Functions.pdf")

    def Modules():
        f13=Frame(root)
        f13.place(x=80, y=0)
        logging.info("Topic: Modules And Packages Topic Opened.")
        v = DocViewer(f13, width=830, height=700) 
        v.pack()
        v.display_file("docs/12.Modules And Packages.pdf")

    def FileOperation():
        f14=Frame(root)
        f14.place(x=80, y=0)
        logging.info("Topic: File I/O operation Topic Opened.")
        v = DocViewer(f14, width=830, height=700) 
        v.pack()
        v.display_file("docs/13.File IO.pdf")

    def ExceptionHandeling():
        f15=Frame(root)
        f15.place(x=80, y=0)
        logging.info("Topic: Exception Handeling Topic Opened.")
        v = DocViewer(f15, width=830, height=700) 
        v.pack()
        v.display_file("docs/14.ExceptionHandeling.pdf")

    def OOPS():
        f16=Frame(root)
        f16.place(x=80, y=0)
        logging.info("Topic: OOPS Topic Opened.")
        v = DocViewer(f16, width=830, height=700) 
        v.pack()
        v.display_file("docs/15.OOPS.pdf")

    def Mysql():
        f17=Frame(root)
        f17.place(x=80, y=0)
        logging.info("Topic: Introduction Topic Opened.")
        v = DocViewer(f17, width=830, height=700) 
        v.pack()
        v.display_file("docs/16.Mysql DB.pdf")

    def Networking():
        f18=Frame(root)
        f18.place(x=80, y=0)
        logging.info("Topic: Networking Topic Opened.")
        v = DocViewer(f18, width=830, height=700) 
        v.pack()
        v.display_file("docs/17.Networking.pdf")

    def Email():
        f19=Frame(root)
        f19.place(x=80, y=0)
        logging.info("Topic: Email Topic Opened.")
        v = DocViewer(f19, width=830, height=700) 
        v.pack()
        v.display_file("docs/18.Email sending.pdf")

    def Multithreading():
        f20=Frame(root)
        f20.place(x=80, y=0)
        logging.info("Topic: Multithreading Topic Opened.")
        v = DocViewer(f20, width=830, height=700) 
        v.pack()
        v.display_file("docs/19.Multithreaded.pdf")

    def GUI():
        f21=Frame(root)
        f21.place(x=80, y=0)
        logging.info("Topic: GUI Topic Opened.")
        v = DocViewer(f21, width=830, height=700) 
        v.pack()
        v.display_file("docs/tkinter.pdf")



    root=Toplevel()
    root.geometry('950x700')

    f1=Frame(root)
    f1.place(x=0, y=0)
    
    l1=Button(f1, text="Introduction",width=10, command=Introduction)
    l1.pack()
    
    l2=Button(f1, text="Basic",width=10, command=Basic)
    l2.pack()
    
    l3=Button(f1, text="Variables",width=10, command=Variables)
    l3.pack()
    
    l4=Button(f1, text="If-Else",width=10, command=IfElse)
    l4.pack()
    
    l5=Button(f1, text="Loops",width=10, command=Loops)
    l5.pack()
    
    l6=Button(f1, text="Number",width=10, command=Number)
    l6.pack()
    
    l7=Button(f1, text="String",width=10, command=String)
    l7.pack()
    
    l8=Button(f1, text="List",width=10, command=List)
    l8.pack()
    
    l9=Button(f1, text="Tuple",width=10, command=Tuple)
    l9.pack()
    
    l10=Button(f1, text="Dictionary",width=10, command=Dictionary)
    l10.pack()
    
    l12=Button(f1, text="Functions",width=10, command=Functions)
    l12.pack()
    
    l13=Button(f1, text="Modules",width=10, command=Modules)
    l13.pack()
    
    l14=Button(f1, text="FileOperation",width=10, command=FileOperation)
    l14.pack()
    
    l15=Button(f1, text="ErrorHandel",width=10, command=ExceptionHandeling)
    l15.pack()
    
    l16=Button(f1, text="OOPS",width=10, command=OOPS)
    l16.pack()
    
    l17=Button(f1, text="Mysql",width=10, command=Mysql)
    l17.pack()
    
    l11=Button(f1, text="Networking",width=10, command=Networking)
    l11.pack()
    
    l18=Button(f1, text="Email",width=10, command=Email)
    l18.pack()

    
    l19=Button(f1, text="Multithreading",width=10, command=Multithreading)
    l19.pack()
    
    l20=Button(f1, text="GUI",width=10, command=GUI)
    l20.pack()

    root.mainloop()
