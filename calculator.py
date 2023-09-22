from tkinter import *

root = Tk() 
root.geometry("330x330")  
root.resizable(0, 0)  
root.title("Calculator")


# This Function continuously updates the input field whenever you enter a number
def click_btn(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# 'clear_btn' function :This is used to clear the input field
def clear_btn(): 
    global expression 
    expression = "" 
    input_text.set("")
 
# equal_btn:This method calculates the expression present in input field 
def equal_btn():
    global expression
    result = str(eval(expression)) # 'eval':This function is used to evaluates the string expression directly
    input_text.set(result)
    expression = ""
 
expression = "" 
#StringVar():It is used to get the instance of input field
 
input_text = StringVar() 
frame_for_input = Frame(root,
                        width=312,
                        height=50,
                        bd=0,
                        highlightbackground="black",
                        highlightcolor="black",
                        highlightthickness=2) 
frame_for_input.pack(side=TOP)
 
input_field = Entry(frame_for_input,
                    font=('Times New Roman', 19, 'bold'),
                    textvariable=input_text,
                    width=50, bg="#eee",
                    bd=0,
                    justify=RIGHT)
input_field.grid(row=0, column=0) 
input_field.pack(ipady=10) # 'ipady' is internal padding to increase the height of input field
 
btn_all_frame = Frame(root, width=312, height=272.5, bg="grey")  #Frame for buttons
btn_all_frame.pack()

#created first row
clear = Button(btn_all_frame,
               text = "C",
               fg = "black",
               width = 32,
               height = 3,
               bd = 0,
               bg = "red",
               cursor = "hand2",
               command = lambda: clear_btn()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
 
divide = Button(btn_all_frame,
                text = "/",
                fg = "black",
                width = 10,
                height = 3,
                bd = 0,
                bg = "#eee",
                cursor = "hand2",
                command = lambda: click_btn("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
 
#second row
seven = Button(btn_all_frame,
               text = "7",
               fg = "black",
               width = 10,
               height = 3,
               bd = 0,
               bg = "#fff",
               cursor = "hand2",
               command = lambda: click_btn(7)).grid(row = 1, column = 0, padx = 1, pady = 1)

eight = Button(btn_all_frame,
               text = "8",
               fg = "black",
               width = 10,
               height = 3,
               bd = 0,
               bg = "#fff",
               cursor = "hand2",
               command = lambda: click_btn(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
 
nine = Button(btn_all_frame,
              text = "9",
              fg = "black",
              width = 10,
              height = 3,
              bd = 0,
              bg = "#fff",
              cursor = "hand2",
              command = lambda: click_btn(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
 
multiply = Button(btn_all_frame,
                  text = "*",
                  fg = "black",
                  width = 10,
                  height = 3,
                  bd = 0,
                  bg = "#eee",
                  cursor = "hand2",
                  command = lambda: click_btn("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
 
#third row
four = Button(btn_all_frame,
              text = "4",
              fg = "black",
              width = 10,
              height = 3,
              bd = 0,
              bg = "#fff",
              cursor = "hand2",
              command = lambda: click_btn(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
 
five = Button(btn_all_frame,
              text = "5",
              fg = "black",
              width = 10,
              height = 3,
              bd = 0,
              bg = "#fff",
              cursor = "hand2",
              command = lambda: click_btn(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
 
six = Button(btn_all_frame,
             text = "6",
             fg = "black",
             width = 10,
             height = 3,
             bd = 0,
             bg = "#fff",
             cursor = "hand2",
             command = lambda: click_btn(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
 
minus = Button(btn_all_frame,
               text = "-",
               fg = "black",
               width = 10,
               height = 3,
               bd = 0,
               bg = "#eee",
               cursor = "hand2",
               command = lambda: click_btn("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
 
# fourth row
 
one = Button(btn_all_frame,
             text = "1",
             fg = "black",
             width = 10,
             height = 3,
             bd = 0,
             bg = "#fff",
             cursor = "hand2",
             command = lambda: click_btn(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
 
two = Button(btn_all_frame,
             text = "2",
             fg = "black",
             width = 10,
             height = 3,
             bd = 0,
             bg = "#fff",
             cursor = "hand2",
             command = lambda: click_btn(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
 
three = Button(btn_all_frame,
               text = "3",
               fg = "black",
               width = 10,
               height = 3,
               bd = 0,
               bg = "#fff",
               cursor = "hand2",
               command = lambda: click_btn(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
 
plus = Button(btn_all_frame,
              text = "+",
              fg = "black",
              width = 10,
              height = 3,
              bd = 0,
              bg = "#eee",
              cursor = "hand2",
              command = lambda: click_btn("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
 
# fourth row 
zero = Button(btn_all_frame,
              text = "0",
              fg = "black",
              width = 21,
              height = 3,
              bd = 0,
              bg = "#fff",
              cursor = "hand2",
              command = lambda: click_btn(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
 
point = Button(btn_all_frame,
               text = ".",
               fg = "black",
               width = 10,
               height = 3,
               bd = 0,
               bg = "#eee",
               cursor = "hand2",
               command = lambda: click_btn(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
 
equals = Button(btn_all_frame,
                text = "=",
                fg = "black",
                width = 10,
                height = 3,
                bd = 0,
                bg = "green",
                cursor = "hand2",
                command = lambda: equal_btn()).grid(row = 4, column = 3, padx = 1, pady = 1)
 
root.mainloop()
