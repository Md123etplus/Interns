from tkinter import *
from random import *
from string import *
def copy_on():
    password_to_copy = lab_final.cget("text")
    root.clipboard_clear()
    root.clipboard_append(password_to_copy)
    root.update()
def validate_entry(a):
    var_int = int(var.get())
    lower_caracters = ascii_lowercase
    upper_caracters = ascii_uppercase
    numbers = digits

    symbols = punctuation
    all_caracters = lower_caracters + upper_caracters + numbers + symbols
    first_caracter= choice(lower_caracters + upper_caracters)
    rest_caracter = ''.join(choice(all_caracters) for _ in range(int(var_int-1)))
    password = first_caracter + rest_caracter
    frame.destroy()

    lab_final.config(text=password,cursor='ibeam')
    lab_final.pack(side="top",expand=True,padx=10,pady=10)
    copy_button.pack(side="bottom",expand=True,padx=10)
    '''root.clipboard_clear()
    root.clipboard_append(var.get())
    root.update()'''
root = Tk()
root.title("Passwor_Generator_Technohacks")
frame = Frame(root, bg="white", relief=SUNKEN)
frame.pack(side="top",expand=True)
lab_welcome = Label(frame,width=50,height=10, text="Welcome to Pass-Gen!", font=("Arial",25,"bold"))
lab_welcome.pack(side="top",expand=True,padx=10,pady=10)
lab_enter = Label(frame, text="Enter the length:", font=("Arial",15,"bold"))
lab_enter.pack(side="left",expand=True,padx=100,pady=10)
var = StringVar()
entry_1= Entry(frame,textvariable=var, font=("Arial"),borderwidth=5)
entry_1.pack(side="left",expand=True,padx=2,pady=10)
entry_1.bind("<Return>", validate_entry)

lab_final = Label(root,text="", font=("Arial",12,"bold"))
copy_button = Button(root,text="Copy", font=("Arial",12,"bold"),bg="green",relief="solid",command=copy_on)
root.mainloop()