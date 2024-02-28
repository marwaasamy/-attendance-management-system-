
import tkinter as tk
from tkinter import ttk
from tkinter import *

selected_item = None  # Global variable to store the selected item

def add_details():
    id_val = id_entry.get()
    name_val = name_entry.get()
    date_val = date_entry.get()
    choice = Rbt_var.get()
    data = (id_val, name_val, date_val, choice)
    treeview.insert('', 'end', values=data)
    clear_details()

def edit_details():
    global selected_item
    selected_item = treeview.selection()
    if len(selected_item) == 0:
        return
    item_values = treeview.item(selected_item)['values']
    id_entry.delete(0, 'end')
    id_entry.insert(0, item_values[0])
    name_entry.delete(0, 'end')
    name_entry.insert(0, item_values[1])
    date_entry.delete(0, 'end')
    date_entry.insert(0, item_values[2])
    Rbt_var.set(item_values[3])
    add_button.config(command=update_details)  # Remove lambda and selected_item parameter
   

def update_details():
    global selected_item  # Add global keyword
    id_val = id_entry.get()
    name_val = name_entry.get()
    date_val = date_entry.get()
    status_val = Rbt_var.get()
    treeview.item(selected_item, values=(id_val, name_val, date_val, status_val))
    clear_details()

def delete_details():
    selected_item = treeview.selection()
    if len(selected_item) > 0:
        treeview.delete(selected_item)

def clear_details():
    id_entry.delete(0, 'end')
    name_entry.delete(0, 'end')
    date_entry.delete(0, 'end')
    Rbt_var.set('Present')

root = tk.Tk()
root.title('User Details')
root.geometry('500x400')
root.configure(bg='darkslategray')

# Left Frame
left_frame = ttk.Frame(root)
left_frame.pack(side='left', padx=10, pady=10)

id_label = ttk.Label(left_frame, text='ID:')
id_label.grid(row=0, column=0, sticky='w')
id_entry = ttk.Entry(left_frame)
id_entry.grid(row=0, column=1)

name_label = ttk.Label(left_frame, text='Name:')
name_label.grid(row=2, column=0, sticky='w')
name_entry = ttk.Entry(left_frame)
name_entry.grid(row=2, column=1)

date_label = ttk.Label(left_frame, text='Date:')
date_label.grid(row=3, column=0, sticky='w')
date_entry = ttk.Entry(left_frame)
date_entry.grid(row=3, column=1)

Rbt_var = StringVar()
Rbt_var.set('Present')
rd1 = Radiobutton(left_frame, text='Absent', value='Absent', variable=Rbt_var)
rd1.grid(row=5, column=1, pady=5, sticky='w')

rd2 = Radiobutton(left_frame, text='Present', value='Present', variable=Rbt_var)
rd2.grid(row=5, column=0, pady=5, sticky='w')

add_button = ttk.Button(left_frame, text='Add', command=add_details)
add_button.grid(row=6, column=0, pady=10)

edit_button = ttk.Button(left_frame, text='Edit', command=edit_details)
edit_button.grid(row=6, column=1, pady=10)

delete_button = ttk.Button(left_frame, text='Delete', command=delete_details)
delete_button.grid(row=7, column=0, pady=10)

clear_button = ttk.Button(left_frame, text='Clear', command=clear_details)
clear_button.grid(row=7, column=1, pady=10)

# Right Frame
right_frame = ttk.Frame(root)
right_frame.pack(side='right', padx=10, pady=10)
treeview = ttk.Treeview(right_frame, columns=('ID', 'Name', 'Date', 'Status'), show='headings')
treeview.heading('ID', text='ID')
treeview.heading('Name', text='Name')
treeview.heading('Date', text='Date')
treeview.heading('Status', text='Status')
treeview.pack()

root.mainloop()