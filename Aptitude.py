import logging
import time
from tkinter import *
import random
format="%(asctime)s : %(message)s"
logging.basicConfig(format=format,level=logging.INFO,filename="ProjectLog.log",filemode="w",datefmt="%D, %H:%M:%S")

user_answer=[]

indexes=[]
ques = 1
answers = [0,0,0,1,3,1,0,3,3,3]
def Apti():
    logging.info("Login: Test Function Called.")
    questions = [
        "Which Function is called as \n Anonemous Function?",
        "Which of the following functions \n takes an Entry Input in Python ?",
        "How many Loops are there \n in Python ?",
        "Which of The Following is must to\n Execute a Python Code ?",
        "Which of the wollowing Symbol is \n used for single line comment?",
        "The append Method adds value \nto the list at the  ?",
        "Which of the following is Syntax of \n Constructor?",
        "Which of The following is not a \n Datatype in python? ?",
        "Which of the following keyword is used \n to create a function in Python ?",
        "Which of the following has more \n Precedance(Higher Priority)?",
    ]
    answers_choice = [
        ["lambda","def","built-in","None",],
        ["get()","input()","gets()","scan()",],
        ["2","3","1","4",],
        ["TURBO C","Py Interpreter","Notepad","IDE",],
        ["//","/","/*","#",],
        ["custom location","end","center","beginning",],
        ["def __init__()","init()","def _constructor_","All of the Above",],
        ["String","Numeric","List","Database",],
        ["function","void","fun","def",],
        ["+","*","/","()",],
    ] 

    # 

    #user_answer = []

    #indexes = []
    def gen():
        global indexes
        while(len(indexes) < 10):
            x = random.randint(0,9)
            if x in indexes:
                continue
            else:
                indexes.append(x)


    def showresult(score):
        lblQuestion.destroy()
        r1.destroy()
        r2.destroy()
        r3.destroy()
        r4.destroy()
        labelimage = Label(
            root,
            background = "#ffffff",
            border = 0,
        )
        labelimage.pack(pady=(50,30))
        labelresulttext = Label(
            root,
            font = ("Consolas",20),
            background = "#ffffff",
        )
        labelresulttext.pack()
        if score >= 20:
            img = PhotoImage(file="images/great.png")
            labelimage.configure(image=img)
            labelimage.image = img
            labelresulttext.configure(text="You Are Excellent !!"+str(score),font=("times new roman",12))
        elif (score >= 10 and score < 20):
            img = PhotoImage(file="images/thumbs_up_through_wall.png")
            labelimage.configure(image=img,width=250,height=250)
            labelimage.image = img
            labelresulttext.configure(text="You Can Be Better !!"+str(score),font=("times new roman",12))
        else:
            img = PhotoImage(file="images/120px-Face-sad.svg.png")
            labelimage.configure(image=img)
            labelimage.image = img
            labelresulttext.configure(text="You Should Work Hard !!"+str(score),font=("times new roman",12))


    def calc():
        global indexes,user_answer,answers
        x = 0
        score = 0
        for i in indexes:
            if user_answer[x] == answers[i]:
                score = score + 5
            x += 1
        showresult(score)


    #ques = 1
    def selected():
        global radiovar,user_answer
        global lblQuestion,r1,r2,r3,r4
        global ques
        x = radiovar.get()
        user_answer.append(x)
        radiovar.set(-1)
        if ques < 10:
            lblQuestion.config(text= questions[indexes[ques]])
            r1['text'] = answers_choice[indexes[ques]][0]
            r2['text'] = answers_choice[indexes[ques]][1]
            r3['text'] = answers_choice[indexes[ques]][2]
            r4['text'] = answers_choice[indexes[ques]][3]
            ques += 1
        else:
            # print(indexes)
            # print(user_answer)
            # these two lines were just developement code
            # we don't need them
            calc()
        




    def startquiz():
        logging.info("Test: Test Started.")
        root.geometry("300x500")
        root.configure(bg="sky blue")
        l=Label(root,text="Test Your Brains",bg="red",fg="black",width=500,height=2,font=("times new roman",15)).pack()
        global lblQuestion,r1,r2,r3,r4
        lblQuestion = Label(
            root,
            text = questions[indexes[0]],
            font = ("Consolas",10),
            justify=LEFT,
            width = 500,
            background = "white",
        )
        lblQuestion.pack(pady=(50,30),anchor=W)

        global radiovar
        radiovar = IntVar()
        radiovar.set(-1)

        r1 = Radiobutton(
            root,
            text = answers_choice[indexes[0]][0],
            font = ("Times", 12),
            value = 0,
            variable = radiovar,
            command = selected,
            background = "skyblue",
        )
        r1.pack(pady=5,anchor=W)

        r2 = Radiobutton(
            root,
            text = answers_choice[indexes[0]][1],
            font = ("Times", 12),
            value = 1,
            variable = radiovar,
            command = selected,
            background = "skyblue",
        )
        r2.pack(pady=5,anchor=W)

        r3 = Radiobutton(
            root,
            text = answers_choice[indexes[0]][2],
            font = ("Times", 12),
            value = 2,
            variable = radiovar,
            command = selected,
            background = "skyblue",
        )
        r3.pack(pady=5,anchor=W)

        r4 = Radiobutton(
            root,
            text = answers_choice[indexes[0]][3],
            font = ("Times", 12),
            value = 3,
            variable = radiovar,
            command = selected,
            background = "skyblue",
        )
        r4.pack(pady=5,anchor=W)


    def startIspressed():
        labelimage.destroy()
        labeltext.destroy()
        lblInstruction.destroy()
        lblRules.destroy()
        btnStart.destroy()
        gen()
        startquiz()



    root = Toplevel()
    root.title("Aptitude  Trainer")
    root.geometry("300x500")
    root.config(background="#ffffff")
    root.resizable(0,0)


    img1 = PhotoImage(file="images/transparentGradHat.png")

    labelimage = Label(
        root,
        image = img1,
        background = "#ffffff",
    )
    labelimage.pack(pady=(40,0))

    labeltext = Label(
        root,
        text = "Aptitude  Trainer",
        font = ("Comic sans MS",11,"bold"),
        background = "#ffffff",
    )
    labeltext.pack(pady=(0,50))

    img2 = PhotoImage(file="images/Frame.png")

    btnStart = Button(
        root,
        image = img2,
        relief = FLAT,
        border = 0,
        command = startIspressed,
    )
    btnStart.pack()

    lblInstruction = Label(
        root,
        text = "Read The Rules And\nClick Start Once You Are ready",
        background = "#ffffff",
        font = ("Consolas",10),
        justify = "center",
    )
    lblInstruction.pack(pady=(10,50))

    lblRules = Label(
        root,
        text = "This test contains 10 questions\nYou will get 20 seconds to solve a question\nOnce you select a radio button that will be a final choice\nhence think before you select",
        width = 100,
        font = ("Times",10),
        background = "#000000",
        foreground = "#FACA2F",
    )
    lblRules.pack()
    root.mainloop()
