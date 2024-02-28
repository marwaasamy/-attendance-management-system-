
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import Connection_DB


def add_details():
    id_val = id_entry.get()
    username_val = username_entry.get()
    name_val = name_entry.get()
    password_val = password_entry.get()
    dept_val = dept_comboBox.get()
    data = (id_val, username_val, name_val, password_val, dept_val)
    if(len(id_val)==0 or len(str(username_val))==0 or len(str(name_val))==0 or len(password_val)==0 or len(str(dept_val))==0):
       messagebox.showerror('error','All Data is Required, Please Enter Your Data')
    else :
        treeview.insert('', 'end', values=data)
        Connection_DB.addStudent(id_val,name_val,username_val, password_val,dept_val)

def edit_details():
    selected_item = treeview.selection()
    if len(selected_item) > 0:
        item_values = treeview.item(selected_item)['values']
        id_entry.delete(0, 'end')
        id_entry.insert(0, item_values[0])
        username_entry.delete(0, 'end')
        username_entry.insert(0, item_values[1])
        name_entry.delete(0, 'end')
        name_entry.insert(0, item_values[2])
        password_entry.delete(0, 'end')
        password_entry.insert(0, item_values[3])
        dept_comboBox.set(item_values[4])
        # Update the command of the "Add" button to call a different function
        add_button.config(command=lambda: update_details(selected_item))
    else:
        id_val = id_entry.get()
        username_val = username_entry.get()
        name_val = name_entry.get()
        password_val = password_entry.get()
        dept_val = dept_comboBox.get()
        if(len(id_val)==0):
           messagebox.showerror('error','Required Data, Please Enter Your Data')
        else:   
             Connection_DB.updateStudent(id_val,name_val,username_val,password_val,dept_val)

# Add a new function to update the details
def update_details(selected_item):
    id_val = id_entry.get()
    username_val = username_entry.get()
    name_val = name_entry.get()
    password_val = password_entry.get()
    dept_val = dept_comboBox.get()
    Connection_DB.updateStudent(id_val,name_val,username_val,password_val,dept_val)
    # Update the values in the treeview
    treeview.item(selected_item, values=(id_val, username_val, name_val, password_val, dept_val))
    # Clear the entry fields
    clear_details()

def delete_details():
    selected_item = treeview.selection()
    if len(selected_item) > 0:
        item_values = treeview.item(selected_item)['values']
        id_teh=item_values[0]
        Connection_DB.deleteStudent(id_teh)
        treeview.delete(selected_item)
    else:  
       id_val = id_entry.get()
       username_val = username_entry.get()
       name_val = name_entry.get()
       password_val = password_entry.get()
       dept_val = dept_comboBox.get()
       if(len(id_val)==0):
            messagebox.showerror('error','Required Data, Please Enter Your Data')
       else: 
             Connection_DB.deleteStudent(id_val)

def clear_details():
    id_entry.delete(0, 'end')
    username_entry.delete(0, 'end')
    name_entry.delete(0, 'end')
    password_entry.delete(0, 'end')
    dept_comboBox.set('')

def go_back():
    # Add your code to handle going back to the previous GUI here
    #root.destroy()
    import admin
    #pass

root = tk.Tk()
root.title('Student Control Module')
root.geometry('500x400')
root.configure(bg='darkslategray')

# Left Frame
left_frame = ttk.Frame(root)
left_frame.pack(side='left', padx=10, pady=10)

id_label = ttk.Label(left_frame, text='ID:')
id_label.grid(row=0, column=0, sticky='w')
id_entry = ttk.Entry(left_frame)
id_entry.grid(row=0, column=1)

username_label = ttk.Label(left_frame, text='Email:')
username_label.grid(row=1, column=0, sticky='w')
username_entry = ttk.Entry(left_frame)
username_entry.grid(row=1, column=1)

name_label = ttk.Label(left_frame, text='Name:')
name_label.grid(row=2, column=0, sticky='w')
name_entry = ttk.Entry(left_frame)
name_entry.grid(row=2, column=1)

password_label = ttk.Label(left_frame, text='Password:')
password_label.grid(row=3, column=0, sticky='w')
password_entry = ttk.Entry(left_frame, show='*')
password_entry.grid(row=3, column=1)

dept_label = ttk.Label(left_frame, text='Class:')
dept_label.grid(row=4, column=0, sticky='w')

dept_vars = ['CS', 'SC', 'AI', 'IS']
dept_comboBox = ttk.Combobox(left_frame, values=dept_vars, state='readonly')
dept_comboBox.grid(row=4, column=1)

add_button = ttk.Button(left_frame, text='Add', command=add_details)
add_button.grid(row=5, column=0, pady=10)

edit_button = ttk.Button(left_frame, text='Edit', command=edit_details)
edit_button.grid(row=5, column=1, pady=10)

delete_button = ttk.Button(left_frame, text='Delete', command=delete_details)
delete_button.grid(row=6, column=0, pady=10)

clear_button = ttk.Button(left_frame, text='Reset', command=clear_details)
clear_button.grid(row=6, column=1, pady=10)

back_button = ttk.Button(left_frame, text='Back', command=go_back)
back_button.grid(row=7, column=0, columnspan=2, pady=10)

# Right Frame
right_frame = ttk.Frame(root)
right_frame.pack(side='right', padx=10, pady=10)
treeview = ttk.Treeview(right_frame, columns=('ID', 'Email', 'Name', 'Password', 'Class'), show='headings')
treeview.heading('ID', text='ID')
treeview.heading('Email', text='Email')
treeview.heading('Name', text='Name')
treeview.heading('Password', text='Password')
treeview.heading('Class', text='Class')
treeview.pack()

root.mainloop()


