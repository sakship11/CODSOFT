# importing the required modules  
#importing the tkinter module as tk  
import tkinter as tk                   
from tkinter import ttk                 
from tkinter import messagebox          
import sqlite3 as sql    #importing the sqlite3 module as sql   

def add_list():  
    get_task = thr_label.get()  # getting the string from the entry field  
    if len(get_task) == 0:    # checking whether the string is empty or not  
       messagebox.showerror( 'Field is Empty!',"Please fill Task")  
    else:  
        type_task.append(get_task)          # adding the string to the tasks list  
        obj.execute('insert into type_task values (?)', (get_task ,))    #execute() method to execute a SQL statement       
        update_list()           
        thr_label.delete(0, 'end')  
  
def update_list():  
    clear_list()  
    for task in type_task:  # iterating through the strings in the list  
        listbox.insert('end', task)  
  
def delete_list():     
    try:          
        add = listbox.get(listbox.curselection())    # getting the selected entry from the list box          
        if add in type_task:         # checking if the stored value is present in the tasks list      
            type_task.remove(add)              
            update_list()              
            obj.execute('delete from type_task where title = ?', (add,))  
    except:            
        messagebox.showerror('No Task Selected',"Please select Task")      # displaying the message box with 'No task Selected' message for an exception    
  
def delete_all_list():  
    all_task = messagebox.askyesno('Delete All', 'Are you sure?')     #displaying a message box to ask user for confirmation  
    if all_task == True:  
        while(len(type_task) != 0):
            type_task.pop()         # using the pop() method to pop out the elements from the list  
            obj.execute('delete from type_task')          
            update_list()  
   
def clear_list():  
    listbox.delete(0, 'end')

def retrieve_database():  
    while(len(type_task) != 0):           #while loop to iterate through the elements in the tasks list      
        type_task.pop()       
    for row in obj.execute('select title from type_task'):       # iterating through the rows in the database table   
        type_task.append(row[0])  

 # main function   
if __name__ == "__main__":      
    top = tk.Tk()      
    top.title("To-Do List ")       
    top.geometry("500x500+850+250")      
    top.resizable(0, 0)   
    top.configure(bg = "pink")  
     
     #connect() method to connect to the database  
    connection = sql.connect('to_doList.db')      
    obj = connection.cursor()      # creating an object of the cursor class  
    obj.execute('create table if not exists type_task (title text)')  # using the execute() method to execute a SQL statement  
  
    type_task = []  
          
    main_frame = tk.Frame(top, bg = "pink")
    main_label= ttk.Label(  
        main_frame,  
        text = "To-Do List",  
        font = ("Castellar", "35"),  
        background = "pink",  
        foreground = "black"  
    )     
    main_label.pack(padx = 20, pady = 20)
    main_frame.pack(fill = "both")  
    
    sec_frame = tk.Frame(top, bg = "pink")
    sec_label = ttk.Label(  
        sec_frame,  
        text = "Enter the Task:",  
        font = ("Times New Roman", "12", "bold"),  
        background = "pink",  
        foreground = "#000000"  
    )      
    sec_label.place(x = 30, y = 40)
    sec_frame.pack(side = "left", expand = True, fill = "both")  
          
    thr_frame = tk.Frame(top, bg = "pink")
    thr_label = ttk.Entry(  
        sec_frame,  
        font = ("Times New Roman", "12"),  
        width = 20,  
        background = "#FFF8DC",  
        foreground = "black"  
    )      
    thr_label.place(x = 30, y = 80)
    thr_frame.pack(side = "right", expand = True, fill = "both")  
    
    add_button = ttk.Button(  
        sec_frame,  
        text = "Add Task",  
        width =26,  
        command = add_list  
    )
    add_button.place(x = 30, y = 120)
    
    del_button = ttk.Button(  
        sec_frame,  
        text = "Delete Task",  
        width =26,  
        command = delete_list  
    )
    del_button.place(x = 30, y = 160)
    
    del_all_button = ttk.Button(  
        sec_frame,  
        text = "Delete All type_task",  
        width =26,  
        command = delete_all_list  
    )  
    del_all_button.place(x = 30, y = 200)  
 
    listbox = tk.Listbox(  
        thr_frame,
        height = 15, 
        width = 30,  
        selectmode = 'SINGLE',  
        background = "white",   #FFFFFF 
        foreground = "black",  #000000
        selectbackground = "#CD853F",  
        selectforeground = "#FFFFFF"  
    )  
    listbox.place(x = 10, y = 20)  

    retrieve_database()  
    update_list()   
    connection.commit()  
    obj.close()  
    top.mainloop()  
    
