
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import Connection_DB

def add_details():
        id_val = id_entry.get()
        email_val = email_entry.get()
        name_val = name_entry.get()
        password_val = password_entry.get()
        class_val = class_comboBox.get()
        data = (id_val, email_val, name_val, password_val, class_val)
 
        if(len(id_val)==0 or len(str(email_val))==0 or len(str(name_val))==0 or len(password_val)==0 or len(str(class_val))==0):
           messagebox.showerror('Wornning!','All Data is Required, Please Enter Your Data')
        else :
            flagID = Connection_DB.searchStudentId(id_val)
            if(flagID==True): # This ID is Already Exist
                messagebox.showerror('Wornning!','Invalid ID , Try Again!')
 
            flagPassowrd = Connection_DB.searchStudentPassowrd(password_val)
            if(flagPassowrd==True): # This Passowd is Already Exist
                messagebox.showerror('Wornning!','Invalid Passowrd , Try Again!')
 
            flagEmail = Connection_DB.searchStudentEmail(email_val)
            if(flagEmail==True): # This Email is Already Exist
                messagebox.showerror('Wornning!','Invalid Email , Try Again!')
 
            if(flagID==False and flagPassowrd==False and flagEmail==False):
                treeview.insert('', 'end', values=data)
                Connection_DB.addStudent(id_val,email_val,name_val, password_val,class_val)
                messagebox.showinfo('System','Added successfully')
                resetValues()
 
 
    # Display new updated tree view 
def updateTreeView():
        students = Connection_DB.allStudents()
        # remove tree view from other display
        treeview.delete(*treeview.get_children())
        for row in students:
            treeview.insert('',END,values=row)
 
 
def edit_details():
        selected_item = treeview.selection()
        if len(selected_item) > 0:
            item_values = treeview.item(selected_item)['values']
            id_entry.delete(0, 'end')
            id_entry.insert(0, item_values[0])
            email_entry.delete(0, 'end')
            email_entry.insert(0, item_values[1])
            name_entry.delete(0, 'end')
            name_entry.insert(0, item_values[2])
            password_entry.delete(0, 'end')
            password_entry.insert(0, item_values[3])
            class_comboBox.set(item_values[4])
            # Update the command of the "Edit" button to call a different function
            edit_button.config(command=lambda: update_details(selected_item))
        else:
            id_val = id_entry.get()
            email_val = email_entry.get()
            name_val = name_entry.get()
            password_val = password_entry.get()
            class_val = class_comboBox.get()
            if(len(id_val)==0):
               messagebox.showerror('error','you should enter correct ID')
            else:   
                flagID = Connection_DB.searchStudentId(id_val)
                if(flagID==False): # Does not Exist
                     messagebox.showerror("error","This ID is not Exist")
                else: # ID is Exist
                    if(len(str(email_val)) > 0):
                        Connection_DB.updateStudentEmail(id_val, email_val)
                    if(len(str(name_val)) > 0):
                        Connection_DB.updateStudentName(id_val, name_val)
                    if(len(password_val) > 0):
                        Connection_DB.updateStudentPassowrd(id_val, password_val)
                    if(len(str(class_val)) > 0):
                        Connection_DB.updateStudentClass(id_val, class_val)
 
                    updateTreeView()
                    messagebox.showinfo('System','Updeted successfully')
                    resetValues()
 
    # Add a new function to update the details
def update_details(selected_item):
        id_val = id_entry.get()
        email_val = email_entry.get()
        name_val = name_entry.get()
        password_val = password_entry.get()
        class_val = class_comboBox.get()
        Connection_DB.updateStudent(id_val,email_val,name_val,password_val,class_val)
        # Update the values in the treeview
        treeview.item(selected_item, values=(id_val, email_val, name_val, password_val, class_val))
        # Clear the entry fields
        messagebox.showinfo('System','Updeted successfully')
        resetValues()
 
def delete_details():
        selected_item = treeview.selection()
        if len(selected_item) > 0:
            item_values = treeview.item(selected_item)['values']
            id_student=item_values[0]
            Connection_DB.deleteStudent(id_student)
            treeview.delete(selected_item)
            messagebox.showinfo('System','Deleted successfully')
            resetValues()
        else:  
           id_val = id_entry.get()
           if(len(id_val)==0):
                messagebox.showerror('error','Required Data, Please Enter Your Data')
           else: 
                 Connection_DB.deleteStudent(id_val)
                 updateTreeView()
                 messagebox.showinfo('System','Deleted successfully')
                 resetValues()
 
def resetValues():
        id_entry.delete(0, 'end')
        email_entry.delete(0, 'end')
        name_entry.delete(0, 'end')
        password_entry.delete(0, 'end')
        class_comboBox.set('')
 
def go_back():
        student_control_module.destroy()
        AdminScreen()
 
 
student_control_module = tk.Tk()
student_control_module.title('Student Control Module')
student_control_module.geometry('1250x400')
student_control_module.configure(bg='darkslategray')
 
    # Left Frame
left_frame = ttk.Frame(student_control_module)
left_frame.pack(side='left', padx=10, pady=10)
 
id_label = ttk.Label(left_frame, text='ID:')
id_label.grid(row=0, column=0, sticky='w')
id_entry = ttk.Entry(left_frame)
id_entry.grid(row=0, column=1)
 
email_label = ttk.Label(left_frame, text='Email:')
email_label.grid(row=1, column=0, sticky='w')
email_entry = ttk.Entry(left_frame)
email_entry.grid(row=1, column=1)
 
name_label = ttk.Label(left_frame, text='Name:')
name_label.grid(row=2, column=0, sticky='w')
name_entry = ttk.Entry(left_frame)
name_entry.grid(row=2, column=1)
 
password_label = ttk.Label(left_frame, text='Password:')
password_label.grid(row=3, column=0, sticky='w')
password_entry = ttk.Entry(left_frame, show='*')
password_entry.grid(row=3, column=1)
 
class_label = ttk.Label(left_frame, text='Class:')
class_label.grid(row=4, column=0, sticky='w')
 
class_vars = ['CS', 'SC', 'AI', 'IS']
class_comboBox = ttk.Combobox(left_frame, values=class_vars, state='readonly')
class_comboBox.grid(row=4, column=1)
 
add_button = ttk.Button(left_frame, text='Add', command=add_details)
add_button.grid(row=5, column=0, pady=10)
 
edit_button = ttk.Button(left_frame, text='Edit', command=edit_details)
edit_button.grid(row=5, column=1, pady=10)
 
delete_button = ttk.Button(left_frame, text='Delete', command=delete_details)
delete_button.grid(row=6, column=0, pady=10)
 
clear_button = ttk.Button(left_frame, text='Reset', command=resetValues)
clear_button.grid(row=6, column=1, pady=10)
 
back_button = ttk.Button(left_frame, text='Back', command=go_back)
back_button.grid(row=7, column=0, columnspan=2, pady=10)
 
    # Right Frame
right_frame = ttk.Frame(student_control_module)
right_frame.pack(side='right', padx=10, pady=10)
treeview = ttk.Treeview(right_frame, columns=('ID', 'Email', 'Name', 'Password', 'Class'), show='headings')
treeview.heading('ID', text='ID')
treeview.heading('Email', text='Email')
treeview.heading('Name', text='Name')
treeview.heading('Password', text='Password')
treeview.heading('Class', text='Class')
 
data =Connection_DB.allStudents()
for row in data:
   treeview.insert('',END,values=row)
treeview.pack()
 
student_control_module.mainloop()



