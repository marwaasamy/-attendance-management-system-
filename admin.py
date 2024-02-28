



from tkinter import *  
root = Tk()             
root.geometry('500x400')
root.configure(bg='darkslategray')
# Create a Button
#to write lable
lbl=Label(root,text="Welcome admin,")
lbl.grid(row=1,column=0)


#first botton
btn1 = Button(root, text = 'STUDENTS',  bd = '10',
                          command = root.destroy)

btn1.config(height=2,width=50)
btn1.grid(row=3,column=1)


#second botton
btn2 = Button(root, text = 'Teachers', bd = '10',
                          command = root.destroy)
btn2.grid(row=4,column=1)
btn2.config(height=2,width=50)




root.mainloop()