import tkinter as tk
from tkinter import *
from tkinter import messagebox

quizque=[
    {
        "q":" Who developed the Python language?",
        "o":["Zim Den","Guido van Rossum","Niene Stom","Wick van Rossum"],
        "a":"Guido van Rossum",
    },
    {
        "q":" Which of the following statements is correct regarding the object-oriented programming concept in Python?",
        "o":["Classes are real-world entities while objects are not real","Objects are real-world entities while classes are not real","Both objects and classes are real-world entities","All of the above"],
        "a":"Objects are real-world entities while classes are not real",
    },
    {
        "q":"What is the method inside the class in python language?",
        "o":["Object","Function","Attribute","Argument"],
        "a":"Function",
    },
    {
        "q":"Which of the following functions is a built-in function in python language?",
        "o":["val()","print()","printf()","None of these"],
        "a":"print()",
             
    },
    {
        "q":"What is the maximum possible length of an identifier?",
        "o":["16","32","64","None of these above"],
        "a":"None of these above",
    },
]

score =0
current_que =0

def nextpage():
    l1.destroy()
    inst.destroy()
    rules.destroy()
    btn.destroy()
    
def new_que(que_no): 
    if que_no < len(quizque):
        questions.config(text=quizque[que_no]["q"])
        for i in range(4):
            rdo_buttons[i].config(text=quizque[que_no]["o"][i], font=('Times New Roman',14),background="white")
    else:
        result()

def nxtpage():   
    global current_que
    global score
    selected = int(radio_var.get())

    if selected == -1:
        messagebox.showwarning("Warning","Please select one option.",font=("Times New Roman",12,"Italic"))
    else:
        a = quizque[current_que]["a"]
        if quizque[current_que]["o"][selected]== a:
            score+=1
                        
        current_que += 1
        radio_var.set(-1)
                        
        if current_que < len(quizque):
            new_que(current_que)
        else:
            result()

def result():
    messagebox.showinfo("Result",f"You got {score}/{len(quizque)}")
    root.quit()

root = tk.Tk()
root.title("Quiz")
root.geometry("888x600")
root.configure(bg="white")
root.resizable(0,0)

img1 = PhotoImage(file="image1.png")

l1 = Label(
    root,
    image = img1,
    background="white",
    border=5
)
l1.pack(pady=(40,0))

btn = Button(
    root,
    text = ' Start',
    bd = '7',
    background="green",
    command=nextpage,
)
btn.pack(pady=(40,0))

inst = Label(
    root,
    text="Read the Rules and \nClick Start once you are ready",
    background="white",
    font=("Consolas",14),
    justify="center"

)
inst.pack(pady=(10,150))

rules = Label(
    root,
    text="This quiz contain 5 questions\n once you select a radio button that will be final choice\n hence think before you select",
    width=100,
    font =("Times new roman",14),
    background ="black",
    foreground ="yellow"
    
)	
rules.pack()

questions=tk.Label(
    root,
    text="",
    wraplength=700,
    font=("Times New Roman",14,"bold"),
    background="white"
)
questions.pack(pady=50)

radio_var=tk.StringVar()
radio_var.set(-1)

rdo_buttons=[] 
for i in range(4):
    r_btn =tk.Radiobutton(root,text="",value=i, variable=radio_var)
    rdo_buttons.append(r_btn)
    r_btn.pack(anchor = CENTER)
    

nxt_btn=tk.Button(
    root,
    text="Next",
    font=("Times New Roman",14,"bold"),
    command=nxtpage,
)

nxt_btn.pack(pady=50)
new_que(0)

root.mainloop()

