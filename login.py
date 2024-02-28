from tkinter import *
from tkinter.ttk import Combobox
import tkinter.messagebox

import Connection_DB

##gui_basics##
root=Tk()
root.title('login')
w=500
h=300
root.geometry(f'{w}x{h}')
root.configure(bg='darkslategray')



#frame#
frame=Frame(root)
frame['bg']='darkslategray'



#username and entery#
username_lbl=Label(frame,text='Username',bg='darkslategray',fg='white')
username_entry=Entry(frame)
username_lbl.grid(row=0,column=0 ,padx=10,pady=10)
username_entry.grid(row=0,column=1,padx=10,pady=10)


#password and entery#
password_lbl=Label(frame,text='Password',bg='darkslategray',fg='white' )
password_entry=Entry(frame,show='*')
password_lbl.grid(row=1,column=0,padx=10,pady=10)
password_entry.grid(row=1,column=1,padx=10,pady=10)

#combobow###
Pos= StringVar()

combo_lbl=Label(frame,text='Position',bg='darkslategray',fg='white')
objects=['student','admin','teacher']
combo=Combobox(frame,values=objects,state='readonly',width=16,textvariable=Pos)
combo_lbl.grid(row=2,column=0,padx=10,pady=10)
combo.grid(row=2,column=1,padx=10,pady=10)



def action():
    Position=str(Pos.get())
    Email=str(username_entry.get())
    Passowrd=str(password_entry.get())
    
    # To Ensure That Is There Is No Field Is Empty
    if(len(str(Position))==0 or len(Email)==0 or len(Passowrd)==0 ):
        tkinter.messagebox.askokcancel('System','All Data is Required, Please Enter Your Data')
        
        
    ### Make Action depending on PositionValue ###
    
    # ADMIN
    if(Position=='admin'):
        
        if(Email=='ADMIN' and Passowrd=='1111'):
            root.destroy()
            import Admin
        else: # Wrong Values
            tkinter.messagebox.askokcancel('System','Your Email Or Passowrd is Wrong , Try Again!')
            
    # STUDENT        
    elif(Position=='student'):
    
        flag = Connection_DB.searchStudent(Passowrd, Email)
        
        if(flag==True):
            root.destroy()
            import Student
        else:
            tkinter.messagebox.askokcancel('System','Your Email Or Passowrd is Wrong , Try Again!')
            
    # TEACHER
    else: # Position == 'teacher'
        
        flag = Connection_DB.searchTeacher(Passowrd, Email)
        
        if(flag==True):
            root.destroy()
            import TeacherControlModule1
        else:
            tkinter.messagebox.askokcancel('System','Your Email Or Passowrd is Wrong , Try Again!')
    
    
    
    
##login button###
login_btn=Button(frame,text='login',width=7,fg='darkslategray',command=action)
login_btn.grid(row=3,column=1,columnspan=2,padx=1,pady=1)



frame.place(anchor='center',relx=.5,rely=.5)
root.mainloop()





