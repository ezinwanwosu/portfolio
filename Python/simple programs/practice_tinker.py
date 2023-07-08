from tkinter import *
master = Tk()
name = StringVar()
buttonClicked = True
def beenClicked():
    
    name1 = name.get()
    Label(master,text = f'Hello {name1}').grid(row=4)
Label(master, text='Enter Your Name').grid(row=0)
Label(master, text='Enter Your Email').grid(row=1)
Label(master, text='Enter Your Password').grid(row=2)


e1 = Entry(master,bg = 'white',textvariable = name)
e2 = Entry(master,bg = 'white')
e3 = Entry(master,bg = 'white',show='*')
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
Button(master,text = 'Submit',activebackground = 'grey',activeforeground = 'blue',command = beenClicked).grid(row=3)
mainloop()


