import random
from tkinter import *
from tkinter.ttk import *

def low():
    entry.delete(0,END)
    length=var1.get()
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ""
 
    if var.get() == 1:
        for i in range(0, length):
            password = password + random.choice(lower)
        return password
 
    elif var.get() == 0:
        for i in range(0, length):
            password = password + random.choice(upper)
        return password
 
    elif var.get() == 3:
        for i in range(0, length):
            password = password + random.choice(digits)
        return password
    else:
        print("Please choose an option")
 
    
def generate():
    password1 = low()
    entry.insert(10, password1)

root = Tk()
var = IntVar()
var1 = IntVar()

root.title("Random Password Generator")
root.geometry("500x500+850+250")      
root.resizable(0, 0)
root.configure(bg = "pink") 

Random_password = Label(root, text="Password")
Random_password.place(x=30,y=70)
entry = Entry(root)
entry.place(x=100,y=70)

c_label = Label(root, text="Length")
c_label.place(x=30,y=150)

generate_button = Button(root, text="Generate", command=generate)

generate_button.place(x=200,y=400)

radio_low = Radiobutton(root, text="Low", variable=var, value=1)
radio_low.place(x=100,y=200)
radio_middle = Radiobutton(root, text="Medium", variable=var, value=0)
radio_middle.place(x=100,y=230)
radio_strong = Radiobutton(root, text="Strong", variable=var, value=3)
radio_strong.place(x=100,y=260)


combo = Combobox(root, textvariable=var1)
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
				17, 18, 19, 20, 21, 22, 23, 24, 25,
				26, 27, 28, 29, 30, 31, 32, "Length")
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.place(x=100,y=150)

root.mainloop()
