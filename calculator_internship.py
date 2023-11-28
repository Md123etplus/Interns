from math import *
from tkinter import *
def on_button_click(value):
    current = entry_var.get()
    entry_var.set(current + str(value))
    entry.icursor(END)
def clear():
    entry_var.set("")
    entry.icursor(END)
def evalu():
    try:
        result = eval(entry_var.get())
        entry_var.set(result)
        entry.icursor(END)
    except Exception as e:
        entry_var.set("Error")


root = Tk()
root.title("Calculator_TechnoHack")

entry_var = StringVar()
entry = Entry(root,textvariable=entry_var, justify="right", font=("Helvetica", 16))
entry.grid(row=0, column=0, columnspan=4)
for i in range(1, 10):
    Button(root, text=str(i), command=lambda i=i: on_button_click(i), padx=20, pady=20).grid(row=(i-1)//3 + 1, column=(i-1)%3)
Button(root, text="0",command= lambda: on_button_click(0),padx=20,pady=20).grid(row=4,column = 0)
Button(root, text="Clear",command= lambda: clear(),padx=20,pady=20).grid(row=4,column = 1)
Button(root, text="=",command= lambda: evalu(),padx=20,pady=20).grid(row=4,column = 2)
operations = ['+', '-', '*', '/']
for i, op in enumerate(operations):
    Button(root, text=op, command=lambda op=op: on_button_click(op), padx=20, pady=20).grid(row=i+1, column=3)
root.resizable(False,False)
root.mainloop()

