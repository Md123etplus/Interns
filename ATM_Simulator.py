from tkinter import *
from time import *

def enter():
    mot_de_passe = var.get()
    if len(mot_de_passe) == 4 and mot_de_passe not in a:
        frame.destroy()
        user_frame.pack(side="top",expand=True)
        user_frame.grid_propagate(False)
        lab2.pack()
        cancel_button.pack(side="bottom", expand=True, padx=20, pady=20)
        check_button.pack(side="top",expand=True,padx=20,pady=20)
        withdraw_button.pack(side="right", expand=True,padx=20,pady=20)
        releve_button.pack(side="left", expand=True, padx=20,pady=20)

        check_button.configure(borderwidth=5)
        withdraw_button.configure(borderwidth=5)
        releve_button.configure(borderwidth=5)
        cancel_button.configure(borderwidth=5)
    else:
        lab1.configure(text="Error, wrong passcode!")
def sucess():
    lab5.configure(text="WITHDRAW SUCCESFULLY DONE!")

def enter1():
    i = var1.get()
    try:

        if int(i) not in range(1,1000000000):
            lab4.configure(text="Your sold must be a number!")
            var1.set("")
        else:

            withdraw_frame.destroy()
            releve_frame.pack(side="top", expand=True)
            #lab5.configure(text="Please Wait ...")
            lab5.pack(side="top", expand=True)


            root.after(3000,sucess())

    except:
        lab4.configure(text="Your sold must be a number!")

def cancel():
    user_frame.destroy()
    lab3.pack(side="top",expand=True)
def check():
    user_frame.destroy()
    releve_frame.pack(side="top", expand=True)
    lab5.pack(side="top", expand=True)
    lab5.configure(text="Your sold is:...")
def withdraw():
    user_frame.destroy()

    withdraw_frame.pack(side="top",expand=True)
    lab4.pack(side="top",expand=True)
    ok1_button.pack(side="bottom", expand=True)
    ok1_button.configure(borderwidth=5)
    e2.pack(side="bottom",expand=True)

def releve():
    user_frame.destroy()
    releve_frame.pack(side="top",expand=True)
    lab5.pack(side="top",expand=True)
def home():
    pass
def canc():
    current = var.get()
    current = current[:-1]
    var.set(current)
def on_click(value):
    current = var.get()

    var.set(current+str(value))
    e1.icursor(END)
def start():
    star.destroy()

    lab1.grid(row=0, column=0, columnspan=3)

    e1.grid(row=1, column=0, columnspan=10,padx=10,pady=10)
    for i in range(1, 10):
        Button(frame,text=str(i), command=lambda i=i: on_click(i), padx=25, pady=20).grid(row=(i - 1) // 3 + 4,
                                                                                          column=(i - 1) % 3)
    ok_button.grid(row=7,column=2)
    back.grid(row=7,column=0)
root= Tk()
root.title("ATM SIMULATOR")
root.configure(bg="blue")
frame = Frame(root, padx=20,pady=40, bg="green")
frame.pack(side="top",expand=True)
frame.pack_propagate(False)
withdraw_frame = Frame(root, padx=20,pady=40, bg="green")
user_frame = Frame(root, padx=20,pady=40, bg="green")
releve_frame= Frame(root, padx=20,pady=40, bg="green")
#check_frame = Frame(root, padx=20,pady=40, bg="green")
lab1 = Label(frame, text="ENTER YOUR PIN",bg="green",padx=40,pady=50, font=("black",20))
lab2 = Label(user_frame, text="WELCOME!",bg="green",padx=40,pady=50, font=("black",20))
lab3 = Label(root, text="THANK YOU!",bg="green",padx=40,pady=50, font=("black",20))
lab4 = Label(withdraw_frame, text="ENTER YOUR SOLD:",bg="green",padx=40,pady=50, font=("black",20))
lab5 = Label(releve_frame, text="This is your releve: ##...##",bg="green",padx=40,pady=50, font=("black",20))
var1 = StringVar()
var = StringVar()
a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
e2 = Entry(withdraw_frame,textvariable = var1, borderwidth=5,justify="right")
star = Button(root, command= start,text="START", padx=40, pady=40, bg="green")
star.pack(side="top", expand=True)

e1= Entry(frame,textvariable = var, borderwidth=5,justify="right")
ok_button = Button(frame,text="ENTER",padx=20,pady=20, command=lambda: enter())
ok1_button = Button(withdraw_frame,text="ENTER",padx=20,pady=15, command=lambda: enter1())
back = Button(frame,text="CANCEL",padx=20,pady=20, command=lambda: canc())
check_button =Button(user_frame,text="CHECK BALANCE",padx=20,pady=20,width=10, height=2, command=lambda: check())
withdraw_button =Button(user_frame,text="WITHDRAW",padx=20,pady=20,bg="blue",width=10, height=2, command=lambda: withdraw())
releve_button =Button(user_frame,text="RELEVE",padx=20,pady=20,bg="yellow",width=10, height=2, command=lambda: releve())
cancel_button = Button(user_frame,text="RETIRE MY CARD",padx=20,pady=20,bg="red",width=10, height=2,command=lambda: cancel())
return_button =Button(user_frame,text="RETURN HOME",padx=20,pady=20,bg="red",width=10, height=2,command=lambda: home())
#root.resizable(False,False)
root.mainloop()