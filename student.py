from tkinter import *
from tkinter.ttk import Treeview

root=Tk()
root.title('Student')
w=600
h=400
root.geometry(f'{w}x{h}')
root.configure(bg='darkslategray')
root.resizable(False,False)
##left frame##
leftframe=Frame(root)
leftframe['bg']='darkslategray'


welcome_lbl=Label(leftframe,text='Welcome ,',bg='darkslategray',fg='white')
welcome_lbl.grid(row=0,column=0 ,padx=10,pady=30)




total_lbl=Label(leftframe,text='Total:',bg='darkslategray',fg='white')
total_entry=Entry(leftframe)
total_lbl.grid(row=1,column=0,padx=10,pady=30)
total_entry.grid(row=1,column=1,padx=10,pady=10)


attended_lbl=Label(leftframe,text='Attended :',bg='darkslategray',fg='white')
attended_lbl.grid(row=2,column=0,padx=10,pady=30)
attended_entry=Entry(leftframe)
attended_entry.grid(row=2,column=1,padx=10,pady=10)


missed_lbl=Label(leftframe,text='Missed :',bg='darkslategray',fg='white')

missed_lbl.grid(row=3,column=0,padx=10,pady=30)
missed_entry=Entry(leftframe)
missed_entry.grid(row=3,column=1,padx=10,pady=10)

leftframe.pack(side='left')


#right frame
right_frame = Frame(root)
right_frame.pack(side='right',padx=20  )
treeview = Treeview(right_frame, columns=('Date', 'Statues'), show='headings')
treeview.heading('Date', text='Date')
treeview.heading('Statues', text='Status')

treeview.pack()

root.mainloop()
   